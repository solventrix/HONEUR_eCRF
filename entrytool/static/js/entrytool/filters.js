filters.filter('translate', function(){
  return function(someText){
    return window.gettext(someText);
  }
})