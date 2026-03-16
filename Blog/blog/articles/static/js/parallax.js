$(document).ready(function () {

    let yPosition;
    let scrolled = 0;
    const $parallaxElements = $('.icons-for-parallax img');
    const $logo = $('.logo');

    $(window).scroll(function () {

        scrolled = $(window).scrollTop();

        for (let i = 0; i < $parallaxElements.length; i++) {
            yPosition = (scrolled * 0.15 * (i + 1));
            $parallaxElements.eq(i).css({top: yPosition});
            const logoPosition = 10 + scrolled * 0.25;
            $logo.css({top: logoPosition});
        }

    });

});
