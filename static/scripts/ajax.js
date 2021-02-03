$(document).ready(function(){
    $("#but").click(function(){
        $(this).animate({'left':'200px'}, function(){
            $(this).animate({'top':"200px"}, function(){
                alert('Animation ended')
            });
        });
    });
    $('#search_bar').keyup(function(){
        var a;
        a = $(this).val();
        $.get('/search/', {search_bar:a},function(data){
            $('#search_list').html(data);
        });
    });
});