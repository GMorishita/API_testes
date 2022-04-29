from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios import views


urlpatterns = [
    path('const_usuarios/', views.ConstUsuarios.as_view()),
    path('const_1_usuario/<int:pk>/', views.Const1Usuario.as_view()),
    path('delete_usuario/<int:pk>', views.DeleteUsuario.as_view()),
    path('criar_usuario/', views.CriarUsuario.as_view()),
    path('update_usuario/', views.UpdateUsuario.as_view()),
    path('obter_token/', TokenObtainPairView.as_view()),
    path('refresh_token/', TokenRefreshView.as_view()),
]
