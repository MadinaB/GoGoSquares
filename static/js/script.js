
var squares= document.getElementsByClassName("square");

function setRandomAnimationDuration(){
  for(var s = 0; s < squares.length; s++){

    squares[s].style.animationDuration =  Math.floor(Math.random() * 10 + 1) + "s";
  
}
  }

setRandomAnimationDuration();
