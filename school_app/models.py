from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    full_name = models.CharField(max_length=144)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, null=True,blank=True, validators=[MinLengthValidator(10),MaxLengthValidator(13)])

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.username

FORM_CHOICES = (
    ('FORM-1','FORM-1'),
    ('FORM-2','FORM-2'),
    ('FORM-3','FORM-3'),
    ('FORM-4','FORM-4'),
)

class Student(models.Model):
    full_name = models.CharField(max_length=144)
    form = models.CharField(max_length=10,choices=FORM_CHOICES)

    def save_student(self):
        self.save()

    def delete_student(self):
        self.delete()

    def __str__(self):
        return self.full_name

class NoticeBoard(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField()
    document = models.FileField(upload_to='documents/notice_board/')
