from django.test import TestCase
from profesionales.forms import ProfesionalForm, ProfesionalExtraForm
from profesionales.models import Servicio
from django.core.files.uploadedfile import SimpleUploadedFile


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


class ProfesionalExtraFormTest(TestCase):

    def setUp(self):
        self.codigo = '3d996006-39ce-400f-9843-2060377319d0'
        self.servicio = Servicio.objects.first()
        self.data_profesional = {
            'servicios': [self.servicio.pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'licencia': True,
            'origen': 1,
        }

        self.data_extra = {
            'servicios': [self.servicio.pk],
            'nombre': 'Yo me llamo Ralph',
            'email': 'correo@correo.com',
            'telefono': '666666666',
            'codigo_postal': '41001',
            'metodo_trabajo': 1,
            'fecha_nacimiento': '2016-05-05',
            'precio': 11.05,
        }
        self.file_data = {
            'foto': SimpleUploadedFile(
                name='foo.gif',
                content=b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00')}

        form = ProfesionalForm(self.data_profesional)
        form.is_valid()
        self.profesional = form.save()
        self.profesional.codigo_actualizacion = self.codigo
        self.profesional.save()

    def test_init_sin_profesional_1(self):
        with self.assertRaises(KeyError):
            ProfesionalExtraForm()

    def test_init_sin_profesional_2(self):
        with self.assertRaises(KeyError):
            ProfesionalExtraForm(profesional=None)

    def test_init(self):
        ProfesionalExtraForm(profesional=self.profesional)

    def test_formulario_bien_inicializado(self):
        form = ProfesionalExtraForm(profesional=self.profesional)
        self.assertEqual(form.initial['telefono'], '666666666')
        self.assertEqual(form.initial['nombre'], 'Yo me llamo Ralph')
        self.assertQuerysetEqual(form.initial['servicios'], [repr(self.servicio)])
        self.assertEqual(form.initial['email'], 'correo@correo.com')
        self.assertEqual(form.initial['codigo_postal'], '41001')

    def test_formulario_no_vacio(self):
        form = ProfesionalExtraForm({}, profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio(self):
        self.data_extra['nombre'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_nombre_no_vacio_2(self):
        self.data_extra['nombre'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio(self):
        self.data_extra['email'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_email_no_vacio_2(self):
        self.data_extra['email'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_servicio_no_vacio(self):
        self.data_extra['servicios'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        form.is_valid()
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_servicio_no_vacio_2(self):
        self.data_extra['servicios'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_telefono_no_vacio(self):
        self.data_extra['telefono'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_telefono_no_vacio_2(self):
        self.data_extra['telefono'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_codigo_postal_no_vacio(self):
        self.data_extra['codigo_postal'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_codigo_postal_no_vacio_2(self):
        self.data_extra['codigo_postal'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_metodo_no_vacio(self):
        self.data_extra['metodo_trabajo'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_metodo_no_vacio_2(self):
        self.data_extra['metodo_trabajo'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_precio_no_vacio(self):
        self.data_extra['precio'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_precio_no_vacio_2(self):
        self.data_extra['precio'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_fecha_nacimiento_no_vacio(self):
        self.data_extra['fecha_nacimiento'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_fecha_nacimiento_no_vacio_2(self):
        self.data_extra['fecha_nacimiento'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_foto_no_vacio(self):
        self.file_data['foto'] = None
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_foto_no_vacio_2(self):
        self.file_data['foto'] = ''
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_facebook_no_texto(self):
        self.data_extra['facebook'] = 'Pene'
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_facebook_url(self):
        self.data_extra['facebook'] = 'http://www.facebook.com'
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertTrue(form.is_valid())

    def test_linkedin_no_texto(self):
        self.data_extra['linkedin'] = 'Pene'
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertFalse(form.is_valid())

    def test_linkedin_url(self):
        self.data_extra['linkedin'] = 'http://www.batamanta.com'
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertTrue(form.is_valid())

    def test_formulario_completo(self):
        form = ProfesionalExtraForm(self.data_extra, self.file_data,  profesional=self.profesional)
        self.assertTrue(form.is_valid())
