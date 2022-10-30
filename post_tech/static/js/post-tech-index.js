const modal = document.getElementById('post-tech-modal');
const openModalButton = document.getElementById('open-post-tech-modal-button');
openModalButton.addEventListener(
    'click',
    () => modal.classList.toggle('hidden')
);

const closeModalButton = document.getElementById('close-post-tech-modal-button');
closeModalButton.addEventListener(
    'click',
    () => modal.classList.toggle('hidden')
)

function getAllPost() {
    $.get(
        './post-tech-json',
        (res) => {
            $('#post-tech-container').empty();
            for (let i = 0; i < res.length; i++) {
                let dateObj = new Date(res[i].fields.date);
                let date = dateObj.toString().slice(0, 16)
                console.log();
                $('#post-tech-container').append(
                    `<a href="../post-detail/user-post-detail/${res[i].pk}">
                        <div class="aspect-video p-8 mb-4 rounded-lg break-inside-avoid bg-charcoal-800 {% if user.is_authenticated %} hover:bg-charcoal-700 {% endif %}">
                            <div class="flex items-center gap-3">
                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"
                                    preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
                                    <path fill="none"
                                        d="M8.007 24.93A4.996 4.996 0 0 1 13 20h6a4.996 4.996 0 0 1 4.993 4.93a11.94 11.94 0 0 1-15.986 0ZM20.5 12.5A4.5 4.5 0 1 1 16 8a4.5 4.5 0 0 1 4.5 4.5Z" />
                                    <path fill="#2563eb"
                                        d="M26.749 24.93A13.99 13.99 0 1 0 2 16a13.899 13.899 0 0 0 3.251 8.93l-.02.017c.07.084.15.156.222.239c.09.103.187.2.28.3c.28.304.568.596.87.87c.092.084.187.162.28.242c.32.276.649.538.99.782c.044.03.084.069.128.1v-.012a13.901 13.901 0 0 0 16 0v.012c.044-.031.083-.07.128-.1c.34-.245.67-.506.99-.782c.093-.08.188-.159.28-.242c.302-.275.59-.566.87-.87c.093-.1.189-.197.28-.3c.071-.083.152-.155.222-.24ZM16 8a4.5 4.5 0 1 1-4.5 4.5A4.5 4.5 0 0 1 16 8ZM8.007 24.93A4.996 4.996 0 0 1 13 20h6a4.996 4.996 0 0 1 4.993 4.93a11.94 11.94 0 0 1-15.986 0Z" />
                                </svg>
                                <div class="flex-1 min-w-0">
                                    <p class="text-sm font-medium text-blue-500 truncate">
                                        @${res[i].fields.username}
                                    </p>
                                    <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                                        ${date}
                                    </p>
                                </div>
                                <div class="inline-flex items-center text-base gap-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 48 48">
                                        <mask id="svgIDa"><path fill="#fff" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M15 8C8.925 8 4 12.925 4 19c0 11 13 21 20 23.326C31 40 44 30 44 19c0-6.075-4.925-11-11-11c-3.72 0-7.01 1.847-9 4.674A10.987 10.987 0 0 0 15 8Z"/>
                                        </mask><path fill="#ff1212" d="M0 0h48v48H0z" mask="url(#svgIDa)"/>
                                    </svg>
                                    <h2 class="font-semibold text-white">${res[i].fields.likes.length}</h2>
                                </div>
                            </div>
                            <h5 class="my-2 text-2xl font-bold tracking-tight text-white">
                                ${res[i].fields.title}
                            </h5>
                            <p class=" text-gray-400">
                                ${res[i].fields.description}
                            </p>
                        </div>
                    </a>`
                );
            }
        }
    )
}

function onlySpaces(str) {
    return str.trim().length === 0;
}

function createPostTech() {
    const getTitle = $('#post-tech-title').val();
    const getDescription = $('#post-tech-description').val();
    console.log(!onlySpaces(getTitle) && !onlySpaces(getDescription));
    if (!onlySpaces(getTitle) && !onlySpaces(getDescription)) {
        $.post(
            {
                url: 'add-post-tech/',
                data: {
                    'title': $('#post-tech-title').val(),
                    'description': $('#post-tech-description').val()
                },
                success: getAllPost
            }
        )
        modal.classList.toggle('hidden');
    }
}
$('#button-submit-post-tech').attr(
    'onclick',
    `createPostTech()`
)

getAllPost();