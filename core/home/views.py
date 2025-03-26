from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import Student
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache
import requests
import time
from .models import RequestLog 

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'login.html')

@api_view(['GET','POST'])
def get_student(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    return Response({'status' : 200, 'payload' : serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)

    if not serializer.is_valid():
        return Response({'status' : 400, 'payload' : serializer.errors, 'message' : 'Invalid data'})
    serializer.save()


    return Response({'status' : 200, 'payload' : data, 'message' : 'Data received'})


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status' : 200, 'payload' : serializer.data})
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status' : 400, 'payload' : serializer.errors, 'message' : 'Invalid data'})
        serializer.save()
        return Response({'status' : 200, 'payload' : serializer.data, 'message' : 'Data received'})



class registeruser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':400,'payload':serializer.errors,'message':'Invalid data'})
        
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload': serializer.data,'token': str(token_obj) , 'message':'Data received'})
        

#proxy_server
#rate limiting

# RATE_LIMIT = 5  # Max requests
# TIME_WINDOW = 60  # In seconds (1 min)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def proxy_view(request):
#     user = request.user
#     key = f'rate-limit-{user.id}'
#     current_count = cache.get(key, 0)

#     if current_count >= RATE_LIMIT:
#         return Response({'status': 429, 'message': 'Rate limit exceeded. Try again later.'}, status=429)

#     # Increment count
#     cache.set(key, current_count + 1, timeout=TIME_WINDOW)

#     # Forward the request
#     backend_url = 'http://localhost:8000/studentdata'  # or any other backend
#     response = requests.request(
#         method=request.method,
#         url=backend_url,
#         headers={"Content-Type": "application/json"},
#         params=request.query_params,
#         data=request.body
#     )

#     return Response(response.json(), status=response.status_code)
RATE_LIMIT = 5   # requests
TIME_WINDOW = 60  # seconds

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def proxy_view(request):
    user = request.user
    cache_key = f"rate-limit-{user.id}"
    current_count = cache.get(cache_key, 0)

    # Rate Limiting check
    if current_count >= RATE_LIMIT:
        # Log rate limit hit
        RequestLog.objects.create(
            user=user,
            endpoint='/proxy/',
            status_code=429
        )
        return Response({'status': 429, 'message': 'Rate limit exceeded. Try again later.'}, status=429)

    # Update rate limit counter
    cache.set(cache_key, current_count + 1, timeout=TIME_WINDOW)

    # Forwarding the request to backend (your actual API or student data)
    backend_url = 'http://localhost:8000/studentdata'  # Change if needed
    start_time = time.time()

    try:
        backend_response = requests.request(
            method=request.method,
            url=backend_url,
            headers={"Content-Type": "application/json"},
            params=request.query_params,
            data=request.body
        )
    except Exception as e:
        # Log failure
        RequestLog.objects.create(
            user=user,
            endpoint=backend_url,
            status_code=500
        )
        return Response({'status': 500, 'message': 'Backend server error'}, status=500)

    end_time = time.time()
    response_time = round(end_time - start_time, 3)
    print("User:", request.user)
    print("Logging request...")
    # Logging the request
    RequestLog.objects.create(
        user=user,
        endpoint=backend_url,
        status_code=backend_response.status_code,
        response_time=response_time
    )

    return Response(backend_response.json(), status=backend_response.status_code)