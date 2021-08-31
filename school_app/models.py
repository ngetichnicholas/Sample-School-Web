from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=144)
    last_name = models.CharField(max_length=144)
    phone = models.CharField(max_length=13, null=True,blank=True, validators=[MinLengthValidator(10),MaxLengthValidator(13)])

