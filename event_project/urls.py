from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Vous avez été déconnecté avec succès.')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Vous avez été déconnecté avec succès.')
        return super().post(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(
        next_page='/',
        template_name='registration/login.html'
    ), name='logout'),
    path('', include('events.urls')),
]