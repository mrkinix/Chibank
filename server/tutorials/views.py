from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response

from tutorials.models import User
from tutorials.serializers import UserSerializer, DataSerializer, UserInfoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user(request):
    if request.method == 'GET':
        users = User.objects.values('first_name', 'last_name', 'email')
        user_serializer = DataSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        if user_data['login']:
            users = User.objects.filter(email=user_data['email'])
            user_serializer = UserInfoSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        else:
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
    user_data = JSONParser().parse(request)
    email = user_data['email']
    destination = user_data['destination']
    amount = user_data['amount']
    res = User.objects.get(email=email)
    res1 = User.objects.get(email=destination)

    str0 = "You payed {} {} €.".format(user_data['receiver'], amount)
    str1 = "{} payed you {} €.".format(user_data['sender'], amount)

    res.transactions.append(str0)
    res1.transactions.append(str1)
    User.objects.filter(email=email).update(balance=res.balance-amount,
                                            transactions=res.transactions)
    User.objects.filter(email=destination).update(balance=res1.balance+amount,
                                                  transactions=res1.transactions)

    return Response({'balance': res.balance}, status=status.HTTP_201_CREATED)



