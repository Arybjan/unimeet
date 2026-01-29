from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser должен иметь is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class GenderChoice(models.TextChoices):
    FEMALE = "Female", "Женский"
    MALE = "Male", "Мужской"
    TRANSGENDER = "Transgender", "Трансгендер"


class UserRole(models.TextChoices):
    STUDENT = "student", "Студент"
    PROFESSOR = "professor", "Преподаватель"
    ADMIN = "admin", "Администратор"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Email")

    role = models.CharField(
        max_length=20, choices=UserRole.choices, default=UserRole.STUDENT
    )

    age = models.PositiveBigIntegerField(null=False)

    gender = models.CharField(max_length=20, choices=GenderChoice.choices, default=None)

    is_staff = models.BooleanField(default=False, help_text="Доступ в админку Django")

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"


class StudentProfile(models.Model):
    user_profile = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"StudentProfile: {self.user.email}"


class ProfessorProfile(models.Model):
    user_profile = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="professor_profile"
    )
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"ProfessorProfile: {self.user.email}"


class AdminProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="admin_profile"
    )

    access_level = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"AdminProfile: {self.user.email}"
