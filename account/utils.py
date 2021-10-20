from django.core.mail import send_mail


def send_activation_code(email, activation_code, status=None):
    if status == 'register':
        activation_url = f'http://localhost:8000/api/account/activate/{activation_code}'
        message = f"Поздравляем! Вы успешно зарегистрированы! Перейдите по ссылке для активации аккаунта: {activation_url}"

        send_mail(
            'Batbat.kg. Активация аккаунта',
            message,
            'admin.batbat@gmail.com',
            [email, ],
            fail_silently=False
        )

    elif status == 'reset_password':
        send_mail(
            'Batbat.kg. Сброс пароля',
            f'Ваш код активации: {activation_code}',
            'admin.batbat@gmail.com',
            [email, ],
            fail_silently=False,
        )