from rest_framework import viewsets, generics
from user import models, serializer


class UserViewSet(viewsets.ViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer


class StudenProfileViewSet(viewsets.ViewSet):
    queryset = models.StudentProfile.objects.all()
    serializer_class = serializer.StudentProfileSerializer


class ProfessorViewSet(viewsets.ViewSet):
    queryset = models.ProfessorProfile.objects.all()
    serializer_class = serializer.ProfessorProfileSerializer
