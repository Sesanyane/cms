from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'cms'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Contract Management System'
    institution = 'Botswana-Harvard AIDS Institute'
