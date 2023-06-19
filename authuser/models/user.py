from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    UserManager
)
from django.utils import timezone

ACCOUNT_TYPE = [
    ('vendor','Vendor'),
    ('agent','Agent'),
    ('driver','Driver'),
    ('users','users')
]

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
        

class User(AbstractBaseUser):
    email = models.EmailField(('email address'), unique=True, error_messages="Email Already Taken")
    password = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE, default='users')
    created = models.DateTimeField(auto_now_add=timezone.now())
    last_login = models.DateTimeField(blank=True, null=True)
    is_token_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=300, blank=True, null=True)
    token_pin_id = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20)
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
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return  self.email.split('@')[0]
        
    def get_username(self):
        return  self.email.split('@')[0]
        
    def get_short_name(self):
        return  self.email.split('@')[0]

    def natural_key(self):
        return  self.email.split('@')[0]

    def has_module_perms(self, *args, **kwargs):
        return self.is_staff
 
    def has_perm(self, *args, **kwargs):
        return self.is_staff