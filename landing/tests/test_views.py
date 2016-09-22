from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexTest(TestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'landing/index.html')


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
