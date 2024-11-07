from django.urls import path, include
from .views import Home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', Home.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]