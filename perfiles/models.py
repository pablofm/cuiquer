from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
import uuid
import os


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre=None, telefono=None, password=None):
        if not email:
            raise ValueError('Debes proporcionar un correo válido')

        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            telefono=telefono,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            nombre=' - ',
            telefono='',
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    def foto_perfil_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('perfiles', filename)

    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=9)
    foto = models.ImageField(upload_to=foto_perfil_path, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
