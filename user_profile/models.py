# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# class UserManager(BaseUserManager):
#     def create_user(self, email, name, role, password=None, password2=None, **extra_fields):
#         """
#         Creates and saves a User with the given email, name, and role.
#         """
#         if not email:
#             raise ValueError("User must have an email address")

#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#             role=role,
#             **extra_fields
#         )
#         user.set_password(password)

#         if role.lower() == 'admin':
#             user.is_superuser = True
#             user.is_staff = True
#         else:
#             user.is_superuser = False
#             user.is_staff = False

#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password=None, password2=None, **extra_fields):
#         """
#         Creates and saves a superuser with the given email, name, and password.
#         """
#         extra_fields.setdefault('role', 'admin')
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)

#         if extra_fields.get('role').lower() != 'admin':
#             raise ValueError('Superuser must have role=admin.')

#         return self.create_user(email, name, **extra_fields)


# class User(AbstractBaseUser):
#     ROLE_CHOICES = (
#         ('admin', 'admin'),
#         ('customer', 'customer'),
#     )

#     role = models.CharField(max_length=15, choices=ROLE_CHOICES)
#     email = models.EmailField(
#         verbose_name="Email",
#         max_length=255,
#         unique=True,
#     )
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name", "role"]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return self.is_superuser

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
