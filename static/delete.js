const deleteButtons = document.querySelectorAll(".deleteButton");

deleteButtons.forEach(button => {
    button.addEventListener("click", function(event) {
    const confirmed = confirm("Are you sure you want to delete this?")
    if (confirmed){
        const url = button.dataset.url
        fetch(url, {
                method: "DELETE"
            }).then(() => {
                location.reload();
            });
    }
})})
