const currentPostId = $('#post_id').val();
const currentLoginId = $('#current_login_id').val();

function postComment() {
    if ($('#comment').val()) {
        console.log('object');
        $.post({
            url: `../add-post-comment/`,
            type: 'post',
            data: {
                'post_id': currentPostId,
                'comment': $('#comment').val()
            },
            success: getUserComment
        })
    }
}

$('#button-submit-post-comment').click(() => {
    postComment();
    document.getElementById('comment').value = '';
    return false;
})

function getUserComment() {
    $('#comment-container').empty();
    $.get(
        '../post-comment-json',
        (response) => {
            for (let i = 0; i < response.length; i++) {
                if (response[i].fields.post == currentPostId) {
                    let dateObj = new Date(response[i].fields.created_on);
                    let date = dateObj.toString().slice(0, 16)
                    $('#comment-container').append(
                        `<div
                            class="aspect-video py-2 px-4 mb-4 rounded-lg break-inside-avoid bg-charcoal-800">
                            <div class="flex items-center gap-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"
                                    preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                                    <path fill="none"
                                        d="M8.007 24.93A4.996 4.996 0 0 1 13 20h6a4.996 4.996 0 0 1 4.993 4.93a11.94 11.94 0 0 1-15.986 0ZM20.5 12.5A4.5 4.5 0 1 1 16 8a4.5 4.5 0 0 1 4.5 4.5Z" />
                                    <path fill="#2563eb"
                                        d="M26.749 24.93A13.99 13.99 0 1 0 2 16a13.899 13.899 0 0 0 3.251 8.93l-.02.017c.07.084.15.156.222.239c.09.103.187.2.28.3c.28.304.568.596.87.87c.092.084.187.162.28.242c.32.276.649.538.99.782c.044.03.084.069.128.1v-.012a13.901 13.901 0 0 0 16 0v.012c.044-.031.083-.07.128-.1c.34-.245.67-.506.99-.782c.093-.08.188-.159.28-.242c.302-.275.59-.566.87-.87c.093-.1.189-.197.28-.3c.071-.083.152-.155.222-.24ZM16 8a4.5 4.5 0 1 1-4.5 4.5A4.5 4.5 0 0 1 16 8ZM8.007 24.93A4.996 4.996 0 0 1 13 20h6a4.996 4.996 0 0 1 4.993 4.93a11.94 11.94 0 0 1-15.986 0Z" />
                                </svg>
                                <div class="flex flex-col min-w-0">
                                    <p class="text-base font-base text-white truncate">
                                        <span class="font-medium text-blue-500">@${response[i].fields.username}</span> ${response[i].fields.comment}
                                    </p>
                                    <p class=" text-gray-400 text-sm">
                                        ${date}
                                    </p>
                                </div>
                            </div>
                        </div>`
                    )
                }
            }
        }
    )
}

function getPostLikes() {
    $.get(
        "../../post-tech/post-tech-json",
        (response) => {
            for (let i = 0; i < response.length; i++) {
                if (response[i].pk == currentPostId) {
                    document.getElementById('likes-container').innerHTML = response[i].fields.likes.length
                    $('#svg-love-container').empty();
                    if (response[i].fields.likes.includes(Number(currentLoginId))) {
                        $('#svg-love-container').append(`
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="mr-2 -ml-1 w-5 h-5" viewBox="0 0 16 16">
                            <path fill="#FF1212" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                        </svg>
                        `);
                    } else {
                        $('#svg-love-container').append(`
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="mr-2 -ml-1 w-5 h-5" viewBox="0 0 16 16">
                            <path fill="#FFFFFF" d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                        </svg>
                        `);
                    }

                }
            }
        }
    )
}

function likePost(pk) {
    $.post(
        {
            url: `../../post-tech/like-post/${pk}/`,
            type: 'post',
            data: {},
            success: getPostLikes
        }
    )
}
$(`#like-button`).attr(
    'onclick',
    `likePost(${currentPostId})`
);

$(document).ready(() => {
    getUserComment()
    getPostLikes()
});