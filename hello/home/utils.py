# utils.py

from .models import CustomUser

def create_user(name, email, phone, password):
    user = CustomUser(name=name, email=email, phone=phone, password=password)
    user.save()

def get_user_by_email(email):
    try:
        return CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None

def authenticate_user(email, password):
    user = get_user_by_email(email)
    if user and user.password == password:
        return user
    return None
