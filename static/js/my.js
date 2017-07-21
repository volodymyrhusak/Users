
$('#coursesB').on("click", function(evt){
obj = $('#coursesD')
if (obj.hasClass('hide')){
    obj.removeClass('hide')
} else {
    if ($("#cour ul li").length <= 5){
        $('#cour').removeClass('hide')
        courseName = $('#selectCourse option:selected').text()
        $("#cour ul").append('<li>'+courseName+'<a href="#" id="li_course"><i class="glyphicon glyphicon-remove-circle IconBlack"></i></a></li>')
        $('#selectCourse option:selected').remove();
        $('#cour ul li').on("click", function(evt){
        evt.currentTarget.remove();
        });
    }  else {
    obj.addClass('hide');
    }
//console.log($("#cour ul"))
}

});

