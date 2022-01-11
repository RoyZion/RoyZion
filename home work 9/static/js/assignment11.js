function frontend_func() {
    number = document.getElementById("f_number");
    url = "https://reqres.in/api/users/"+number.value
    fetch(url).then(
        response => response.json()
    ).then((response_obj) => {
        console.log(response_obj.data)
        return users_to_html(response_obj.data)
    }
    ).catch(
        error => console.log(error)
    )
}

function users_to_html(response_obj) {
    const current_main = document.querySelector("main");
    current_main.innerHTML = `
        <img src="${response_obj.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj.name}</span>
            <br>
            <a href="mailto:${response_obj.email}">Send Email</a>
            <br><br>
        </div>
    `;
}