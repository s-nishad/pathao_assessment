from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.firstName


class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=50)
    expiry = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'tag')

    def __str__(self):
        return self.tag
