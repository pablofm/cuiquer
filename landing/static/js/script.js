$(document).ready(function($){
    menuStickyColor();
    cambiarLugarLogoFooter();
    $(window).resize(function(){
        cambiarLugarLogoFooter();
    });
});

function cambiarLugarLogoFooter(){
    if($(window).width()<=768){
        $('#footerLogo').addClass('fAbajo').insertAfter(".fooProfesionales");
    }else{
        if($('#footerLogo').hasClass('fAbajo')){
            $('#footerLogo').insertBefore(".fooEmpresa");
        }
    }
}

function menuStickyColor(){
  var altura = 150;

  $(window).on('scroll', function(){
    if ( $(window).scrollTop() > altura ){
      $('.navbar').addClass('menu-fixed');
    } else {
      $('.navbar').removeClass('menu-fixed');
    }
  });
}