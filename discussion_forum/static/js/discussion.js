const createNestedReplyInput = (replyPk, replyUser) => {
    return `
    <div class="flex flex-col bg-charcoal-800 rounded-lg py-4 px-6 gap-2" id="nested-reply-input-parent">
    <p class="font-medium text-white">Replying to <span class="font-bold text-blue-600">${replyUser}</span></p>
    <textarea id="nested-reply-input" class="rounded-lg bg-charcoal-800 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500" placeholder="Enter your message here"></textarea>
    <div class="flex">
        <button type="button"
            class="rounded bg-blue-600 text-white py-2 px-4 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300"
                onClick="postNestedReply(${replyPk})">
                Post
            </button>
        </div>
    </div>
    `;
}

const showReplyInput = (replyPk, replyUser) => {
    $("#nested-reply-input-parent").remove();
    $(`#nested-replies-${replyPk}`).append(createNestedReplyInput(replyPk, replyUser));
}

const createReplyCard = (data, loggedUser) => {
    return `
    <div class="flex flex-col bg-charcoal-800 rounded-lg py-4 px-6 break-words" id="reply-${data.pk}">
        <p class="font-bold text-blue-600">${(data.user == loggedUser) ? 'You' : '@' + data.user}</p>
        <p class="text-white">${data.content}</p>
        <div class="flex justify-between">
            <p class="text-gray-500">On ${data.date}</p>
            ${loggedUser == "" ? "" : `
            <button class="bg-transparent text-blue-600" onClick="showReplyInput(${data.replyParentPk}, '${data.user}')">Reply</button>
            `}
        </div>
    </div>`;
}

const createReply = (data, loggedUser) => {
    return `
    <div class="flex flex-col gap-4">
        ${createReplyCard(data, loggedUser)}
        <div class="flex flex-col ml-16 gap-4" id="nested-replies-${data.pk}">
        </div>
    </div>`;
}

const postNestedReply = (pk) => {
    $.post(`/discussion/replies/${pk}/add/`, {
        content: $("#nested-reply-input").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    (data, status) => {
        $(`#nested-replies-${pk}`).append(createReplyCard(data.reply, data.user));
        $("#nested-reply-input").val("");
        $("#nested-reply-input-parent").remove();
    });
}

const getNestedReplies = (pk) => {
    $.get(`/discussion/replies/${pk}/`, (data) => {
        for(var i = 0; i < data.replies.length; i++){
            $(`#nested-replies-${pk}`).append(createReplyCard(data.replies[i], data.user));
        }
    });
}

const postReply = (pk) => {
    $.post(`/discussion/${pk}/replies/add/`, {
        content: $("#content-field").val(),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
    (data, status) => {
        $("#replies").append(createReply(data.reply, data.user));
        $("#content-field").val("");
    });
}

const getReplies = (pk) => {
    $.get(`/discussion/${pk}/replies/`, (data) => {
        for(var i = 0; i < data.replies.length; i++){
            $("#replies").append(createReply(data.replies[i], data.user));
            getNestedReplies(data.replies[i].pk);
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