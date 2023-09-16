from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30)  # Add this line
    last_name = models.CharField(max_length=30)   # Add this line
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    # Required fields for the authentication system
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username




# from django.db import models

# class CustomUser(models.Model):
#     # Define your fields here
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     # Add more fields as needed
#     REQUIRED_FIELDS = ['password']
#     USERNAME_FIELD = 'username'
#     def __str__(self):
#         return self.username
    



# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     # Required fields for the authentication system
#     REQUIRED_FIELDS = ['email']
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username