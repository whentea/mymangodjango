from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
 
class AboutPageView(TemplateView):
    template_name = "about.html"

class HelpPageView(TemplateView):
    template_name = "help.html"

# Create your views here.
