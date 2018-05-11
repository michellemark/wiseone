/**
 * @copyright Copyright Wise One Realty, 2018
 *
 * Common to all pages
 */

let wise_one_js = (function() {

    return {
        setup_page: function () {
            // Give site wide top navigation items with children arrows
            $("#main_navigation li.child").has("ul").children("a").append(
                "<i class='material-icons md-inactive align-bottom'>arrow_drop_down</i>");
        }
    };

})();

$(document).ready(function () {
    wise_one_js.setup_page();
});
