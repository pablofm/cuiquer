from django.test import TestCase
from django.core.urlresolvers import reverse
from clientes.models import Servicio
from clientes.models import Cliente
from perfiles.models import Usuario


class AltaClienteGETTest(TestCase):
    def setUp(self):
        url = reverse('alta-cliente')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'clientes/cliente-form.html')


class AltaClientePostTest(TestCase):
    def setUp(self):
        self.data = {
            'servicio': Servicio.objects.first().pk,
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'licencia': True,
        }

    def test_creacion_correcta(self):
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Cliente.objects.count())

    def test_creacion_incorrecta(self):
        self.data['servicio'] = []
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Cliente.objects.count())

    def test_creacion_incorrecta_2(self):
        self.data['nombre'] = ''
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Cliente.objects.count())

    def test_creacion_incorrecta_3(self):
        self.data['email'] = ''
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Cliente.objects.count())

    def test_creacion_incorrecta_4(self):
        self.data['telefono'] = ''
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Cliente.objects.count())

    def test_creacion_incorrecta_6(self):
        self.data['licencia'] = ''
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Cliente.objects.count())

    def test_repetir_email_no_crea_usuarios_ni_Clientees(self):
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Cliente.objects.count())
        self.client.post(reverse('alta-cliente'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Cliente.objects.count())
