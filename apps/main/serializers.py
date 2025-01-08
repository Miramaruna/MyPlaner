# Serializers
from rest_framework import serializers

# models
from apps.main.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'password', 'confirm_password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        age = attrs.get('age')
        
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({password: 'Passwords must match.'})
        if len(password) < 8:
            raise serializers.ValidationError({password: 'Password must be at least 8 characters long.'})
        if age is not None:
            if age > 148:
                raise serializers.ValidationError({age: 'You must be at most 148 years old. WHAT THE HELL MAN????????BRUHHH'})
            if age < 13:
                raise serializers.ValidationError({'age': 'You must be at least 13 years old. GET OUR BRUHH'})
        return attrs
    
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'created_at', 'email']