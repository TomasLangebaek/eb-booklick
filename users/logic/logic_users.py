from ..models import User


def get_user_detail():

    user = User.objects.get(pk=1)
    return user


def get_users_list():

    users = User.objects.all()
    return users



