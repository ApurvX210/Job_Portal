from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

def return_date_time():
    now=datetime.now()
    return now+timedelta(days=10)

class jobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Internship = 'Internship'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Industry(models.TextChoices):
    Business = 'Business'
    IT= 'Information Technology'
    Banking = 'Banking'
    Education='Education'
    Telecommunication = 'Telecommunication'
    Others='Others'

class Experience(models.TextChoices):
    No_Experience = 'No Experience'
    One_Year = '1 year'
    Two_Year = '2 year'
    Three_Year_Plus='3 years above'


class Job(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=100,null=True)
    jobType=models.CharField(
        max_length=20,
        choices=jobType.choices,
        default=jobType.Permanent
    )
    education=models.CharField(
        max_length=20,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry=models.CharField(
        max_length=50,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience=models.CharField(
        max_length=20,
        choices=Experience.choices,
        default=Experience.No_Experience
    )
    salary=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(1000000)])
    position=models.IntegerField(default=1)
    company=models.CharField(max_length=100,null=True)  
    lastDate=models.DateTimeField(default=return_date_time)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        super(Job,self).save(*args,**kwargs)

class CandidateApplied(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    appliedAt=models.DateTimeField(auto_now_add=True)