$(document).ready( function() {

    $("#go1").click(function() {
        $('html, body').animate({
            scrollTop: $("#um").offset().top
        }, 500);
    });

     $("#go2").click(function() {
        $('html, body').animate({
            scrollTop: $("#dois").offset().top
        }, 500);
    });

     $("#go3").click(function() {
        $('html, body').animate({
            scrollTop: $("#tres").offset().top
        }, 500);
    });

});