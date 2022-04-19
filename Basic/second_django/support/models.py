from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()

    Category = (
        ('일반', '일반')
        ('계정', '계정')
        ('기타', '기타')
    )
    category = models.CharField(max_length=2, choices=Category)

    answer = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    update_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='update_writer')
    updated_at = models.DateTimeField(auto_now=True)
