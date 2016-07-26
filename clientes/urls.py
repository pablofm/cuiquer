from django.conf.urls import url
from clientes.views import ClienteCreate
from clientes.views import ClienteCreateFinished
# from clientes.views import ClienteUpdate


urlpatterns = [
    url(r'alta/$', ClienteCreate.as_view(), name='alta_cliente'),
    url(r'alta_finalizada/$', ClienteCreateFinished.as_view(), name='alta_cliente_finalizada'),
    # url(r'(?P<pk>[0-9]+)/$', ClienteUpdate.as_view(), name='actualizar_cliente'),
]
