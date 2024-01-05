from django.contrib import admin

# Register your models here.
from progress.models import Dance, Figure, Level

# class FiguresAdmin(admin.ModelAdmin):
#     fields=["figure_name, leader_description, follower_description, dance, level"]

# class DancesAdmin(admin.ModelAdmin):
#     fields=["dance_name"]

# class LevelsAdmin(admin.ModelAdmin):
#     fields=["level_name, level_value"]

admin.site.register(Dance)
admin.site.register(Figure)
admin.site.register(Level)