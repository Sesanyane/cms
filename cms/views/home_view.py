from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'cms/home.html'
    navbar_name = 'cms'
    navbar_selected_item = 'home'
