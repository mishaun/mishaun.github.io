$("ul").on("click", "li",function(){
    $(this).toggleClass("strike");
});

$("ul").on("click","span", function(){
    $(this).parent().fadeOut(350, function(){
        $(this).remove();
    });
})

$("input").on("keypress",function(event){

    if(event.which===13){
        var newTodo= $(this).val();
        $("ul").append("<li><span><i class=\"fa fa-trash\"></i></span>" + newTodo + "</li");
        $(this).val("");
    }
})

var add = $(".fa-plus");

add.on("click", function(){

    $("input").toggleClass("hidden");
})