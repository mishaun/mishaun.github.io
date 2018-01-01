

var squares = document.querySelectorAll(".squares"); //variable holding the color square divs 
var message = document.querySelector("#tryagain");
var resetButton = document.querySelector("#resetButton");
var hardButton = document.querySelector("#hard");
var easyButton = document.querySelector("#easy");
var isEasy = false;

var numberSquares = 6;
var colors = randomColors(numberSquares);
var colorAnswer = colors[randomNumber(numberSquares)]; //selecting correct color by generating random number as the index of colors array
var displayColor = document.querySelector("#guessColor"); //holding value in heading with color to guess
displayColor.textContent = colorAnswer;


//assiging colors to squares

for(var i = 0; i<numberSquares; i++){

    squares[i].style.backgroundColor = colors[i];
    squares[i].addEventListener("click", checker)
};

hardButton.addEventListener("click",function(){
    hardButton.classList.add("difficultySelect")
    easyButton.classList.remove("difficultySelect")
    isEasy = false;
    reset();
})

easyButton.addEventListener("click",function(){
    hardButton.classList.remove("difficultySelect")
    easyButton.classList.add("difficultySelect")
    isEasy = true;
    reset();
})

resetButton.addEventListener("click",reset);


//function for click event listenor on squares to determine if right color was picked
function checker(){

    if(this.style.backgroundColor == colorAnswer){
        message.textContent= "Correct!!!";
        changeColor();
        resetButton.textContent = "Play Again?"
    } else{
        this.style.backgroundColor = "black";
        message.textContent = "Try Again!";
    }
}

//function to change color of square divs when correct color is chosen and change heading color
function changeColor(){
    for(var i = 0; i<numberSquares; i++){
        squares[i].style.backgroundColor = colorAnswer;
    }

    document.querySelector("#heading").style.backgroundColor = colorAnswer; //changes heading color to correct color
}

//function to create random number to pick color

function randomNumber(num){
    return Math.floor(Math.random()*num)
}


//function to create array of random colors

function randomColors(num){
    var arr = [];
        for(var i = 0; i<num; i++){
            var R = Math.floor(Math.random()*256);
            var G = Math.floor(Math.random()*256);
            var B = Math.floor(Math.random()*256);

            arr[i] = "rgb(" + R +", " + G + ", " + B + ")"
        }

        return arr;
    }
   
function reset(){
    if(isEasy){
        numberSquares = 3;
        for(var i = numberSquares; i<squares.length; i++){
            squares[i].style.display = "none";
        }
    } else{
        numberSquares = 6;
    }

    colors = randomColors(numberSquares); //regenerates numberSquares colors in colors array
    colorAnswer = colors[randomNumber(numberSquares)]; //resets the color to guess by assigning random index
    displayColor.textContent = colorAnswer; //resets rgb in heading to the new color to guess
    document.querySelector("#heading").style.backgroundColor = "ghostwhite" //resets heading color back to default

    //assigning new random colors to all squares again
    for(var i = 0; i<numberSquares; i++){

        squares[i].style.backgroundColor = colors[i];
        squares[i].addEventListener("click", checker)
        squares[i].style.display = "block";
    };

    message.textContent = ""; //resets the message content of try again/correct to nothing
}
