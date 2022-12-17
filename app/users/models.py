from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=10, blank=False, default='')
    password = models.CharField(max_length=10, blank=False, default='')
    firstname = models.CharField(max_length=50, blank=True, default='')
    lastname = models.CharField(max_length=50, blank=False, default='')
    email = models.CharField(max_length=50, blank=False, default='')

    # username = request.POST['username']
#         password = request.POST['password']
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         email = request.POST['email']
