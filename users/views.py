from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from users.models import IMUser
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])

def user_profile(request):
    return JsonResponse({
        "name": "Tafadzwa Choga",
        "age": 30,
        "city": "New York"
    })

def signUp(request):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")
    
    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number
    )

    new_user.set_password(password)
    new_user.save()
    #new_user.generate_auth_token()
    serializer = UserSerializer(new_user, many=False)
    return Response({"message":"Account successfuly created", "result":serializer.data})

def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = IMUser.objects.get(username=username)
    if user.check_password(password):
        auth_user = authenticate(username=username, password=password)

        if auth_user:
                if user.is_active:
                    if user.Is_blocked:
                        user.temporal_login_failed += 1
                        return Response({"message":"Your account has been deactivated, please contact support"})
                    else:
                         login(request, user)
                         UserSerializer= UserSerializer(user, many=False)
                         return Response({"message":"Login successful", "result":UserSerializer.data})
                else:
                  return Response({"message":"Your account has been blocked, please contact support"})
        user.temporal_login_failed += 1
        user.save()
        return Response({"message":"Login successful", "result":UserSerializer.data})
    else:
        return Response({"message":"Invalid login credentials"})
    
class ForgotPassword(APIView):

    @action_
    def post(self, request):

        #1. receive the username
        #2. find the user with the username
        #3  send otp code to the user
        username = request.data.get("username")
        if not username:
            return Response({"message":"Username is required"})
        user = IMUser.objects.get(username=username)

        if user:
            user.send_reset_password_email()
            return Response({"message":"An email has been sent to your email address"})
        else:
            return Response({"message":"User not found"})
    
   