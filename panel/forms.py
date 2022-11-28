from django import forms

username = forms.CharField(
    min_length=4,
    max_length=50,
    label='Nombre de usuario'
)
password = forms.CharField(
    min_length=4,
    max_length=50,
    widget=forms.PasswordInput(),
    label="Contraseña"
)
password_confirmation = forms.CharField(
    min_length=4,
    max_length=50,
    widget=forms.PasswordInput(),
    label='Confirmar contraseña'
)

first_name = forms.CharField(
    min_length=2,
    max_length=50,
    label='Nombre'
)
last_name = forms.CharField(
    min_length=2,
    max_length=50,
    label='Apellido'
)
email = forms.CharField(
    widget=forms.EmailInput(),
    label='Email'
)