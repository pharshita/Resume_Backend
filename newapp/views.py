from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  AllowAny
from django.contrib.auth import authenticate
from rest_framework import viewsets
from django.core.mail import EmailMessage
from django.conf import settings

class RegisterUserView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        request_data['is_active'] = True
        serializer = UserSerializer(data = request_data)
        if serializer.is_valid():
            new = serializer.save()
            new.set_password(new.password)
            new.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class UserDetailView(APIView):
    def get(self, request):
        queryset = User.objects.get(id=request.user.id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request,id):
        queryset = User.objects.get(id=request.user.id)
        serializer = UserSerializer(instance=queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ChangePasswordView(APIView):
    def patch(self, request):
        queryset = User.objects.get(id=request.user.id)
        request_data = request.data.copy()
        email = queryset.email
        old_password = request_data['old_password']
        user = authenticate(email=email, password=old_password)
        if user is not None:
            request_data['password'] = request_data['new_password']  
            serializer = UserSerializer(instance=queryset,data=request_data,partial=True)
            if serializer.is_valid():
                new = serializer.save()
                new.set_password(new.password)
                new.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Incorrect password'})

# class AllUserListView(APIView):
#     def get(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class LogoutView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             print(BlacklistedToken.objects.all())
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    def get(self, request):
        queryset = UserInformations.objects.filter(user = request.user)
        serializers = UserInformationSerializer(queryset,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        request_data['user'] = request.user.id
        serializer = UserInformationSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        

class EducationListView(APIView):
    def get(self, request):
        queryset = EducationModel.objects.all()
        serializer = EducationSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        user = UserInformations.objects.filter(id=request.data.get('user')).first()
        request_data['user'] = user.id
        serializer = EducationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ExperienceListView(APIView):
    def get(self, request):
        queryset = ExperienceModel.objects.all()
        serializer = ExperienceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        user = UserInformations.objects.filter(id=request.data.get('user')).first()
        request_data['user'] = user.id
        serializer = ExperienceSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class SkillListView(APIView):
    def get(self, request):
        queryset = SkillsModel.objects.all()
        serializer = SkillSerializer(queryset,many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def post(self, request):
        new = UserInformations.objects.filter(id=request.data.get('id')).first()
        if new:
            data = request.data.get("skills")
            data = data.split(",")
            for i in data:
                request_data = request.data.copy()
                request_data.pop('skills')
                request_data['skills'] = i
                serializer = SkillSerializer(data=request_data)
                if serializer.is_valid():
                    serializer.save()
                    skill_obj = SkillsModel.objects.filter(skills=i).first()
                    new.skills.add(skill_obj)
                    new.save() 
                else:
                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("user not found", status=status.HTTP_404_NOT_FOUND)

class ResumeListView(APIView):
    def get(self,request):
        quesyset = UserInformations.objects.filter(user=request.user.id)
        serializer = ResumeSerializer(quesyset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class ResumedetailView(APIView):
    def get(self, request,id):
        queryset = UserInformations.objects.filter(id=id).first()
        serializer = ResumeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request,id):
        queryset = UserInformations.objects.filter(id = id).first()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobApplications(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        queryset = Jobapplication.objects.all()
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ApplicationSerializer(data= request.data)
        if serializer.is_valid():
            Name = request.data.get('full_name')
            email = request.data.get('email')
            contact_no = request.data.get('phone_number')
            resume = request.data.get('resume')

            subject = 'Job application'
            from_email = settings.EMAIL_HOST_USER
            contact_message = "%s %s %s %s %s via %s" % (
            'Full name :',Name , '\n'
            'Contaact no. :',contact_no , '\n'
            'Email :',email)
            mail = EmailMessage(subject,contact_message,from_email,['ramkrishna.mrdigito@gmail.com'])
            mail.attach(resume.name, resume.read(), resume.content_type)
            mail.send()
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class JobList(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    authentication_classes  = []
    permission_classes = []
    serializer_class = JobSerializer

class ContectForm(APIView):
    def get(self,request):
        queryset = ContectUs.objects.all()
        serializer = ContectusSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ContectusSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

# class EditResumeView(APIView):
#     def patch(self, request,id):

#         queryset = UserInformations.objects.filter(id=id).first()
#         serializer = EditUserinformation(queryset,data=request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             queryset = ExperienceModel.objects.filter(id=id).first()
            
#             if serializer.is_valid():
#                 serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)








    

