from rest_framework.views import exception_handler

def custom_exception_handler(exec,context):

    respone=exception_handler(exec,context)

    exception_class=exec.__class__.__name__

    print(exception_class)
    if exception_class=='AuthenticationFailed':
        respone.data={
            'error':"Invalid Email or Password"
        }
    elif exception_class=='NotAuthenticated':
        respone.data={
            'error':"Login first to access the resource"
        }
    elif exception_class=='InvalidToken':
        respone.data={
            'error':"Your authentication token is expired"
        }

    return respone