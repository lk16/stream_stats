function load_stats() {
    $.ajax({
        url: "/stats",
        success: function(data) {
            $("span").empty();
            let split_data = data["stats"].split(/\r?\n/);
            console.log(split_data);
            for (var i = 0; i < split_data.length; i++) {
                let line = split_data[i];
                $("span").append(line);
                $("span").append("<br/>");
            }
        },
        dataType: "json",
    });
}

var interval = setInterval(load_stats, 1000);
