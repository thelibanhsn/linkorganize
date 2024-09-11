from flask import Blueprint, flash, url_for, render_template, redirect, send_file
from ..extensions import login_required, current_user,db,login_manager
from .forms import AddLinkForm, UpdateLinkForm, DeleteLinkForm
from .models import SocialLinkModel
import qrcode
from io import BytesIO
import base64
import io
from ..auth.models import User

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates' , url_prefix='/dashboard')

# All unauthorised return to login
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth_bp.login'))

@dashboard_bp.route('/', methods = ['GET', 'POST'])
@login_required
def dashboard():    
    social_links = SocialLinkModel.query.filter_by(user_id = current_user.id)
    qr_code_base64 = None
    if current_user.qr_code:
        qr_code_base64 = base64.b64encode(current_user.qr_code).decode('utf-8')
    return render_template('/dashboard.html', social_links=social_links, qr_code=qr_code_base64)

@dashboard_bp.route('/add-social-link', methods=["GET", "POST"])
@login_required
def add_social():
    form = AddLinkForm()

    if form.validate_on_submit():
        data = SocialLinkModel(social_name = form.social_name.data.lower(), social_username = form.social_username.data.lower(), user_id=current_user.id)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    return render_template('/add_social.html', form=form)


@dashboard_bp.route('/edit-social-link/<social_link_id>', methods=["GET", "POST"])
@login_required
def update_social_link(social_link_id):
    form = UpdateLinkForm()
    social_link_data = SocialLinkModel.query.filter_by(id = social_link_id).first()

    if not social_link_data:
        # Handle case where social link with given ID does not exist
        flash('Social link not found.', 'error')
        return redirect(url_for('dashboard_bp.dashboard'))
    
    if form.validate_on_submit():
        social_link_data.social_name = form.social_name.data
        social_link_data.social_username = form.social_username.data
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    form.social_name.data = social_link_data.social_name
    form.social_username.data = social_link_data.social_username
    return render_template('/update_social.html', social_link_data=social_link_data, form=form)

@dashboard_bp.route('/delete-social-link/<social_link_id>', methods=["GET", "POST"])
@login_required
def delete_social_link(social_link_id):
    form = DeleteLinkForm()
    social_link_data = SocialLinkModel.query.filter_by(id = social_link_id).first()

    if not social_link_data:
        # Handle case where social link with given ID does not exist
        flash('Social link not found.', 'error')
        return redirect(url_for('dashboard_bp.dashboard'))
    
    if form.validate_on_submit():
        db.session.delete(social_link_data)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    form.social_name.data = social_link_data.social_name
    form.social_username.data = social_link_data.social_username
    return render_template('/delete_social.html', social_link_data=social_link_data, form=form)

# function generates qrcode
def generate_qr_code(username):
    url = f"http://127.0.0.1:5000/{username}"
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Convert the image to binary data
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    
    return byte_io.getvalue() 

@dashboard_bp.route('/generate-qrcode/<username>')
@login_required
def generate_qr(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('You are not logged in')
        return redirect(url_for('auth_bp.login'))
    
    qr_code_data = generate_qr_code(username)
    user.qr_code = qr_code_data
    db.session.commit()

    return redirect(url_for('dashboard_bp.dashboard'))
    

# Download Qrcode
@dashboard_bp.route('/download-qr')
def download_qr():

    qr_image = None
    if current_user.qr_code:
        # Convert binary data back to an image format
        qr_image = io.BytesIO(current_user.qr_code)
        qr_image.seek(0)
        
        # Send the file as a downloadable image (PNG)
    return send_file(qr_image, mimetype='image/png', as_attachment=True, download_name=f"{current_user.username}_qr.png")