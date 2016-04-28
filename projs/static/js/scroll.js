$(document).ready( function() {

    $("#go1").click(function() {
        $('html, body').animate({
            scrollTop: $("#1").offset().top
        }, 500);
    });

     $("#go2").click(function() {
        $('html, body').animate({
            scrollTop: $("#2").offset().top
        }, 500);
    });

     $("#go3").click(function() {
        $('html, body').animate({
            scrollTop: $("#3").offset().top
        }, 500);
    });

});