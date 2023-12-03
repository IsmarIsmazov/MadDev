from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.users.views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view({'post': 'create'}), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

]