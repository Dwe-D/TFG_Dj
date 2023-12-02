const slides = document.querySelectorAll('.slider li');
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

let activeSlideIndex = 0;

// Función para ocultar todas las imágenes excepto la activa
function hideAllSlidesExceptActive() {
    slides.forEach((slide, index) => {
        if (index !== activeSlideIndex) {
            slide.style.display = 'none';
        } else {
            slide.style.display = 'block';
        }
    });
}

// Función para cambiar de imagen
function changeSlide(direction) {
    activeSlideIndex = (activeSlideIndex + direction + slides.length) % slides.length;
    hideAllSlidesExceptActive();
}

// Eventos para los botones
nextButton.addEventListener('click', () => {
    changeSlide(1);
});
prevButton.addEventListener('click', () => {
    changeSlide(-1);
});

// Inicialización
hideAllSlidesExceptActive();
