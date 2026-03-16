$(document).ready(function () {
    const logo = $('.logo');
    logo.hover(
        function () {
            const currentWidth = $(this).width();
            const newWidth = currentWidth + 20;
            $(this).stop().animate({
                width: newWidth
            }, 300);
        },
        function () {
            const currentWidth = $(this).width();
            const newWidth = currentWidth - 20;
            $(this).stop().animate({
                width: newWidth
            }, 300);
        }
    );
});
