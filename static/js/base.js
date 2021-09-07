// code to toggle dropdown for mobile nav
const navToggler = document.querySelector(".navbar-toggler");
const mobileNav = document.querySelector(".mobile_nav_menu");
const navTogglerClose = document.querySelector(".navbar-toggler-close");

function openMobileNav() {
    mobileNav.style.display = "block";
    navToggler.style.display = "none";
    navTogglerClose.style.display = "block";
    $("body").toggleClass("fixedPosition");
}

function closeMobileNav() {
    mobileNav.style.display = "none";
    navToggler.style.display = "block";
    navTogglerClose.style.display = "none";
    $("body").toggleClass("staticPosition");
}

navToggler.addEventListener("click", openMobileNav);
navTogglerClose.addEventListener("click", closeMobileNav);
