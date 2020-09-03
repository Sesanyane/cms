from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_sms.apps import AppConfig as BaseEdcSmsAppConfig


class AppConfig(DjangoAppConfig):
    name = 'cms'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Contract Management System'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcSmsAppConfig(BaseEdcSmsAppConfig):
    locator_model = 'contract.contract'
    consent_model = None
    locator_auto_create_contact = False
