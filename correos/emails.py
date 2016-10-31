from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def enviar_correo(para, asunto, plantilla, contexto, adjuntos=None):
    plaintext = get_template('correos/{}.txt'.format(plantilla))
    htmly = get_template('correos/{}.html'.format(plantilla))
    d = Context(contexto)
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    correo = EmailMultiAlternatives(asunto, text_content, 'hello@cuiquer.com', [para])
    correo.attach_alternative(html_content, "text/html")
    correo.attachments = adjuntos
    correo.send()


def correo_mensaje_agradecimiento(para):
    contexto = {}
    return enviar_correo(para=para, asunto='Mensaje recibido', plantilla='mensaje-agradecimiento', contexto=contexto)


def correo_alta_newsletter(para):
    contexto = {}
    return enviar_correo(para=para, asunto='Bienvenido a Cuiquer', plantilla='alta-newsletter', contexto=contexto)


def correo_alta_cliente(para):
    contexto = {}
    return enviar_correo(para=para, asunto='Bienvenido a Cuiquer', plantilla='alta-cliente', contexto=contexto)


def correo_alta_profesional(para):
    contexto = {}
    return enviar_correo(para=para, asunto='Bienvenido a Cuiquer', plantilla='alta-profesional', contexto=contexto)
