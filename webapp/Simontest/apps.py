from django.apps import AppConfig


class SimontestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Simontest'
    # 下面用verbose改显示名称
    verbose_name = '第一个站点'
