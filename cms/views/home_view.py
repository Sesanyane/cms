from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin

from contract.models import Consultant, Employee, Pi 


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'cms/home.html'
    navbar_name = 'cms'
    navbar_selected_item = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.all()
        cosultant = Consultant.objects.all()
        pi = Pi.objects.all()
        
        total = employees.count() + cosultant.count() + pi.count()
        context.update(
            total=total,
            employees_total=employees.count(),
            cosultant_total=cosultant.count(),
            pi_total=pi.count()
            )
        return context