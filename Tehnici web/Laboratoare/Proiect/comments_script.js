
window.onload = function(){
    document.querySelector('#comment_input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          postComment()
        }
    });
    var comments = document.querySelector("#display_comments");
    comments.addEventListener(
        'click', 
        function(){
            var commentsList = getCommentsFromLocalStorage();
            showHiddenComments(commentsList);
            alert("p");
            
        }
    )
    var hiddenCommentsSection = comments.parentElement;//document.getElementById("comments_section").nextElementSibling;
    hiddenCommentsSection.addEventListener(
        'click',
        function(event){
            // var commentsList = getCommentsFromLocalStorage();
            // showHiddenComments(commentsList);
            // var sectionComputedStyle =  window.getComputedStyle(hiddenCommentsSection);
            // var defaultColor = "RGB(255, 255, 255)";
            // if (sectionComputedStyle.backgroundColor.toLowerCase() == defaultColor.toLowerCase()) {
            //     hiddenCommentsSection.style.backgroundColor = getRandomColor();//"#b3cccc";
            // } else {
            //     hiddenCommentsSection.style.backgroundColor = "rgb(255, 255, 255)"
            //     //event.stopPropagation();
            // }
            if (event.target.tagName == "DIV"){
                hiddenCommentsSection.style.newBackgroundColor = "#b3cccc"; 
            }
            else {
                hiddenCommentsSection.style.newBackgroundColor = getRandomColor();
                if (hiddenCommentsSection.style.newBackgroundColor == "#ffffff")
                    event.stopPropagation();
            }
            hiddenCommentsSection.style.backgroundColor = hiddenCommentsSection.style.newBackgroundColor;
            alert("div");
            
            
            
        },
        true
    )

    var brokenA = document.getElementById("broken_a");

    brokenA.addEventListener(
        "click",
        function(event){
            event.preventDefault();
            alert("This link is broken")
        }
        )
    
    
}



function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function showHiddenComments(commentsList){
    var hiddenSection = document.getElementById("hidden_comments");
    //ar merge ceva asemanator cu strcat
    for (let i = 0; i < commentsList.length; i++){
        hiddenSection.innerHTML += commentsList[i];
    }
}

function getCommentsFromLocalStorage() {
    var commentsListJSON = localStorage.getItem("commentsList");
    return JSON.parse(commentsListJSON);
}

function postComment(){
    var main = document.getElementsByTagName("main")[0];

    var inputText = main.children[3].value.trim();//document.getElementById("comment_input").value.trim();
    var defaultMessage = "Write your opinion about my website here.";

    ///e o problema ca la enter imi pune textul default in text area si apoi imi trece pe rand nou cu textul

    if (inputText != defaultMessage && inputText != ""){

        var newComment = createNewComment(inputText);
        
        //clear the textbox
        //document.getElementById("comment_input").value = "";
        inputText = "";
        var post = document.getElementById("post");
        if (post.checked) {
            postCommentInCommentSection(newComment);
        }
        else{
            saveCommentToLocalStorage (newComment);
        }

    }
}

function saveCommentToLocalStorage (newDiv){
    var commentsList;
    if (localStorage.getItem("commentsList") == null){
       commentsList = new Array();
       
    } else {
        commentsListJSON = localStorage.getItem('commentsList')
        commentsList = JSON.parse(commentsListJSON);
    }
    var newDivHtmlContentent = newDiv.outerHTML;
    commentsList.unshift(newDivHtmlContentent);
    var commentsListToString = JSON.stringify(commentsList);
    localStorage.setItem("commentsList", commentsListToString); 
}

function postCommentInCommentSection(newDiv){
    var commentsSections = document.getElementById("comments_section");
    commentsSections.appendChild(newDiv)
}

function createNewComment(inputText) {
    var newDiv = document.createElement("div");
    newDiv.className = "comment";
    //create a new paragraph
    var newParagraph = createCommentParagraph(inputText);
    newDiv.appendChild(newParagraph);

    //create a new date
    var dateParagraph = createDateParagraph()
    newDiv.appendChild(dateParagraph)
    return newDiv;
}

function createCommentParagraph(inputText){
    var newParagraph = document.createElement("p");
    var text = document.createTextNode(inputText);
    newParagraph.appendChild(text);

    return newParagraph;
}
function createDateParagraph(){
    var dateParagraph = document.createElement("p");
    dateParagraph.classList.add("comment-date");
    var dateSpan = document.createElement("span");
    dateSpan.innerHTML = getFormatedDate();
    dateParagraph.innerHTML = "Posted on: ";
    dateParagraph.appendChild(dateSpan);
    return dateParagraph;
}


function getFormatedDate () {
    var currentDate = getCurrentDate();
    return (currentDate.time + " - " + currentDate.date)
}

function getCurrentDate() {
    var d = new Date();
    this.time = d.getHours() + ":" + d.getMinutes();
    this.date = d.getDate() + "." + (d.getMonth() + 1) + "." + d.getFullYear();
    return this;
}


function deleteComments(){
    var comments_section = document.getElementById("comments_section");
    var comments = document.getElementsByClassName("comment");
    var commentsLen =  comments.length;
    for (let i = 0; i < commentsLen; i++) {
        comments_section.removeChild(comments[0]);
    }
}

function test()
{
    var arr = document.getElementsByClassName("comment");
    var arrString = [];
    for (let elem of arr){
        console.log(JSON.stringify(elem))
    }
    
}