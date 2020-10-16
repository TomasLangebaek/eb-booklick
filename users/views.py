
from .logic.logic_users import get_user_detail
from .logic.logic_users import get_users_list
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def get_user(request):

    user = get_user_detail()
    array_result = serializers.serialize('json', [user], ensure_ascii=False)
    just_object_result = array_result[1:-1]
    return HttpResponse(just_object_result, content_type='application/json')


def get_users(request):

    users = get_users_list()
    users_list = serializers.serialize('json', users)
    return HttpResponse(users_list, content_type='application/json')