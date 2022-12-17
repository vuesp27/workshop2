from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader


from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
User = get_user_model()


# def register(request):
#     next = request.GET.get('next', '/')
#     try:
#         username = request.POST['username']
#         password = request.POST['password']
#         auth_user = authenticate(request, username=username, password=password)
#         try:
#             login(request, auth_user)
#             return HttpResponseRedirect(next)
#         except:
#             messages.error(request, 'Invalid credentials')
#             return HttpResponseRedirect(next)
#     except (KeyError):
#         messages.error(request, 'Invalid credentials')
#         # return render(request, '/', { 'message': "Invalid username or password. Please try again." })


@api_view(['GET', 'POST', 'DELETE'])
def register(request):
    if request.method == 'GET':
        users = User.objects.all()

        user = request.GET.get('username', None)
        if user is not None:
            users = users.filter(name__icontains=user)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Users were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         email = request.POST['email']

#         print("----------------- register called")
#         print(username)
#         print(password)
#         print(firstname)
#         print(lastname)
#         print(email)

#         # try:
#         #     user = get_object_or_404(User, username=username)
#         # except:
#         #     pass

#         messages.success(request,
#                          f'Your account has been created! You can now login!')
#         return redirect('login')
#     else:
#         return render(request, 'users/register.html')
