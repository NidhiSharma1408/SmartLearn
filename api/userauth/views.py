from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser, IfUserPasswordReset

from .models import User, OtpModel
from .serializers import UserSerializer

from django.http import Http404

from random import randint
from django.core.mail import send_mail

import time


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        coming_data      = request.data
        
        user_otp         = coming_data.get("otp", "")
        user_email       = coming_data.get("email", "")

        try:
            query        = OtpModel.objects.filter(otp_email__iexact = user_email)[0]
        except:
            raise Http404

        model_email      = query.otp_email 
        model_otp        = query.otp
        
        otp_creation_time = query.time_created
        current_time = int(time.time())
        
        if user_email == model_email and user_otp == model_otp and (current_time - otp_creation_time < 300):
            serializer = UserSerializer(data = coming_data)
            if serializer.is_valid():
                serializer.save()
                query.delete()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]



class PasswordResetView(APIView):
    permission_classes = [IfUserPasswordReset]

    def post(self, request):
        email = request.data.get("email","")
        password = request.data.get("password", "")
        if email and password:
            try:
                user = User.objects.filter(email__iexact = email)[0]
            except:
                raise Http404
            user.set_password(password)
            user.save()
            return Response(status = status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

# class ForgotPasswordView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):




class OtpCreation(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user_email = request.data.get("email", "")
        if user_email:
            user = User.objects.filter(email__iexact = user_email)
            
            if user.exists():
                    return Response(status = status.HTTP_226_IM_USED) # "User with this email already exists"
            else:
                    otp = randint(100000, 999999) 
                    time_of_creation = int(time.time())
                    OtpModel.objects.create(otp = otp, otp_email = user_email, time_created = time_of_creation)
                    mail_body = f"Hello Your OTP for registration is {otp}. This OTP will be valid for 5 minutes."
                    send_mail('OTP for registering on SmartLearn', mail_body, 'nidhi.smartlearn@gmail.com', [user_email], fail_silently = False) 
                    return Response(status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST) # "User must provide an email"


        