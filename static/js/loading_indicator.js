/**
 * Created by Kevin on 8/2/2014.
 */

var over = null;
function loading_indicator_trigger() {
    // add the overlay with loading image to the page
    if(over == null) {
        over = '<div id="overlay">' +
                '<img id="loading" src="https://s3.amazonaws.com/Vis_Pics/pics/loading_01.gif">' +
                '</div>';
        $(over).appendTo('loadhere');
    }
    else{
        $('#overlay').remove();
        over = null;
    }
}


