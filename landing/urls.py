from django.conf.urls import url
from landing import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^como-funciona$', views.ComoFunciona.as_view(), name='como-funciona'),

    url(r'^contacto$', views.contacto, name='contacto'),
    url(r'^suscripcion$', views.suscripcion, name='suscripcion'),

    # Secundarias
    url(r'^salud-y-bienestar$', views.SaludYBienestarView.as_view(), name='salud-y-bienestar'),
    url(r'^cuidado-de-personas$', views.CuidadoDePersonasView.as_view(), name='cuidado-de-personas'),
    url(r'^clases-particulares$', views.ClasesParticulares.as_view(), name='clases-particulares'),
    url(r'^monitor-de-deportes$', views.MonitorDeDeportesView.as_view(), name='monitor-de-deportes'),
    url(r'^hogar-y-limpieza$', views.HogarYLimpiezaView.as_view(), name='hogar-y-limpieza'),
    url(r'^servicios-informaticos$', views.ServiciosInformaticosView.as_view(), name='servicios-informaticos'),
    url(r'^reparaciones-y-reformas$', views.ReparacionesYReformasView.as_view(), name='reparaciones-y-reformas'),
    url(r'^todos-nuestros-servicios$', views.TodosNuestrosServiciosView.as_view(), name='todos-nuestros-servicios'),
    # Legal
    url(r'^cookies$', views.CookiesView.as_view(), name='cookies'),
    url(r'^condiciones-uso$', views.CondicionesUsoView.as_view(), name='condiciones-uso'),
    url(r'^condiciones-privacidad$', views.CondicionesPrivacidadView.as_view(), name='condiciones-privacidad'),
]
