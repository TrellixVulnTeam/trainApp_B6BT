
//For hover on log
$( document ).ready(function() {
        $('#blackScreenContCont').fadeIn(1);
        var left = $('#logoImg').offset().left;
        var top = $('#logoImg').offset().top;
        var move_up = ($('#centImage').offset().top - top)+30;
        var move_left = ($('#centImage').offset().left - left)+80;
        console.log(move_left);
        setTimeout(function(){
            $('#imgCont').animate({left:'-='+move_left, top:'-='+move_up},1);
            $('#centImage').animate({width:'160px',height:'60px'},1);
         },1);
         setTimeout(function(){
            $('#blackScreen').css('background-color','transparent');
            $('#blackScreen').css('background-color','transparent');
            $('#blackScreen').hide();
         },1);
});



/*

//For hover on log
$( document ).ready(function() {
        $('#blackScreenContCont').fadeIn(3000);
        var left = $('#logoImg').offset().left;
        var top = $('#logoImg').offset().top;
        var move_up = ($('#centImage').offset().top - top)+30;
        var move_left = ($('#centImage').offset().left - left)+80;
        console.log(move_left);
        setTimeout(function(){
            $('#imgCont').animate({left:'-='+move_left, top:'-='+move_up},1000);
            $('#centImage').animate({width:'160px',height:'60px'},1000);
         },5000);
         setTimeout(function(){
            $('#blackScreen').css('background-color','transparent');
            $('#blackScreen').css('background-color','transparent');
            $('#blackScreen').hide();
         },6500);
});
*/
