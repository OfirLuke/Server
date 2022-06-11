
const markCurrentPage = () => {
    document.querySelectorAll('nav a').forEach(currElement => {
        if (currElement.href.includes(`${window.location.pathname}`)) {
            currElement.classList.add('curr-page')     
        }
    });;
}

const submitMessage = () => {
    let validInptut = true;
    const firstName = document.forms["contact-form"]["FName"].value;
    const lastName = document.forms["contact-form"]["LName"].value;
    const email = document.forms["contact-form"]["email"].value;
    const agree = document.forms["contact-form"]["agree"].checked;

    if(firstName === "" && firstName.length < 2){
        validInptut = false;
    }
    if(lastName === "" && lastName.length < 2){
        validInptut = false;
    }
    if(email === ""){
        validInptut = false;
    }
    if(agree === false){
        validInptut = false;
    }

    if(validInptut){
        document.getElementById("submit-place-holder").innerHTML = `Thanks ${firstName} For Contacting`
    }
}
    function onHover()
    {
        const element = document.getElementById("main-photo");
        element.attributes("src","../static/goodlifeHover.jpg" )
        console.log(element)
    }

    function offHover()
    {
    
    }


