const createDiscussionPost = (data) => {
    return `<div class="flex flex-col bg-charcoal-800 rounded-lg p-4 break-words">
      <p class="italic font-bold text-gray-400">${data.user[0]}</p>
      <p>${data.content}</p>
    </div>`;
}

const loadDiscussion = () => {
    $.get("/discussion/get-discussion/", (data) => {
        for (var i = 0; i < data.length; i++) {
            const post = createDiscussionPost(data[i].fields);
            $("#forum").append(post);
        }
    });
}

const postDiscussion = () => {
    $.post("/discussion/post-discussion-forum/", {
        content: $("#content-field").val(),
        csrfmiddlewaretoken: "{{ csrf_token }}"
    },
        (data, status) => {
            const post = createDiscussionPost(data[0].fields);
            $("#forum").append(post);
            $("#content-field").val("");
        });
}

$(document).ready(() => {
    loadDiscussion();

    $('#post-discussion').click(() => {
        postDiscussion();
        return false;
    });
});