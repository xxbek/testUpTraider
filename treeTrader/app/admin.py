from django.contrib import admin
from .models import *


class DashboardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'user_id', )
    search_fields = ('name',)
    empty_value_display = "-пусто-"


class TreePointAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user_id', 'dashboard_id', 'parent_id', )
    search_fields = ('name',)
    empty_value_display = "-пусто-"


class TreePointRelationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'point_id', 'child_id', )
    search_fields = ('text',)
    empty_value_display = "-пусто-"


admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(TreePoint, TreePointAdmin)
admin.site.register(TreePointRelation, TreePointRelationAdmin)

