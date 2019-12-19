//导航栏代码
$('#l2').hover(function () {
    $('#sub_nav').stop(true, true).show(100)
}, function () {
    $('#sub_nav').stop(true, true).hide(100)
});
//大图切换代码
var arrImg = [{
    'url': '/static/images/9/fm.jpg',
    'tip': '第一张图片'
}, {
    'url': '/static/images/7/fm.jpg',
    'tip': '第二张图片'
}, {
    'url': '/static/images/6/fm.jpg',
    'tip': '第三张图片'
}];
var i = 0;
$('#imgleft').on('click', function () {
    $('.lleft img').fadeOut(1000, function () {
        i++;
        if (i == 0) {
            i = arrImg.length - 1
        } else {
            i = 0;
        }
        $(this).attr('src', arrImg[i].url).fadeIn(1000);
        $('.lleft p').html(arrImg[i].tip)
    })
});
$('#imgright').on('click', function () {

});
window.scrollReveal = new scrollReveal({
    reset: true
});

function getFocus($obj) {
//找到所有添加了focus类别样式的元素
    $obj.each(function (i, e) {
//将e对象转换成jq对象
        $(e).removeClass('focus')
    });
//添加需要获取焦点的样式
    $obj.addClass('focus');
}