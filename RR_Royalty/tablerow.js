var states = document.querySelectorAll("#states div");
var acres = document.querySelectorAll("#acres div");


for(var i =1; i<states.length; i++){
    addHover(i);
}


function addHover(num){
    states[num].addEventListener("mouseover",function(){
        this.classList.add("highlight"); 
        acres[num].classList.add("highlight");
    })
    
    states[num].addEventListener("mouseout",function(){
        this.classList.remove("highlight");
        acres[num].classList.remove("highlight");
    })

    acres[num].addEventListener("mouseover",function(){
        this.classList.add("highlight"); 
        states[num].classList.add("highlight");
    })
    
    acres[num].addEventListener("mouseout",function(){
        this.classList.remove("highlight");
        states[num].classList.remove("highlight");
    })
}


//scratch notes 


/////forced highlight to work by manually entering
// states[1].addEventListener("mouseover",function(){
//     this.classList.add("highlight"); 
//     acres[1].classList.add("highlight");
// })

// states[1].addEventListener("mouseout",function(){
//     this.classList.remove("highlight");
//     acres[1].classList.remove("highlight");
// })


/////would not work because index i was out of bounds on acres when event was triggered 
// for(var i =1; i<states.length; i++){
//     states[i].addEventListener("mouseover",function(){
//         this.classList.add("highlight"); 
//         acres[i].classList.add("highlight");

//     })

//     states[i].addEventListener("mouseout",function(){
//         this.classList.remove("highlight");
//     })

// }

