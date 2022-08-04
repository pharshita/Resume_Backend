from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformations
        # fields = ['id','profile_image','first_name','last_name','profession','city','country','phone_number','pin_code','email','social_links','profile_summary']
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = '__all__' 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsModel
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    Experience = serializers.SerializerMethodField()
    Education = serializers.SerializerMethodField()
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='skills',
    )
    class Meta:
        model = UserInformations
        fields = ['id','profile_image','first_name','last_name','profession','city','country','phone_number','pin_code','email','social_links','profile_summary','Education','Experience','skills']
    def get_Experience(self,instance):
        data = ExperienceModel.objects.filter(user=instance.id)
        return ExperienceSerializer(data,many=True).data

    def get_Education(self,instance):
        data = EducationModel.objects.filter(user=instance.id)
        return EducationSerializer(data,many=True).data


# class EditUserinformation(serializers.ModelSerializer):
#     class Meta:
#         model = UserInformations
#         fields = '__all__'

# class EditExperience(serializers.ModelSerializer):
#     class Meta:
#         model = ExperienceModel
#         fields = '__all__'

# class EditEducationModel(serializers.ModelSerializer):
#     class Meta:
#         model = EducationModel
#         fields = '__all__'



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobapplication
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ContectusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContectUs
        fields = '__all__'