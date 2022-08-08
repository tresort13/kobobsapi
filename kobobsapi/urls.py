from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,EnvoieFormulaire
from .import views

urlpatterns = [
    path('',views.welcom, name='welcom'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/envoieFormulaire/',EnvoieFormulaire.as_view(),name='envoieFormulaire')   
]

urlpatterns = format_suffix_patterns(urlpatterns)