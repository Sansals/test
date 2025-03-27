from login.models import User_Status

def get_user_email(request):
    if request.user.is_authenticated:
        return request.user.email
    else:
        return None
        #logging

def get_user_id(request):
    if request.user.is_authenticated:
        return request.user.id
    else:
        return None

def get_user(request):
    if request.user.is_authenticated:
        return request.user
    else:
        return None
        #logging

def get_username(request):
    if request.user.is_authenticated:
        return request.user.username
    else:
        return 'Нет пользователя'

def get_user_verify_is(request):
    if request.user.is_authenticated:
        try:
            return User_Status.objects.get(username=request.user.id).Isverified
        except ValueError:
            pass
            #loging
        except Exception:
            pass
            #login
    else:
        return None

