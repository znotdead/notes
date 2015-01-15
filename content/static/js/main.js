$(document).ready(function(){
    $('table').addClass('table');
    $('table').addClass('table-striped');
    $('table').tablesorter();
    // for bootstrap css (display borders)
    $($('div.container')[1]).find('img').addClass('img-thumbnail');

    // hover
    $($('div.container')[1]).find('img').addClass('thumbnail');
    $('.thumbnail').hover(function(){
        $(this).addClass('fullsizeimage');
        $(this).removeClass('thumbnail');
    },
    function(){
        $(this).addClass('thumbnail');
        $(this).removeClass('fullsizeimage');
    });
});
