from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    UserManager,
    PermissionsMixin
)
from django.utils import timezone


class CustomUserManager(UserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a vaild email address")

        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True, error_messages="Email Already Taken")
    password = models.CharField(max_length=200)
    phone = models.CharField(blank=False, max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=timezone.now())
    last_login = models.DateTimeField(blank=True, null=True)
    is_token_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=300, blank=True, null=True)
    token_pin_id = models.CharField(max_length=300, blank=True, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    
    # section for mananging api session login
    key  = models.CharField(max_length = 150,blank=True, null=True)
    message  = models.CharField(max_length = 600, blank=True, null=True)
    encoded  = models.CharField(max_length = 600, blank=True, null=True)
    encrypt_date = models.DateField(auto_now=False,default=timezone.now)
    rsa_duration = models.IntegerField(default=24)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'AuthUser'
        verbose_name_plural = "AuthUsers"

    def __str__(self):
        return  self.email
        
    def get_username(self):
        return  self.username

    def natural_key(self):
        return  self.email.split('@')[0]


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)





class Agent(CustomUser):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    address = models.TextField(blank=False)
    
    def save(self):
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active=True
            self.is_staff=True
        super().save()
        
        
class Client(CustomUser):
    first_name = models.CharField(blank=False, max_length=50)
    address = models.TextField(blank=False)
    
    def save(self):
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active=True
        super().save()
    


class Driver(CustomUser):
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER, blank=False)
    address = models.TextField(blank=False)
    
    def save(self):
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active=True
            self.is_staff=True
        super().save()



class Vendor(CustomUser):    
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER, blank=False)
    address = models.TextField(blank=False)
    
    def save(self):
        if not len(self.password) > 20:
            super().set_password(self.password)
            self.is_active=True
            self.is_staff=True
        super().save()
            