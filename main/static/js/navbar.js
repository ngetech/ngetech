const hamburger = document.querySelector('#hamburger');
const menu = document.querySelector('.menu');
if (hamburger != null) {
    hamburger.addEventListener(
        'click',
        function () {
            menu.classList.toggle('hidden');
        }
    )
}

const avatar = document.querySelector('#avatarButton');
if (avatar != null) {
    const avatarMenu = document.querySelector('#userDropdown');
    avatar.addEventListener(
        'click',
        function () {
            avatarMenu.classList.toggle('hidden');
        }
    )
}