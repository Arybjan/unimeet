from django.db.models.signals import post_save
from django.dispatch import receiver
from models import ( 
    UserRole, User, StudentProfile, ProfessorProfile, AdminProfile
)

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.role == UserRole.CLIENT:
        StudentProfile.objects.create(user=instance)

    elif instance.role == UserRole.MANAGER:
        ProfessorProfile.objects.create(user=instance)

    elif instance.role == UserRole.ADMIN:
        AdminProfile.objects.create(user=instance)
