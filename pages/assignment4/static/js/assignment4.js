const getUser = () => {
    const formInputValue = document.getElementById("frontend-request").user_number.value;
    fetch(` https://reqres.in/api/users/${formInputValue}`)
        .then((response) => response.json())
        .then((object) => {
            const data = object?.data;
            document.getElementById("place_holder_for_response").innerHTML =
                `
                    <br>
                    <h3>${data?.first_name} ${data?.last_name}</h3>
                    <h4>${data?.email}</h4>
                    <img src="${data?.avatar}" alt="Profile Picture"/>
                `
        })
        .catch((err) => console.log(err));
}