// static/js/home.js

// Tabbed Menu
function openMenu(evt, menuName) {
  var i, x, tablinks;
  x = document.getElementsByClassName("menu");
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
     tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
  }
  document.getElementById(menuName).style.display = "block";
  evt.currentTarget.firstElementChild.className += " w3-red";
}
document.getElementById("myLink").click();


// Add slides to the carousel
var slideIndex = 0;
var slides = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("dot");

showSlides();

function showSlides() {
  var i;
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 4000); // Change image every 4 seconds
}

// Add active class to the current slide
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

//Centra las imagenes y le da estilos al body
document.body.style.display = "flex";
document.body.style.alignItems = "center";
document.body.style.justifyContent = "center";

//Agrega estilos al carrusel y le deja el fondo negro
var carrousel = document.getElementsByClassName("carousel-item");
for(var i = 0; i < carrousel.length; i++){
    carrousel[i].style.display = "flex";
    carrousel[i].style.alignItems = "center";
    carrousel[i].style.justifyContent = "center";
    carrousel[i].style.backgroundColor = "black";
}


