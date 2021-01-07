
window.onload = function () {
    var form = document.getElementsByTagName("form")[0];
    form.onsubmit = function (submit) {
        submit.preventDefault();
    }
}

function registerUser() {
    if (passwordsMatch()) {
        //trimit cu post la /singUp

        var xmlRequest = new XMLHttpRequest();

        if (!xmlRequest) {
            alert("Cannot create XmlHttpRequest ");
            return false;
        }
        
        newUser = null; 
        xmlRequest.open('POST', 'http://localhost:8080/sign_up', true);

        var form = document.getElementsByTagName("form")[0];
        var username = document.getElementsByName("username")[0].value;
        var email = document.getElementsByName("email")[0].value;
        var password = document.getElementsByName("password")[0].value;

        newUser = { 'username': username, 'email': email, 'password': password }
        
        xmlRequest.onreadystatechange = function () {
            alert(xmlRequest.responseText);
        }
        var stringOb = JSON.stringify(newUser);
        xmlRequest.send(stringOb);



        if (xmlRequest.readyState == 4) {
            if (xmlRequest.status == 200) {
                alert(xmlRequest.responseText);
            } else {
                alert("There were problems with the query");
            }
        } 
        
    }

}

function passwordsMatch() {
    if (document.getElementById('password').value !=
        document.getElementById('ConfirmPassword').value) {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = 'password does not match';
        return false;
    }
    return true;

}