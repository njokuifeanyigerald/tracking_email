from django.db import models

from django.db.models.fields import CharField, EmailField, UUIDField, BooleanField

class UserModel(models.Model):
    email = EmailField(max_length=254, blank=True, null=True)
    status = BooleanField(default=False)

    def __str__(self):
        return self.email
                