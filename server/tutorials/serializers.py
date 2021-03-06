from rest_framework import serializers
from tutorials.models import Tutorial, User

 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password',
                  'balance',
                  'transactions'
                  )


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'balance',
                  'transactions'
                  )
