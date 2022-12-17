from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     path('register/', user_views.register, name='register'),
#     path('login/',
#          auth_views.LoginView.as_view(template_name='users/login.html'),
#          name='login'),
#     path('logout/',
#          auth_views.LogoutView.as_view(template_name='users/logout.html'),
#          name='logout'),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('api/users/', user_views.register, name='add'),
    path('api/login/', user_views.register),
    path('api/logout/', user_views.register)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('', tutorials_views.index.as_view(), name='home'),
#     path('api/tutorials/', tutorials_views.tutorial_list),
#     path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
#     path('api/tutorials/published/', tutorials_views.tutorial_list_published)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
