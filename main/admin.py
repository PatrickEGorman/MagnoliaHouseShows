from django.contrib import admin
from .models import MetaData


def meta_created_date(model):
    return model.metaData.posted_on


def meta_created_by(model):
    return model.metaData.posted_by


def meta_updated_date(model):
    return model.metaData.last_updated_on


def meta_updated_by(model):
    return model.metaData.last_updated_by


class MetaAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'posted_by', 'posted_on', 'last_updated_on', 'last_updated_by')

    def save_model(self, request, obj, form, change):
        obj.last_updated_by = request.user
        if not obj.metaData.posted_by:
            obj.metaData.posted_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)


class ModelAdminWithMeta(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.metaData.last_updated_by = request.user
        if not obj.metaData.posted_by:
            obj.metaData.posted_by = request.user
        obj.metaData.save()
        super().save_model(request, obj, form, change)


admin.site.register(MetaData, MetaAdmin)
