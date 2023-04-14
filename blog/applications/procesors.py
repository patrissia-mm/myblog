from applications.home.models import Home

#Procesor para recuperar email y teléfono y mostrarlo en el footer de cada página
def home_contact(request):
    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }