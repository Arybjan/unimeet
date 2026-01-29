from rest_framework import serializers
from user import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentProfile
        fields = "__all__"


class ProfessorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessorProfile
        fields = "__all__"
