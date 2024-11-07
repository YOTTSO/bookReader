from django.db import models
from django.contrib.auth.models import User
from library.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    favorite_books = models.ManyToManyField(Book, related_name='favorited_by', blank=True)
    display_name = models.CharField(max_length=255, blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.pk:
            existing_profile = UserProfile.objects.get(pk=self.pk)
            if existing_profile.profile_picture and existing_profile.profile_picture != self.profile_picture:
                existing_profile.profile_picture.delete(save=False)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"