// grab everything we need
const btn = document.querySelector(".mobile-menu-button");
const close = document.querySelector(".close");
const contentHome = document.querySelector(".content-home");
const sidebar = document.querySelector(".sidebar");

// add our event listener for the click
[btn,close].map(el => {
    el.addEventListener("click", () => {
        sidebar.classList.toggle("-translate-x-full");
    });
})

contentHome.addEventListener("click", () => {
    console.log('coucou');
    sidebar.classList.add("-translate-x-full");
});