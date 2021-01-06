var http = require('http');
var url = require ('url')

var server = http.createServer(
    function(req, res){
        console.log("Asta e url neparsat: " + url);
        var url_parts = url.parse(req.url, true);
        console.log("Asta e url parsat: " + url_parts);
        var query = url_parts.query;

        console.log("Acesta este qury ul: " + query.comment_input + " " + query.postComment)

        res.writeHead(200, {'Content-Type': 'text/plain'});
        // res.end("Buna " + query.name + ' din ' + query.city);
    }
    ) 

server.listen(8080);
console.log("Listening on port 8080")