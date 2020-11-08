import logging, os
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from entrytool.auth.UserDatabase import UserDatabase

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

    def __init__(self):
        self.user_db = UserDatabase(os.environ['USER_DB_USER'],
                                    os.environ['USER_DB_PASSWORD'],
                                    os.environ['USER_DB_HOST'],
                                    os.environ['USER_DB_PORT'],
                                    os.environ['USER_DB_NAME'])

    def authenticate(self, request, username, password):
        logging.info("Authenticate {}".format(username))

        valid_username_password = self.user_db.check_password(username, password)
        if not valid_username_password:
            logging.warning("Invalid username and/or password!")
            return None
        try:
            user = User.objects.get(username=username)
        except UserModel.DoesNotExist:
            # Create a new user. There's no need to set a password
            logging.info("Create user {}".format(username))
            user = User(username=username)
            user.is_active = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None