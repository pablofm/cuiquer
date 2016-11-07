from django.test import TestCase
from django.core.urlresolvers import reverse
from profesionales.models import Servicio
from profesionales.models import Profesional
from perfiles.models import Usuario


class AltaProfesionalGETTest(TestCase):
    def setUp(self):
        url = reverse('alta-profesional')
        self.response = self.client.get(url)

    def test_devuelve_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_llama_plantilla_apropiada(self):
        self.assertTemplateUsed(self.response, 'profesionales/profesional-form.html')


class AltaProfesionalPostTest(TestCase):
    def setUp(self):
        self.servicio = Servicio.objects.first()

        self.data = {
            'servicios': [self.servicio.pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'licencia': True,
            'origen': 1,
        }

    def test_creacion_correcta(self):
        self.client.post(reverse('alta-profesional'), self.data)
        self.assertEqual(1, Usuario.objects.count())
        self.assertEqual(1, Profesional.objects.count())

    def test_creacion_correcta_lleva_a_pagina_de_gracias(self):
        response = self.client.post(reverse('alta-profesional'), self.data)
        self.assertTemplateUsed(response, 'profesionales/alta-profesional-finalizada.html')

    def test_creacion_incorrecta(self):
        self.data['servicios'] = []
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

    def test_los_servicios_que_selecciono_se_guardan(self):
        self.client.post(reverse('alta-profesional'), self.data)
        profesional = Profesional.objects.first()
        self.assertTrue(self.servicio in profesional.servicios.all())


class ActualizarProfesionalGetTest(TestCase):
    def setUp(self):
        self.codigo = '3d996006-39ce-400f-9843-2060377319d0'
        self.servicio = Servicio.objects.first()
        self.data = {
            'servicios': [self.servicio.pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'licencia': True,
            'origen': 1,
        }
        self.client.post(reverse('alta-profesional'), self.data)
        profesional = Profesional.objects.first()
        profesional.codigo_actualizacion = self.codigo
        profesional.save()

    def test_devuelve_el_estado_correcto(self):
        url = reverse('actualizar-profesional', kwargs={'codigo_actualizacion': self.codigo})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_devuelve_404_si_el_perfil_no_existe(self):
        codigo = '4d996006-39ce-400f-9843-2060377319d0'
        url = reverse('actualizar-profesional', kwargs={'codigo_actualizacion': codigo})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_devuelve_404_si_paso_algo_que_no_sea_uuid(self):
        codigo = 'mekemeke'
        url = reverse('actualizar-profesional', kwargs={'codigo_actualizacion': codigo})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
