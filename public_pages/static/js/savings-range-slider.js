/* @author: Michelle Mark */

var sellers_info = (function () {
    var savings_slider = $("#savings-slider");
    var current_home_value = $("#current-home-value");
    var money_saved_value = $("#money-saved-value");

    function format_thousands(value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    return {
        setup_page: function () {
            savings_slider.on("input change", function() {
                var current_value = savings_slider.val();
                var current_savings = "$" + format_thousands(current_value * .02);
                current_value = "$" + format_thousands(current_value);
                current_home_value.html(current_value);
                money_saved_value.html(current_savings);
            });
            savings_slider.trigger("change");
        }
    }

})(sellers_info || {});

$(document).ready(function () {
    sellers_info.setup_page();
});


