from django.shortcuts import render
from .logic.logic_users import get_all_users
from django.http import HttpResponse
from django.core import serializers

def get_users(request):
    users = get_all_users()
    users_list = serializers.serialize('json', users)
    return HttpResponse(users_list, content_type = 'application/json')
