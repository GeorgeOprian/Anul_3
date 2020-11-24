window.onload = function (){
    changeProperties(); 
} 


function postComment(){
    var inputText = document.getElementById("comment_input").value.trim();
    var defaultMessage = "Write your opinion about my website here.";
    
    if (inputText != defaultMessage && inputText != ""){
        var newDiv = document.createElement("div");
        newDiv.className = "comment";
        var newParagraph = document.createElement("p");
        var text = document.createTextNode(inputText);
        newParagraph.appendChild(text);
        newDiv.appendChild(newParagraph);
        var commentsSections = document.getElementById("comments_section");
        commentsSections.appendChild(newDiv)
        document.getElementById("comment_input").value = defaultMessage.trim();
    }
}


function deleteContent(){
    var textArea = document.getElementById("comment_input");
    var inputText = textArea.value.trim();
    if (inputText != ""){
        var defaultMessage = "Write your opinion about my website here.";
        if (inputText == defaultMessage.trim()){
            textArea.value = "";
        }    
    }
    
}

function deleteComments(){
    var comments_section = document.getElementById("comments_section");
    var comments = document.getElementsByClassName("comment");
    var commentsLen =  comments.length;
    for (let i = 0; i < commentsLen; i++) {
        comments_section.removeChild(comments[0]);
    }
}
function displayImages(){
    var figures = document.getElementsByClassName("to_hide");  /// aici sa creez obiectul
    var buttons = document.getElementsByTagName("button");
    var button = buttons[0];
    for (let figure of figures) {
        // alert(figure.figcaption);
        if (figure.style.visibility != "visible"){
            figure.style.visibility = "visible";
            button.textContent = "Hide";
        } else {
            figure.style.visibility = "hidden";
            button.textContent = "Press here to see another pictures";
        }
    }
}

function changeProperties (){
    var george = document.getElementById("george_pic");
    george.onmouseover = changeGeorgeMouseOver;
    george.onmouseout = changeGeorgeMouseOut;

}


function changeGeorgeMouseOver (){
    var george = document.getElementById("george_pic");
    george.style.boxShadow = "10px 10px 5px grey";
    george.style.marginRight = "10px";
    george.style.marginBottom = "10px";
}

function changeGeorgeMouseOut (){
    var george = document.getElementById("george_pic");
    george.style.boxShadow = "";
    george.style.marginRight = "";
    george.style.marginBottom = "";
}

