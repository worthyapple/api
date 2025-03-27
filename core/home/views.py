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
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count
from .models import APILog

from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count
from .models import APILog  # Ensure this model exists
from django.http import JsonResponse
from .models import APILog
from django.core.serializers import serialize

def api_logs(request):
    logs = APILog.objects.all().order_by('-timestamp')[:10]
    data = serialize('json', logs)
    return JsonResponse(data, safe=False)
import random
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import APILog

rate_limit = 5  # Max requests per user
time_window = 60  # In seconds (1 min)

import random
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count
from rest_framework.decorators import api_view
from .models import APILog

rate_limit = 5  # Max requests per user
time_window = 60  # In seconds (1 min)

@api_view(['GET'])
def logs(request):
    total_requests = random.randint(1, 50)
    active_users = random.randint(1, 50)
    requests_made = random.randint(1, 50)
    remaining_requests = max(0, RATE_LIMIT - requests_made)
    time_until_reset = random.randint(1, 50)

    most_used_endpoints = [
        {'endpoint': '/api/student', 'count': random.randint(1, 50)},
        {'endpoint': '/api/login', 'count': random.randint(1, 50)},
        {'endpoint': '/api/data', 'count': random.randint(1, 50)}
    ]

    recent_logs = [
        {'user__username': 'User1', 'endpoint': '/api/student', 'status_code': 200, 'timestamp': '2025-03-26 12:00:00'},
        {'user__username': 'User2', 'endpoint': '/api/login', 'status_code': 401, 'timestamp': '2025-03-26 12:05:00'},
        {'user__username': 'User3', 'endpoint': '/api/data', 'status_code': 403, 'timestamp': '2025-03-26 12:10:00'}
    ]

    params = {
        'total_requests': total_requests,
        'rate_limit': RATE_LIMIT,
        'requests_made': requests_made,
        'remaining_requests': remaining_requests,
        'time_until_reset': time_until_reset,
        'active_users': active_users,
        'most_used_endpoints': most_used_endpoints,
        'recent_logs': recent_logs,
    }

    print("Dashboard Params:", params)  # Debugging print statement
    return render(request, 'logs.html', params)


@api_view(['GET'])
def dashboard(request):
    """Fetch API dashboard stats with randomized values for frontend visualization."""
    total_requests = random.randint(1, 10)  # Randomized

    # Count requests made in the last hour
    recent_time = now() - timedelta(hours=1)
    requests_made = random.randint(1, 10)  # Randomized
    remaining_requests = max(rate_limit - requests_made, 0)

    # Calculate correct countdown for rate limit reset
    current_time = now()
    next_reset = current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    if next_reset < current_time:
        next_reset += timedelta(hours=1)

    time_until_reset = (next_reset - current_time).total_seconds()

    # Fetch active users
    active_users = random.randint(1, 5)  # Randomized

    # Most used endpoints (Randomized counts)
    most_used_endpoints = [
        {"endpoint": "/api/data1/", "count": random.randint(1, 10)},
        {"endpoint": "/api/data2/", "count": random.randint(1, 10)},
        {"endpoint": "/api/data3/", "count": random.randint(1, 10)},
    ]

    # Recent API logs (Randomized)
    recent_logs = [
        {"user": f"user{random.randint(1, 10)}", "endpoint": "/api/random/", "status": 200}
        for _ in range(10)
    ]

    context = {
        "total_requests": total_requests,
        "rate_limit": rate_limit,
        "time_window": time_window,
        "requests_made": requests_made,
        "remaining_requests": remaining_requests,
        "time_until_reset": int(time_until_reset),
        "active_users": active_users,
        "most_used_endpoints": most_used_endpoints,
        "recent_logs": recent_logs,
    }

    return render(request, "dashboard.html", context)

# rate_limit = 5  # Example limit
# time_window = 60  # Example window


# @api_view(['GET'])
# def logs(request):
#     # Fetch total API requests
#     total_requests = APILog.objects.count()
    
   
    
#     # Count requests made in the last hour
#     recent_time = now() - timedelta(hours=1)
#     requests_made = APILog.objects.filter(timestamp__gte=recent_time).count()
#     remaining_requests = max(rate_limit - requests_made, 0)
    
#     # Calculate time until reset (assuming reset happens every hour)
#     current_time = now()
#     next_reset = (current_time + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
#     time_until_reset = (next_reset - current_time).seconds  # Time in seconds until next reset

#     # Fetch active users (distinct users making API calls)
#     active_users = APILog.objects.values("user").distinct().count()
    
#     # Most used endpoints
#     most_used_endpoints = APILog.objects.values("endpoint").annotate(count=Count("endpoint")).order_by("-count")[:5]

#     # Recent API logs
#     recent_logs = APILog.objects.all().order_by("-timestamp")[:10]

#     context = {
#         "total_requests": total_requests,
#         "rate_limit": rate_limit,
#         "TIME_WINDOW": time_window,
#         "requests_made": requests_made,
#         "remaining_requests": remaining_requests,
#         "time_until_reset": time_until_reset,  # Reintroduced
#         "active_users": active_users,
#         "most_used_endpoints": most_used_endpoints,
#         "recent_logs": recent_logs,
#     }
    
#     return render(request, "logs.html", context)

# from django.shortcuts import render
# from django.utils.timezone import now
# from datetime import timedelta
# from django.db.models import Count
# from .models import APILog

# rate_limit = 5  # Max requests
# time_window = 60  # In seconds (1 min)

# @api_view(['GET'])
# def dashboard(request):
#     # Fetch total API requests
#     total_requests = APILog.objects.count()

#     # Count requests made in the last hour
#     recent_time = now() - timedelta(hours=1)
#     requests_made = APILog.objects.filter(timestamp__gte=recent_time).count()
#     remaining_requests = max(rate_limit - requests_made, 0)

#     # Calculate correct countdown for rate limit reset
#     current_time = now()
#     next_reset = current_time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
#     if next_reset < current_time:
#         next_reset += timedelta(hours=1)

#     time_until_reset = (next_reset - current_time).total_seconds()

#     # Fetch active users (distinct users making API calls)
#     active_users = APILog.objects.values("user").distinct().count()

#     # Most used endpoints
#     most_used_endpoints = (
#         APILog.objects.values("endpoint")
#         .annotate(count=Count("endpoint"))
#         .order_by("-count")[:5]
#     )

#     # Recent API logs
#     recent_logs = APILog.objects.all().order_by("-timestamp")[:10]

#     context = {
#         "total_requests": total_requests,
#         "rate_limit": rate_limit,
#         "time_window": time_window,
#         "requests_made": requests_made,
#         "remaining_requests": remaining_requests,
#         "time_until_reset": int(time_until_reset),  # Convert to integer for frontend display
#         "active_users": active_users,
#         "most_used_endpoints": most_used_endpoints,
#         "recent_logs": recent_logs,
#     }

#     return render(request, "dashboard.html", context)
# @api_view(['GET'])
# def dashboard(request):
#     # Fetch total API requests
#     total_requests = APILog.objects.count()
    
   
    
#     # Count requests made in the last hour
#     recent_time = now() - timedelta(hours=1)
#     requests_made = APILog.objects.filter(timestamp__gte=recent_time).count()
#     remaining_requests = max(rate_limit - requests_made, 0)
    
#     # Calculate time until reset (assuming reset happens every hour)
#     current_time = now()
#     next_reset = (current_time + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
#     time_until_reset = (next_reset - current_time).seconds  # Time in seconds until next reset

#     # Fetch active users (distinct users making API calls)
#     active_users = APILog.objects.values("user").distinct().count()
    
#     # Most used endpoints
#     most_used_endpoints = APILog.objects.values("endpoint").annotate(count=Count("endpoint")).order_by("-count")[:5]

#     # Recent API logs
#     recent_logs = APILog.objects.all().order_by("-timestamp")[:10]

#     context = {
#         "total_requests": total_requests,
#         "rate_limit": rate_limit,
#         "TIME_WINDOW": time_window,
#         "requests_made": requests_made,
#         "remaining_requests": remaining_requests,
#         "time_until_reset": time_until_reset,  # Reintroduced
#         "active_users": active_users,
#         "most_used_endpoints": most_used_endpoints,
#         "recent_logs": recent_logs,
#     }
    
#     return render(request, "dashboard.html", context)


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
