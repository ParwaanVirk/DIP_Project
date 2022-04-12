from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,latitude, longitude, password=None):
        if not email:
            raise ValueError("Users must have an email adress")
        if not username:
            raise ValueError("Users must have a username")
        if not latitude:
            raise ValueError("User latitude not provided")
        if not longitude:
            raise ValueError("User longitude not provided")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            longitude = longitude,
            latitude = latitude,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, latitude, longitude, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            longitude = longitude,
            latitude = latitude,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user




class Account(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username = models.CharField(max_length=50, null=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    is_normaluser           = models.BooleanField(default=False)
    latitude                = models.FloatField(default=0)
    longitude               = models.FloatField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'latitude', 'longitude']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    #all admins have all permisions
    def has_perm(self, perm, obj=None):
        return self.is_admin
    #Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)