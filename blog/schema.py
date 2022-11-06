from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from blog import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
