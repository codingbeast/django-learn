from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    Age = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=50)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()