from django.conf.urls import url
from clientes.views import ClienteCreateView
from clientes.views import ClienteDetailView


urlpatterns = [
    url(r'alta/$', ClienteCreateView.as_view(), name='cliente-create'),
    url(r'(?P<cliente_id>[0-9]+)/$', ClienteDetailView.as_view(), name='cliente-detail'),
]
