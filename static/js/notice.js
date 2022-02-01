var scrollTime = 3000;

var timer = function(){
  $('#list').stop().animate({scrollTop:60},400,'swing',function(){
    $(this).scrollTop(0).find('a:last').after($('a:first', this));
  });
}

var ticker = setInterval(timer , scrollTime);

$('#list').hover(function(event){
	clearInterval(ticker);
}, function(event){
	ticker = setInterval(timer, scrollTime);
});