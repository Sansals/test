from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Вызвать исключение, если не предоставлена почта.
        if username is None:
            raise serializers.ValidationError(
                'An username address is required to log in.'
            )

        # Вызвать исключение, если не предоставлен пароль.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Метод authenticate предоставляется Django и выполняет проверку, что
        # предоставленные почта и пароль соответствуют какому-то пользователю в
        # базе данных.
        user = authenticate(username=username, password=password)

        # Если пользователь с данными почтой/паролем не найден, то authenticate
        # вернет None. Возбудить исключение в таком случае.
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        # сообщить, был ли пользователь деактивирован или заблокирован.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # возвращаем словать проверенных данных, в т.ч. в методы create и update.
        return {
            'username': user.username
        }