from django.http import JsonResponse

def handler500(request):
    message='Internal server Error'
    response=JsonResponse(data={'error':message})
    response.status_code=500
    return response

def handler404(request,exception):
    message='Route not Found'
    response=JsonResponse(data={'error':message})
    response.status_code=404
    return response