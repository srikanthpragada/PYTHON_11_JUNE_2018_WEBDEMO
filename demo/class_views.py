from django.views.generic import TemplateView, ListView
from .models import Department


class AboutView(TemplateView):
    template_name = "about.html"


class DeptListView(ListView):
    model = Department
