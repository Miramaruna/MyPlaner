# Serializers
from rest_framework import serializers

# models
from apps.main.models import User, Plan

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        age = attrs.get('age')
        
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        if len(password) < 8:
            raise serializers.ValidationError({'password': 'Password must be at least 8 characters long.'})
        if age is not None:
            if age > 148:
                raise serializers.ValidationError({'age': 'You must be at most 148 years old.'})
            if age < 13:
                raise serializers.ValidationError({'age': 'You must be at least 13 years old.'})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Удаляем confirm_password, так как оно не используется
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        if 'age' in validated_data:
            user.age = validated_data['age']  # Если age добавлен в профиль, установите его
        user.set_password(validated_data['password'])
        user.save()
        return user

    
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'created_at', 'email']
        
class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'user', 'title', 'description', 'created_at', 'deadline']