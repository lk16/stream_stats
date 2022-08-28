$(document).ready(function(){
    $.ajax({
        url: "/stats",
        success: function(data) {
            $("textarea").val(data.stats);
        },
        dataType: "json",
    });


    $("textarea").on("change keyup paste", function() {
        var currentVal = $(this).val();

        $.ajax({
            type: 'PATCH',
            url: "/stats",
            data: JSON.stringify({"stats": currentVal}),
        });


    });
});



