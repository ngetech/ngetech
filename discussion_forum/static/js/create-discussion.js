const createDiscussion = () => {
    $.post("/discussion/create-discussion/post/", {
        title: $("#title-field").val(),
        content: $("#content-field").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    (data, status) => {
        window.location.href = "/discussion/";
    });
}

$(document).ready(() => {
    $('#create-discussion').click(() => {
        createDiscussion();
        return false;
    });
});