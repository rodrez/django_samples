from django.views.generic import View
from django.shortcuts import render


# Create your views here.
class HomeView(View):
    template_name = "rates/home.jinja"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
