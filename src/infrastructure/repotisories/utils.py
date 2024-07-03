def repository_setup():
    import os

    import django

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "src.presentation.admin_panel.config.settings"
    )
    django.setup()
