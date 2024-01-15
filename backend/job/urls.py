from django.urls import path
from . import views

urlpatterns = [
    path('jobs/',views.getAllJobs,name='jobs'),
    path('jobs/<str:pk>/',views.getJob,name='job'),
    path('jobs/create/',views.createJob,name='CreateJob'),
    path('jobs/<str:pk>/update/',views.updateJob,name='UpdateJob'),
    path('jobs/<str:pk>/delete/',views.deleteJob,name='DeleteJob'),
    path('stats/<str:topic>/',views.getTopicStats,name='StatsJob'),
    path('jobs/<str:pk>/apply/',views.applyToJob,name='ApplyToJob'),
    path('me/jobs/appliedJob/',views.getappliedJob,name='getAppliedJob'),
    path('me/jobs/<str:pk>/applied/',views.isapplied,name='isApplied'),
    path('me/jobs/',views.getJobCreated,name='CurrentUserJob'),
    path('jobs/<str:pk>/candidates/',views.getcandidateApplied,name='CandidateApplied')
]