from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from django.core.validators import MaxValueValidator


class User(AbstractUser):

    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to = 'images/', blank=True, null=True)
    is_patient = models.BooleanField(default = False)
    is_doctor = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, )
    line1 = models.CharField(max_length=30, blank = True, null= True)
    city = models.CharField(max_length=20, blank = True, null= True)
    state = models.CharField(max_length=20, blank = True, null= True)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], blank = True, null= True)

    def __str__(self):
        return str(self.user)
