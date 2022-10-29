const createReplyCard = (data, loggedUser) => {
    return `<div class="flex flex-col bg-charcoal-800 rounded-lg p-4 break-words">
      <p class="font-bold text-blue-600">${(data.user == loggedUser) ? 'You' : "@" + data.user}</p>
      <p class="text-white">${data.content}</p>
      <p class="text-gray-500">On ${data.date}</p>
    </div>`;
}

const postReply = (pk) => {
    $.post(`/discussion/${pk}/replies/add/`, {
        content: $("#content-field").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    (data, status) => {
        console.log(data)
        $("#replies").append(createReplyCard(data.reply, data.user));
        $("#content-field").val("");
    });
}

const getReplies = (pk) => {
    $.get(`/discussion/${pk}/replies/`, (data) => {
        for(var i = 0; i < data.replies.length; i++){
            $("#replies").append(createReplyCard(data.replies[i], data.user));
        }
    });
}

$(document).ready(() => {
    const pk = $("#main-discussion").attr("pk");

    getReplies(pk);

    $('#post-reply').click(() => {
        postReply(pk);
        return false;
    });
});