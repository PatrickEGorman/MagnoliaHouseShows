from django.contrib import admin
from .models import MetaData


def meta_created_date(model):
    return model.metaData.posted_date


def meta_created_by(model):
    return model.metaData.posted_by


class MetaAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'posted_by', 'posted_date', 'last_edited_by', 'last_edited_date')

    def save_model(selfself, request, obj, form, change):
        obj.last_edited_by = request.user
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
