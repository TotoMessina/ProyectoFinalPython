from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'