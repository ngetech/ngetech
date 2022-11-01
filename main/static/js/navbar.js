const hamburger = document.querySelector('#hamburger');
const menu = document.querySelector('.menu');
hamburger.addEventListener(
    'click',
    function () {
        menu.classList.toggle('hidden');
    }
)

const avatar = document.querySelector('#avatarButton');
const avatarMenu = document.querySelector('#userDropdown');
avatar.addEventListener(
    'click',
    function () {
        avatarMenu.classList.toggle('hidden');
    }
)