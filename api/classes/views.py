from django.shortcuts import render
from rest_framework import viewsets,status
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from userauth.models import UserProfile
from .models import Classroom, DoubtSection
from .permissions import IsStudent,IsTeacher
from .serializers import ClassroomSerializer, DoubtSectionSerializer
from userauth.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.response import Response
import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class ClassroomViewSet(viewsets.ModelViewSet):
    model = Classroom
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)
        queryset1 = Classroom.objects.filter(teacher=user_profile)
        queryset2 =  Classroom.objects.filter(student=user_profile)
        return queryset2 | queryset1

    def create(self, request):
        data = request.data
        user = request.user
        teacher = UserProfile.objects.get(user=user).pk
        random_code = get_random_string(6)
        while(Classroom.objects.filter(class_code=random_code)) :
            random_code = get_random_string(6)
        data['class_code'] = random_code
        data['teacher'] = teacher
        data['student'] = []
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsTeacher,IsStudent]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsTeacher,IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class ClassjoinView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request, format=None):
        class_code = request.data["class_code"]
        try:
            class_join = Classroom.objects.get(class_code=class_code)
        except:
            return Response({
                "error" : "No such class.",
                "user" : request.user.email
            },status=status.HTTP_400_BAD_REQUEST
            )
        
        current_user =  UserProfile.objects.get(user=request.user)
        class_join.student.add(current_user)
        class_join.save()
        return Response({'detail': f'{ request.user.email }joined{class_join.id} succesfully'}, status=status.HTTP_201_CREATED)


class DoubtSectionList(APIView):

    def get(self, request):
        doubts = DoubtSection.objects.all()
        serializer = DoubtSectionSerializer(doubts, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoubtSectionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DoubtSectionDetail(APIView):
    def get_object(self, pk):
        try:
            return DoubtSection.objects.get(pk = pk)
        except DoubtSection.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        doubt = self.get_object(pk)
        serializer = DoubtSectionSerializer(doubt)
        return Response(serializer.data)

    def put(self, request, pk):
        doubt = self.get_object(pk)
        serializer = DoubtSectionSerializer(doubt, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doubt = self.get_object(pk)
        doubt.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
