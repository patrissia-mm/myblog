import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView, CreateView
)

#models
from applications.entrada.models import Entry
from .models import Home
#forms
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = 'home/index.html'
    # redefiniendo la función para enviar contextos a la página index.html
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargar el home el último de acuerdo a la fecha de creación
        context['home'] = Home.objects.latest('created')
        #contexto portada a través de un manager
        context['portada'] = Entry.objects.entrada_en_portada()
        #contexto entradas_home para mostrar 4 entradas
        context['entradas_home'] = Entry.objects.entradas_en_home()
        #contexto entradas_recientes para mostrar las últimas 6 entradas
        context['entradas_recientes'] = Entry.objects.entradas_recientes()
        #enviar el formulario
        context['form'] = SuscribersForm
        return context

class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'


    
