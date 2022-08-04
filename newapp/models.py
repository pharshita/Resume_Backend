from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
   email = models.EmailField(_('email address'), unique = True)
   mobile_no = models.CharField(max_length = 10)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
   def __str__(self):
       return "{}".format(self.email)

class SkillsModel(models.Model):
    skills = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.skills


class UserInformations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='User')
    profile_image = models.ImageField(upload_to='media',blank=True,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profession  = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    phone_number = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=8,blank=True,null=True)
    email = models.EmailField()
    social_links = models.URLField(blank=True,null=True)
    skills = models.ManyToManyField(SkillsModel,blank=True,null=True)
    profile_summary = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.first_name


class ExperienceModel(models.Model):
    user = models.ForeignKey(UserInformations,on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    Company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    job_discription = models.TextField()
    project_name = models.CharField(max_length=255,null=True,blank=True)
    project_urls = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.job_title

class EducationModel(models.Model):
    user = models.ForeignKey(UserInformations,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.school_name


class Jobapplication(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    resume = models.FileField(upload_to='media')

    def __str__(self):
        return self.email
        
    def __repr__(self):
        return '<Application %s>'% self.email
        
class Job(models.Model):
    class Requirement(models.TextChoices):
        PYTHON = 'python', _('Python Developer')
        REACT = 'react', _('React Developer')
    job_name = models.CharField(max_length=105,null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    number_of_openings = models.IntegerField(null=True, blank=True)
    experience_requride = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10 )], null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    requirement = models.CharField(max_length=12, choices=Requirement.choices, default='python')
    perks_and_benefits = models.TextField(null=True, blank=True)
    skills_required = models.CharField(max_length=100, null=True, blank=True)
