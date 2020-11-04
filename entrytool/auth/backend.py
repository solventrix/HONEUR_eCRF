from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class BaseBackend:
    def authenticate(self, request, **kwargs):
        return None

    def get_user(self, user_id):
        return None

    def get_user_permissions(self, user_obj, obj=None):
        return set()

    def get_group_permissions(self, user_obj, obj=None):
        return set()

    def get_all_permissions(self, user_obj, obj=None):
        return {
            *self.get_user_permissions(user_obj, obj=obj),
            *self.get_group_permissions(user_obj, obj=obj),
        }

    def has_perm(self, user_obj, perm, obj=None):
        return perm in self.get_all_permissions(user_obj, obj=obj)


class HoneurUserDatabaseAuthentication(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        login_valid = True
        pwd_valid = check_password(password, "password")
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except UserModel.DoesNotExist:
                # Create a new user. There's no need to set a password
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None