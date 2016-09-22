from django.test import TestCase
from landing.forms import ContactoForm


class ContactoFormTest(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'Nombre',
            'email': 'correo@correo.com',
            'asunto': 'Esto es un asunto',
            'mensaje': 'Esto es un mensaje'
        }

    def test_formulario_no_vacio(self):
        form = ContactoForm({})
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio(self):
        self.data['nombre'] = None
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio_2(self):
        self.data['nombre'] = ''
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio(self):
        self.data['email'] = None
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio_2(self):
        self.data['email'] = ''
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_asunto_no_vacio(self):
        self.data['asunto'] = None
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_asunto_no_vacio_2(self):
        self.data['asunto'] = ''
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_mensaje_no_vacio(self):
        self.data['mensaje'] = None
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_mensaje_no_vacio_2(self):
        self.data['mensaje'] = ''
        form = ContactoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_formulario_completo(self):
        form = ContactoForm(self.data)
        self.assertTrue(form.is_valid())
