

from accounts.models import User
from django.contrib.auth.backends import ModelBackend 

class EmailAuthBackend(ModelBackend):
    print('back 7')
    @staticmethod
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return None

        if not user.check_password(password):
            return None

        return user

    @staticmethod
    def get_user(user_id):
        print('back 22')
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
