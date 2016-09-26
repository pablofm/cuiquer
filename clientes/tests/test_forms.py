# from django.test import TestCase
# from clientes.forms import ClienteForm


# class ClienteFormTest(TestCase):
#     def setUp(self):
#         self.data = {
#             'servicio': 1,
#             'nombre': 'Yo me llamo Ralph',
#             'email': 'correo@correo.com',
#             'telefono': '666666666'
#         }

#     def test_formulario_no_vacio(self):
#         form = ClienteForm({})
#         self.assertFalse(form.is_valid())

#     def test_nombre_no_vacio(self):
#         self.data['nombre'] = Nonea
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_nombre_no_vacio_2(self):
#         self.data['nombre'] = ''
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_email_no_vacio(self):
#         self.data['email'] = None
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_email_no_vacio_2(self):
#         self.data['email'] = ''
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_servicio_no_vacio(self):
#         self.data['servicio'] = None
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_servicio_no_vacio_2(self):
#         self.data['servicio'] = ''
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_telefono_no_vacio(self):
#         self.data['telefono'] = None
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_telefono_no_vacio_2(self):
#         self.data['telefono'] = ''
#         form = ClienteForm(self.data)
#         self.assertFalse(form.is_valid())

#     def test_formulario_completo(self):
#         form = ClienteForm(self.data)
#         self.assertTrue(form.is_valid())
