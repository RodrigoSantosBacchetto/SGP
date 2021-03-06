#encoding utf-8
__author__ = 'sgp'

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, UserChangeForm
from django.contrib.auth.models import User, Group
from administracion.models import Proyecto, Fase

class UsuarioForm(UserCreationForm):
    """
    Formulario para la creacion de usuarios
    Hereda del formulario UserCreationForm y utiliza la clase user
    para agregar ciertos campos de la clase a la hora de la creacion
    """
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'telefono', 'direccion', 'observacion')

class AsignarRol(forms.ModelForm):
    """
    Formulario para la asignacion de roles a los usuarios
    Hereda del forms.ModelForm y utiliza la clase user
    para agregar ciertos campos de la clase a la hora de la asignacion
    """
    class Meta:
        model = User
        fields = ('groups',)

class ProyectoForm(ModelForm):
    """
    Formulario para la creacion de proyectos en el sistema
    Hereda de ModelForm y utiliza la clase Proyecto
    para agregar ciertos campos de la clase a la hora de la creacion
    """
    class Meta:
        model = Proyecto
        exclude = ['Usuario']

class UsuarioModForm(forms.ModelForm):
    """
    Formluario para la modificacion de usuarios
    Hereda de forms.ModelForm y utiliza la clase user para
    agregar ciertos campos a la hora de la modificacion
    """
    username = forms.RegexField(
        label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href= \"password/\">this form</a>."))
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'telefono', 'direccion', 'observacion')

    def __init__(self, *args, **kwargs):
            super(UsuarioModForm, self).__init__(*args, **kwargs)
            f = self.fields.get('user_permissions', None)
            if f is not None:
                f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
            # Regardless of what the user provides, return the initial value.
            # This is done here, rather than on the field, because the
            # field does not have access to the initial value
            return self.initial["password"]

class UsuarioDelForm(forms.ModelForm):
    """
    Formulario para el la eliminacion logica del usuario
    Hereda de forms.ModelForm y utiliza la clase user para
    agregar ciertos campos a la hora de la eliminacion
    """
    class Meta:
        model = User
        fields = ('is_active',)

class FaseForm(forms.ModelForm):
    """
    Formulario para el la creacion de fases
    Hereda de forms.ModelForm y utiliza la clase Fase para
    agregar ciertos campos a la hora de la creacion/modificacion
    """
    class Meta:
        model = Fase
        exclude = ['Usuario', 'Proyecto']

class RolForm(forms.ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    agregar ciertos campos a la hora de la creacion/modificacion/eliminacion
    """
    class Meta:
        model = Group
        exclude = ['Usuario']
