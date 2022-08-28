function test() {
    $.ajax({
        url: "/stats",
        success: function(data) {
            $("span").text(data.stats);
        },
        dataType: "json",
    });
}

var interval = setInterval(test, 1000);
