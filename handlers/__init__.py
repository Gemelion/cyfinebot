from .registration import register_registration_handlers
from .menu import register_menu_handlers
from .admin import register_admin_handlers
from .privacy import register_privacy_handlers

def register_all_handlers(app):
    register_registration_handlers(app)
    register_menu_handlers(app)
    register_admin_handlers(app)
    register_privacy_handlers(app)
