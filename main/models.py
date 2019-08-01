from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from main.util import parse_date_string

User = get_user_model()


class MetaData(models.Model):
    post_name = models.TextField(default='')

    posted_on = models.DateField()
    posted_by = models.ForeignKey(User, related_name="meta_data_posts", on_delete=models.SET_NULL, null=True)
    last_updated_on = models.DateField()
    last_updated_by = models.ForeignKey(User, related_name="meta_data_edits", on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(MetaData, self).__init__(*args, **kwargs)
        if not self.posted_on:
            self.posted_on = timezone.now()

    def set_name(self, name):
        self.post_name = name

    def save(self, *args, **kwargs):
        self.last_updated_on = timezone.now()
        super(MetaData, self).save(*args, **kwargs)

    @property
    def posted_date_string(self):
        return parse_date_string(self.posted_on)

    @property
    def posted_string(self):
        if(self.posted_by):
            return "Posted by %s, on %s" % (self.posted_by.name, self.posted_date_string)
        else:
            return "Posted on %s" % self.posted_date_string

    @property
    def updated_date_string(self):
        if self.last_updated_on == self.posted_on:
            return None
        return parse_date_string(self.last_updated_on)

    @property
    def updated_string(self):
        if self.last_updated_on:
            return "Last updated by %s, on %s" % (self.last_updated_by.name, self.updated_date_string)
        else:
            return None
