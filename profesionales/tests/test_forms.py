from django.test import TestCase
from profesionales.forms import ProfesionalForm, ProfesionalExtraForm
from profesionales.models import Servicio, Profesional


class ProfesionalFormTest(TestCase):
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

    def test_formulario_no_vacio(self):
        form = ProfesionalForm({})
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio(self):
        self.data['nombre'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio_2(self):
        self.data['nombre'] = ''
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio(self):
        self.data['email'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio_2(self):
        self.data['email'] = ''
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_servicio_no_vacio(self):
        self.data['servicios'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_servicio_no_vacio_2(self):
        self.data['servicios'] = ''
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_telefono_no_vacio(self):
        self.data['telefono'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_telefono_no_vacio_2(self):
        self.data['telefono'] = ''
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_codigo_postal_no_vacio(self):
        self.data['codigo_postal'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_codigo_postal_no_vacio_2(self):
        self.data['codigo_postal'] = ''
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_es_obligatorio_aceptar_la_licencia(self):
        self.data['licencia'] = False
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_no_se_puede_repetir_email(self):
        from perfiles.models import Usuario
        Usuario.objects.create(email='correo@correo.com')
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_formulario_completo(self):
        form = ProfesionalForm(self.data)
        self.assertTrue(form.is_valid())


# class ProfesionalExtraFormTest(TestCase):
#     def setUp(self):
#         self.servicio = Servicio.objects.first()
#         self.data = {
#             'servicios': [self.servicio.pk],
#             'nombre': 'Yo me llamo Ralph',
#             'email': 'correo@correo.com',
#             'telefono': '666666666',
#             'codigo_postal': '41001',
#             'licencia': True,
#             'origen': 1,
#         }

#         self.servicio = Servicio.objects.first()
#         self.codigo = '3d996006-39ce-400f-9843-2060377319d0'
#         self.profesional = Profesional.objects.create(
#             servicios=[self.servicio.pk],
#             nombre='Yo me llamo Ralph',
#             email='correo@correo.com',
#             telefono='666666666',
#             codigo_postal='41001',
#             licencia=True,
#             origen=1,
#             codigo_actualizacion=self.codigo,
#         )

#     def test_formulario_no_vacio(self):
#         form = ProfesionalExtraForm({})
#         self.assertFalse(form.is_valid())

#     def test_nombre_no_vacio(self):
#         self.data['nombre'] = None
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_nombre_no_vacio_2(self):
#         self.data['nombre'] = ''
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_email_no_vacio(self):
#         self.data['email'] = None
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_email_no_vacio_2(self):
#         self.data['email'] = ''
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_servicio_no_vacio(self):
#         self.data['servicios'] = None
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_servicio_no_vacio_2(self):
#         self.data['servicios'] = ''
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_telefono_no_vacio(self):
#         self.data['telefono'] = None
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_telefono_no_vacio_2(self):
#         self.data['telefono'] = ''
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_codigo_postal_no_vacio(self):
#         self.data['codigo_postal'] = None
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_codigo_postal_no_vacio_2(self):
#         self.data['codigo_postal'] = ''
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_es_obligatorio_aceptar_la_licencia(self):
#         self.data['licencia'] = False
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_no_se_puede_repetir_email(self):
#         from perfiles.models import Usuario
#         Usuario.objects.create(email='correo@correo.com')
#         form = ProfesionalExtraForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_formulario_completo(self):
#         form = ProfesionalExtraForm(self.data)
#         self.assertTrue(form.is_valid())
