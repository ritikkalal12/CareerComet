from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

QUALIFICATION_CHOICES = (
    ('High School', 'High School'),
    ('bachelor', 'Bachelor\'s Degree'),
    ('master', 'Master\'s Degree'),
    ('phd', 'Ph.D.'),
    ('Other', 'Other'),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES, max_length=20, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()


