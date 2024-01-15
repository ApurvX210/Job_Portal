from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .models import Job,CandidateApplied
from rest_framework.response import Response
from .serializers import JobSerializer,CandidateAppliedSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Avg,Min,Max,Count
from .filters import JobFilter
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET']) #So in views either we create template using html or in this case when we are using django rest framework we are creating sort of controller here
def getAllJobs(request):

    filterset = JobFilter(request.GET,Job.objects.all().order_by('id'))
    #Pagination
    count=filterset.qs.count()
    jobPerPage = 3
    paginator = PageNumberPagination()
    paginator.page_size =jobPerPage

    queryset=paginator.paginate_queryset(filterset.qs,request)
    serializer = JobSerializer(queryset,many=True)
    return Response({
        'count':count,
        'jobs':serializer.data,
        'jobPerPage':jobPerPage
    })

@api_view(['GET'])
def getJob(request,pk):

    job=get_object_or_404(Job,id=pk)

    serializer = JobSerializer(job,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createJob(request):
    request.data['user']=request.user
    data=request.data
    job = Job.objects.create(**data) #Spread the data similar to javascript

    serializer = JobSerializer(job,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateJob(request,pk):
    job=get_object_or_404(Job,id=pk)
    if job.user !=request.user:
        return Response({'message':'You cannot update this job'},status=status.HTTP_403_FORBIDDEN)
    job.title=request.data['title']
    job.description=request.data['description']
    job.email=request.data['email']
    job.address=request.data['address']
    job.jobType=request.data['jobType']
    job.education=request.data['education']
    job.industry=request.data['industry']
    job.experience=request.data['experience']
    job.salary=request.data['salary']
    job.position=request.data['position']
    job.company= request.data['company']

    job.save()
    serializer = JobSerializer(job,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteJob(request,pk):

    job=get_object_or_404(Job,id=pk)
    if job.user !=request.user:
        return Response({'message':'You cannot update this job'},status=status.HTTP_403_FORBIDDEN)
    job.delete()

    return Response({'message':'Job Deleted Successfully'},status=status.HTTP_200_OK)

@api_view(['GET'])
def getTopicStats(request,topic):

    args={'title__icontains':topic}
    jobs=Job.objects.filter(**args)

    if len(jobs)==0:
        return Response({'message':f'No stats found for {topic}'})
    
    stats=jobs.aggregate(
        total_jobs=Count('title'),
        avg_position=Avg('position'),
        avg_salary = Avg('salary'),
        min_salary=Min('salary'),
        max_salary=Max('salary')
    )

    return Response(stats)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def applyToJob(request,pk):
    user=request.user
    job=get_object_or_404(Job,id=pk)
    if job.lastDate<timezone.now():
        return Response({'error':'You cannot apply to this job date is over'},status=status.HTTP_400_BAD_REQUEST)
    
    # candidate=get_object_or_404(CandidateApplied,user,job)
    alreadyApplied=job.candidateapplied_set.filter(user=user).exists()
    if alreadyApplied:
        return Response({'error':'You have already applied to this job'},status=status.HTTP_400_BAD_REQUEST)
    
    jobapplied=CandidateApplied.objects.create(job=job,user=user)

    return Response({
        'applied':True,
        'job_id':jobapplied.id
    },status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getappliedJob(request):
    user=request.user

    appliedJobs= CandidateApplied.objects.filter(user=user)
    serializer=CandidateAppliedSerializer(appliedJobs,many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isapplied(request,pk):
    user=request.user
    job_id=pk

    args={
        'user_id':user.id,
        'job_id':job_id
    }

    applied=CandidateApplied.objects.filter(**args)
    
    if len(applied)>0:
        return Response({'applied':True})
    else:
        return Response({'applied':False})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getJobCreated(request):
    user=request.user
    args={
        'user':user.id
    }
    job=Job.objects.filter(**args)
    serializer=JobSerializer(job,many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getcandidateApplied(request,pk):

    user=request.user
    job=get_object_or_404(Job,id=pk)

    if user!=job.user:
        return Response({'error':'You cannot access this Job'},status=status.HTTP_403_FORBIDDEN)
    
    candidates=Job.candidateapplied_set.all()
    serializer=CandidateAppliedSerializer(candidates,many=True)

    return Response(serializer.data)