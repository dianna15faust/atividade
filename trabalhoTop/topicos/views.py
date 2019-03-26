from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

#Como funcionam as classes dentro do “views”:
#class NomeDaPaginaView(TemplateView):
#    template_name = "index.html"
