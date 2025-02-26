from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('text', 'Text Only'),
        ('image', 'Image Post'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='text')

    class Meta:
        ordering = ['-created_at']  # Default: Show newest posts first

    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"
