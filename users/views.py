import json, bcrypt, jwt
from json.decoder import JSONDecodeError

from django.http  import JsonResponse
from django.views import View
from django.db    import IntegrityError

from my_settings  import SECRET_KEY, ALGORITHM
from .models      import User
from .validations import validate_account, validate_password

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            account  = data['account']
            password = data['password']

            if not validate_account(account):
                return JsonResponse({'message' : 'INVALID_ACCOUNT'}, status = 400)

            if not validate_password(password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                name          = data['name'],
                account       = account,
                password      = hashed_password.decode('utf-8'),
                date_of_birth = data.get('date_of_birth'),
            )

            return JsonResponse({'message' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        except IntegrityError:
            return JsonResponse({'message' : 'DUPLICATED_ACCOUNT'}, status = 400)

class SigninView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']
            user     = User.objects.get(account=account)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            token = jwt.encode({'id' : user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'message' : 'SUCCESS', 'token' : token}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status = 400)