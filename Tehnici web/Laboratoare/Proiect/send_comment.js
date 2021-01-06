var form = document.getElementById("comment_input_form");

form.onsubmit = function (submit) {
    
    submit.preventDefault();

    var commentText = document.getElementsByName("comment_input")[0].value;
    var postCommentInput = document.getElementsByName("postComment")[0].value;

    var postComment = true;

    // if (postCommentInput != "Post") {
    //     postComment = false;
    // }

    var objectSent = {}

}