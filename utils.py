import json, jwt

from django.http  import JsonResponse
from json.decoder import JSONDecodeError

from my_settings  import ALGORITHM, SECRET_KEY
from users.models import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            user_info = jwt.decode(request.headers.get('Authorization'), SECRET_KEY, algorithms=ALGORITHM)
            user = User.objects.get(id=user_info['id'])
            request.user = user

            return func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status = 400)

        except JSONDecodeError:
            return JsonResponse({'message' : 'UNKNOWN_USER'}, status = 400)

        except UnicodeDecodeError:
            return JsonResponse({'message' : 'UNKNOWN_USER'}, status = 400)


    return wrapper