from django.test import TestCase
from django.core.urlresolvers import reverse
from landing.models import Contacto, Suscripcion


class IndexTest(TestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/index.html')


class ComoFuncionaTest(TestCase):
    def setUp(self):
        url = reverse('como-funciona')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/profesionales-como.html')


# Secundarias
class SaludYBienestarTest(TestCase):
    def setUp(self):
        url = reverse('salud-y-bienestar')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/salud-y-bienestar.html')


class CuidadoDePersonasTest(TestCase):
    def setUp(self):
        url = reverse('cuidado-de-personas')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/cuidado-de-personas.html')


class ClasesParticularesTest(TestCase):
    def setUp(self):
        url = reverse('clases-particulares')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/clases-particulares.html')


class MonitorDeDeportesTest(TestCase):
    def setUp(self):
        url = reverse('monitor-de-deportes')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/monitor-de-deportes.html')


class HogarYLimpiezaTest(TestCase):
    def setUp(self):
        url = reverse('hogar-y-limpieza')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/hogar-y-limpieza.html')


class ServiciosInformaticosTest(TestCase):
    def setUp(self):
        url = reverse('servicios-informaticos')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/servicios-informaticos.html')


class ReparacionesYReformasTest(TestCase):
    def setUp(self):
        url = reverse('reparaciones-y-reformas')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/reparaciones-y-reformas.html')


class TodosNuestrosServiciosTest(TestCase):
    def setUp(self):
        url = reverse('todos-nuestros-servicios')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/secundarias/todos-nuestros-servicios.html')


# Legal
class CookiesTest(TestCase):
    def setUp(self):
        url = reverse('cookies')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/legal/cookies.html')


class CondicionesUsoTest(TestCase):
    def setUp(self):
        url = reverse('condiciones-uso')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/legal/condiciones-uso.html')


class CondicionesPrivacidadTest(TestCase):
    def setUp(self):
        url = reverse('condiciones-privacidad')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/legal/condiciones-privacidad.html')


class ContactoGETTest(TestCase):
    def setUp(self):
        url = reverse('contacto')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/contacto.html')


class ContactoPostTest(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'Nombre',
            'email': 'correo@correo.com',
            'asunto': 'Esto es un asunto',
            'mensaje': 'Esto es un mensaje'
        }

    def test_contacto_correcto(self):
        self.client.post(reverse('contacto'), self.data)
        self.assertEqual(1, Contacto.objects.count())

    def test_contacto_incorrecto(self):
        self.data['nombre'] = ''
        self.client.post(reverse('contacto'), self.data)
        self.assertEqual(0, Contacto.objects.count())

    def test_contacto_incorrecto_2(self):
        self.data['email'] = ''
        self.client.post(reverse('contacto'), self.data)
        self.assertEqual(0, Contacto.objects.count())

    def test_contacto_incorrecto_3(self):
        self.data['asunto'] = ''
        self.client.post(reverse('contacto'), self.data)
        self.assertEqual(0, Contacto.objects.count())

    def test_contacto_incorrecto_4(self):
        self.data['mensaje'] = ''
        self.client.post(reverse('contacto'), self.data)
        self.assertEqual(0, Contacto.objects.count())


class SuscripcionPOSTTest(TestCase):
    def test_sin_datos_no_hay_alta(self):
        self.client.post(reverse('suscripcion'), {})
        self.assertEqual(0, Suscripcion.objects.count())

    def test_sin_correo_no_hay_alta(self):
        self.client.post(reverse('suscripcion'), {'email': None})
        self.assertEqual(0, Suscripcion.objects.count())

    def test_sin_correo_no_hay_alta_2(self):
        self.client.post(reverse('suscripcion'), {'email': ''})
        self.assertEqual(0, Suscripcion.objects.count())

    def test_sin_correo_no_hay_alta_3(self):
        self.client.post(reverse('suscripcion'), {'email': '@correo.com'})
        self.assertEqual(0, Suscripcion.objects.count())

    def test_alta_correcta(self):
        self.client.post(reverse('suscripcion'), {'email': 'correo@correo.com'})
        self.assertEqual(1, Suscripcion.objects.count())
