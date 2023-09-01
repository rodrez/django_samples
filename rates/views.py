import json

from django.views.generic import CreateView
from django.shortcuts import render
from jsonschema.validators import validate

from rates.forms import RateForm
from rates.models import Rate
from rates.schema import RATE_SCHEMA

# Create your views here.


class HomeView(CreateView):
    template_name = "rates/home.jinja"
    form_class = RateForm
    model = Rate

    def post(self, request, *args, **kwargs):
        # Create a new rate object
        rate = Rate()
        # Set the data field to the data from the form
        rate.data = request.POST.get("data")

        try:
            validate(json.loads(request.POST.get("data")), RATE_SCHEMA)
        except Exception as e:
            return render(
                request,
                self.template_name,
                {"error": f"Data is invalid: {e}"},
            )

        # Set the credit union field to the credit union from the form
        rate.credit_union = request.POST.get("credit_union")

        # Save the rate object
        rate.save()

        # Return the home page
        return render(request, self.template_name)
