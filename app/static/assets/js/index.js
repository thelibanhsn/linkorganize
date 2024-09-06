

let copy_link_btn = document.getElementById('copy-link-btn')

function copy_link() {
    let copy_link_value = document.getElementById('copy-link-value')
    // Copy the text inside the text field
    navigator.clipboard.writeText(copy_link_value.value);

    // Alert the copied text
    alert("Copied the text: " + copy_link_value.value);
}