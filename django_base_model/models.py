from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    add_user = models.ForeignKey(User, related_name='%(class)s_user_added')
    is_active = models.BooleanField(default=True)
    deactivate_user = models.ForeignKey(User, related_name='%(class)s_deactivate_user', null=True, blank=True)
    deactivate_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, user):
        self.is_active = False
        self.deactivate_user = user
        self.deactivate_date = timezone.now()
        self.save()

    def delete(self, **kwargs):
        raise NotImplementedError('This function is intentionally not supported. Use delete(user)')
