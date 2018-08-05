from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfilio_site = models.URLField(blank=True)

    portfilio_picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username