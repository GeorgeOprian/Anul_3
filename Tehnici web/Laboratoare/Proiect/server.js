var http = require('http');
var url = require ('url');
var fs = require('fs');

var server = http.createServer(
    function(req, res){
        
        var body = "";
        var url_parsed = url.parse(req.url, true);

        if (url_parsed.pathname == "/sign_up") {

            req.on ('data', function(data){
                body += data;
            })

            req.on ('end', function (){
                console.log("Am primit o cerere");
                var receivedUser = JSON.parse(body);
                
                console.log("ob1: ");
                console.log(receivedUser);
                //console.log(ob2);

                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/html');
               
                if (tryToInsertNewUser(receivedUser) == false) {
                    res.write("User already registered");
                } else {
                    res.write("User registered successfully");
                }
                res.end();
            })
        }

        if (url_parsed.pathname == "/log_in") {
            
            var query = url_parsed.query;
            var waitingUserToLogIn = {'username' : query.username, 'password': query.password};
            

            var listOfUsers = [];
            if (fs.existsSync("users.json")) {
                var usersJson = fs.readFileSync("users.json");
                listOfUsers = JSON.parse(usersJson);
            }

            var resStatus;
            resStatus = 404;
                resString = "Could not find the user";
            if (listOfUsers != []) {
                console.log(waitingUserToLogIn);
                console.log(listOfUsers);
                for (user of listOfUsers){
                    if (userAndPasswordMatch(user, waitingUserToLogIn)){
                        resStatus = 200;
                        resString = "User logged in successfully";
                    }
                }
            }
            res.statusCode = resStatus;
            res.setHeader('Content-Type', 'text/html');
            res.write("<h3>Response: </h3>\n" + resString);
            res.end();
        }
    }
    ) 


server.listen(8080);
console.log("Listening on port 8080")


// function insertUser()


function tryToInsertNewUser (receivedUser) {
    var listOfUsers = [];
    console.log("try to register");
    if (fs.existsSync("users.json")){
        var inputList = fs.readFileSync("users.json");
        listOfUsers = JSON.parse(inputList);
    }
    
    if (!isUserInDataBase (receivedUser, listOfUsers))
        listOfUsers.push(receivedUser);
    else {
        console.log("register failed");
        return false;
    }

    console.log(listOfUsers);

    fs.writeFileSync("users.json", JSON.stringify(listOfUsers))

    return true;
}

function isUserInDataBase (receivedUser, listOfUsers) {
    for (user of listOfUsers){
        if (compareUsersOnInsert(user, receivedUser) == true){
            return true;
        }
    }
}

function userAndPasswordMatch(currentUser, requestedUser){
    if (currentUser.username == requestedUser.username && currentUser.password == requestedUser.password)
        return true;
    return false 
}

function compareUsersOnInsert (user1, user2) {
    if (user1.username == user2.username || user1.email == user2.email) {
        return true;
    }
    return false;
}