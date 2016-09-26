from django.test import TestCase
from profesionales.forms import ProfesionalForm
from profesionales.models import Servicio


class ProfesionalFormTest(TestCase):
    def setUp(self):
        self.data = {
            'servicio': [Servicio.objects.first().pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'licencia': True,
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
        self.data['servicio'] = None
        form = ProfesionalForm(self.data)
        self.assertFalse(form.is_valid())

    def test_servicio_no_vacio_2(self):
        self.data['servicio'] = ''
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
