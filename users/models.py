from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import *
from rest_framework.authtoken.models import Token

class IMUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('EIT', 'entrepreneur in training'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    date_created = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    Is_blocked = models.BooleanField(default=False)
    temporal_login_failed = models.IntegerField(default=0)
    permanent_login_failed = models.IntegerField(default=0)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
@receiver(post_save, sender=IMUser)    
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()

class Cohort(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.SET_NULL, null=True, related_name='+')

    

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name} - {self.cohort.name}'
