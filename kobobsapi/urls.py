from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI
from .import views

urlpatterns = [
    path('',views.welcom, name='welcom'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/envoieFormulaire/',views.envoieFormulaire,name='envoieFormulaire'),
    path('api/envoieFormulaireAbonne/',views.envoieFormulaireAbonne,name='envoieFormulaireAbonne'),
    path('api/getRetraitInfo/<int:pk>/',views.getRetraitInfo,name='getRetraitInfo'),
    path('api/getRetraitNonValideInfo/<str:pk>/',views.getRetraitNonValideInfo,name='getRetraitNonValideInfo'),
    path('api/validateCodeRetrait/<int:pk>/',views.validateCodeRetrait,name='validateCodeRetrait'),
    path('api/payerCodeRetrait/<int:pk>/',views.payerCodeRetrait,name='payerCodeRetrait'),
    path('api/getCodeAbonneInfo/<int:pk>/',views.getCodeAbonneInfo,name='getCodeAbonneInfo'),
    path('api/getAbonneInfo/<str:pk>/',views.getAbonneInfo,name='getAbonneInfo'),
    path('api/getDailyRapportInfo/<str:pk>/',views.getDailyRapportInfo,name='getDailyRapportInfo'),
    path('api/getMonthlyRapportInfo/<str:pk>/',views.getMonthlyRapportInfo,name='getMonthlyRapportInfo'),
    path('api/getUsersInfo/',views.getUsersInfo,name='getUsersInfo'),
    path('api/suprimer/<int:pk>/',views.suprimer,name='suprimer'),
    path('api/getCodeRetraitInfo/<str:pk>/<str:pk2>/<str:pk3>/',views.getCodeRetraitInfo,name='getCodeRetraitInfo')
]

urlpatterns = format_suffix_patterns(urlpatterns)