from ..models import Users


def get_user_detail():

    user = Users.objects.get(pk=1)
    return user


def get_users_list():

    users = Users.objects.all()
    return users



