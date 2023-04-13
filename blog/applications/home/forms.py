from django import forms

#models
from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    """ Formulario para el Home para suscribirse """
    class Meta:
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Tú correo electrónico ... ',
                }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
