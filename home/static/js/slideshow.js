var AutomaticslideIndex=0;
AutomaticshowSlide();
var slideIndex=1;
showSlide(slideIndex);

function plusSlides(n){
    showSlide(slideIndex += n);
}
function currentSlide(n){
    showSlide(slideIndex = n);
}
function showSlide(n){
    var i;
    var slides=document.getElementsByClassName("mySlides");
    var dots=document.getElementsByClassName("dots");
    if(n>slides.length){slideIndex= 1}
    if(n<1){slideIndex = slides.length}
    for(i=0;i<slides.length;i++){
        slides[i].style.display="none";
    }
    for(i=0;i<dots.length;i++){
        dots[i].className=dots[i].className.replace("active","");
        
    }
    slides[slideIndex-1].style.display="block";
    dots[slideIndex-1].className+="active";
    
}


function AutomaticshowSlide(){
    var i=0;
    var slides=document.getElementsByClassName("mySlides");
    for(i=0;i<slides.length;i++){
        slides[i].style.display="none";
    }
    AutomaticslideIndex++;
    if(AutomaticslideIndex>slides.length){
        AutomaticslideIndex=1;
    }
    slides[AutomaticslideIndex - 1].style.display="block";
    setTimeout(AutomaticshowSlide,2000);
}