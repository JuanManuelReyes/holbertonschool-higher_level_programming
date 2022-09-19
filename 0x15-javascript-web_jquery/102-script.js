document.addEventListener("DOMContentLoaded", function() {
    $("#btn_translate").click(function(){
        const url = 'https://stefanbohacek.com/hellosalut/?lang=' + $("INPUT#language_code").val();
        $.get(url, function(data){
            $("#hello").text(data.hello)
        })
    })
});