from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser
from .utils import send_activation_code


# Регистрация
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    password_confirm = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_num', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        phone_num = validated_data.get('phone_num')

        user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                                              last_name=last_name, phone_num=phone_num)
        send_activation_code(email=user.email, activation_code=user.activation_code, status='register')
        return user


# Вход в аккаунт
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                message = 'Неправильный логин или пароль.'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Введите логин или пароль.'
            raise serializers.ValueError(message, code='authorization')

        attrs['user'] = user
        return attrs


# Создание нового пароля
class CreateNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.CharField(max_length=1000,
                                            required=True)
    password = serializers.CharField(min_length=8,
                                     required=True)
    password_confirm = serializers.CharField(min_length=8,
                                     required=True)

    def validate_email(self, email):
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не найден.')
        return email

    def validate_activation_code(self, act_code):
        if not CustomUser.objects.filter(activation_code=act_code,
                                         is_active=False).exists():
            raise serializers.ValidationError('Неверный код активации.')
        return act_code

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают.')
        return attrs

    def save(self, **kwargs):
        data = self.validated_data
        email = data.get('email')
        activation_code = data.get('activation_code')
        password = data.get('password')
        try:
            user = CustomUser.objects.get(email=email, activation_code=activation_code, is_active=False)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Пользователь не найден.')

        user.is_active = True
        user.activation_code = ''
        user.set_password(password)
        user.save()
        return user
