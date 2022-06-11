const markCurrentPage = () => {
    document.querySelectorAll("nav a").forEach((currElement) => {
        if (currElement.href.includes(`${window.location.pathname}`)) {
            currElement.classList.add("curr-page");
        }
    });
};

const submitElement = document.getElementById("contact-form");
if(submitElement){
    addEventListener("click", function(event){
        event.preventDefault()
    })
}

const validateMyForm = () => {
    let validInptut = true;
    const firstName = document.forms["contact-form"]["FName"].value;
    const lastName = document.forms["contact-form"]["LName"].value;
    const email = document.forms["contact-form"]["email"].value;
    const agree = document.forms["contact-form"]["agree"].checked;

    if (firstName.length < 2) {
        validInptut = false;
    }
    if (lastName.length < 2) {
        validInptut = false;
    }
    if (email === "" || !email?.includes("@") || !email?.includes(".")) {
        validInptut = false;
    }
    if (agree === false) {
        validInptut = false;
    }

    if (validInptut) {
        document.getElementById("submit-place-holder").innerHTML = `<p>תודה ${firstName} ${lastName}<br/>פרטים נוספים ישלחו לכתובת המייל: ${email}</p>`;
    }
};

function onHover() {
    const element = document.getElementById("main-photo");
    element.setAttribute("src", "../static/goodlifeHover.jpg");
}

function offHover() {
    const element = document.getElementById("main-photo");
    element.setAttribute("src", "../static/goodlife.jpg");
}

const setImgBorderOnHover = (img) => {
    img.style = "border-style: groove; border-color: black; border-width: 7px;";
}

const setImgBorderOffHover = (img) => {
    img.style = "border-width: 0px;";
}