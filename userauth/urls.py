from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
from django.urls import path
from .views import (RegistrationAPIView, 
                    VerifyEmailAPIView, 
                    ResendVerifyEmailAPIView, 
                    UserAPIView,
                    UserLoginAPIView,
                    UserLogoutAPIView,
                    PasswordResetAPIView,
                    PasswordResetConfirmAPIView
                    )

urlpatterns = [
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegistrationAPIView.as_view(), name='register'),
    path('user/verify-email/', VerifyEmailAPIView.as_view(), name='verify_email'),
    path('user/resend-verify-email/', ResendVerifyEmailAPIView.as_view(), name='resend_verify_email'),
    path('user/reset-password/', PasswordResetAPIView.as_view(), name='reset_password'),
    path('user/reset-password-confirm/', PasswordResetConfirmAPIView.as_view(), name='reset_password_confirm'),
    path('user/login/', UserLoginAPIView.as_view(), name='login'),
    path('user/logout/', UserLogoutAPIView.as_view()),
    path('user/me', UserAPIView.as_view(), name='user'),

]