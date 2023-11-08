from django.apps import AppConfig

class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.category'
    verbose_name = 'Categorias'
    
    def ready(self):
        import apps.category.receivers
        return super().ready()
