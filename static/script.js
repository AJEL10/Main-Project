var scene = document.getElementById('scene');
var parallaxInstance = new Parallax(scene);

var showContent = function() {
  $('.hide-content').addClass('show-content');
}

var hideContent = function() {
  $('.hide-content').removeClass('show-content');
}

var triggerIntro = function() {
  window.setTimeout(function(){$('.layer img').addClass('pan-out');},1);
  window.setTimeout(function(){showContent();},1200);
}

triggerIntro();