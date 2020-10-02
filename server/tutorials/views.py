from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial, User
from tutorials.serializers import TutorialSerializer, UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def user(request):
    if request.method == 'GET':
        users = User.objects.all()

        email = request.GET.get('email', None)
        pwd = request.GET.get('password', None)
        if email and pwd is not None:
            users = users.filter(email=email, password=pwd)

        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_connection(request):
    user_data = JSONParser().parse(request)
    email = user_data['email']
    pwd = user_data['password']
    res = User.objects.get(email=email)
    if email and pwd is not None:
        if res.password == pwd:
            print(res.password)
            user_serializer = UserSerializer(res, many=False)
            print(user_serializer)
            return JsonResponse(user_serializer.data, safe=False)


@api_view(['POST'])
def user_transaction(request):
    # add cookies to verify
    user_data = JSONParser().parse(request)
    email = user_data['email']
    destination = user_data['destination']
    amount = user_data['amount']
    res = User.objects.get(email=email)
    res1 = User.objects.get(email=destination)
    if email is not None:
        res.balance += amount
        res.balance -= amount
        user_serializer1 = UserSerializer(data=res1)
        user_serializer = UserSerializer(data=res)
        if user_serializer.is_valid():
            user_serializer.save()

        if user_serializer.is_valid():
            user_serializer1.save()

        return JsonResponse(status=status.HTTP_201_CREATED)
