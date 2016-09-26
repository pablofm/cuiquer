from django.test import TestCase
from django.core.urlresolvers import reverse
from profesionales.models import Servicio
from profesionales.models import Profesional
from perfiles.models import Usuario


class ContactoGETTest(TestCase):
    def setUp(self):
        url = reverse('alta-profesional')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'profesionales/profesional-form.html')


class ContactoPostTest(TestCase):
    def setUp(self):
        self.data = {
            'servicio': [Servicio.objects.first().pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'licencia': True,
        }

    def test_creacion_correcta(self):
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Profesional.objects.count())

    def test_creacion_incorrecta(self):
        self.data['servicio'] = []
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_creacion_incorrecta_2(self):
        self.data['nombre'] = ''
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_creacion_incorrecta_3(self):
        self.data['email'] = ''
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_creacion_incorrecta_4(self):
        self.data['telefono'] = ''
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_creacion_incorrecta_5(self):
        self.data['codigo_postal'] = ''
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_creacion_incorrecta_6(self):
        self.data['licencia'] = ''
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(0, Usuario.objects.count())
        self.assertEqual(0, Profesional.objects.count())

    def test_repetir_email_no_crea_usuarios_ni_profesionales(self):
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Profesional.objects.count())
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Profesional.objects.count())