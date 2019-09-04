from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fullname = models.CharField(max_length=50, null=True, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=False)

    # For printing out Profiles
    # Will now print Username Profile
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = img.convert('RGB')
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Stats(models.Model):

    Activity_CHOICES = [
        ('S', 'Sedentary'),
        ('A', 'Active'),
        ('VA', 'Very active'),
        ('EA', 'Extremely active')
    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=False)
    activity = models.CharField(max_length=2, choices=Activity_CHOICES, null=True, blank=False)
    # For printing out Profiles
    # Will now print Username Profile

    def __str__(self):
        return f'{self.profile.user.username} Stats'