let slideIndex = 0;
showSlides(slideIndex);
  
// Function to change slides
function changeSlide(n) {
	showSlides(slideIndex += n);
}

// Function to show slides based on the current index
function showSlides(n) {
	const slides = document.getElementsByClassName("slide");
	
	// Reset the slide index if it exceeds the number of slides
	if (n >= slides.length) {
		slideIndex = 0; // Loop back to the first slide
	}
	if (n < 0) {
		slideIndex = slides.length - 1; // Go to the last slide
	}

	// Hide all slides
	for (let i = 0; i < slides.length; i++) {
		slides[i].style.display = "none"; 
	}

	// Show the current slide
	slides[slideIndex].style.display = "block";  
}