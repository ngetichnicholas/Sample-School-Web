from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator,MinLengthValidator
from cloudinary.models import CloudinaryField
from django.db.models.deletion import SET_NULL

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

TERM_CHOICES = (
    ('TERM-1','TERM-1'),
    ('TERM-2','TERM-2'),
    ('TERM-3','TERM-3'),

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

class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.TextField()

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()

    def __str__(self):
        return self.name
    
    @classmethod
    def update_contact(cls, id ,name,email ,message):
        update = cls.objects.filter(id = id).update(name = name,email = email,message=message)
        return update

    @classmethod
    def get_all_contacts(cls):
        contacts = cls.objects.all()
        return contacts

    @classmethod
    def get_contact_id(cls,id):
        contact_id = cls.objects.filter(id= id).all()
        return contact_id
    
    def __str__(self):
        return self.name

class ExamResults(models.Model):
    exam_name = models.CharField(max_length=144)
    form = models.CharField(max_length=10,choices=FORM_CHOICES)
    description = models.TextField()
    term = models.CharField(max_length=10,choices=TERM_CHOICES)

class Post(models.Model):
    title = models.CharField(max_length=144)
    post = models.TextField()
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()