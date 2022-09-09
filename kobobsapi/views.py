from functools import partial
from pickle import PUT
from django.http import HttpResponse
from .models import Envoies_data
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import Envoies_dataSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
import re
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import random
from datetime import datetime
from django.contrib.auth.models import User





class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"username" : user.username})

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
def welcom(request):
    return HttpResponse('WELCOM TO KOBO BUSINESS  API RESOURCES')

@api_view(['POST'])   
def envoieFormulaire(request): 
        nom_expediteur= request.data['nom_expediteur']
        postnom_expediteur= request.data['postnom_expediteur']
        prenom_expediteur= request.data['prenom_expediteur']
        adresse_expediteur= request.data['adresse_expediteur']
        email_expediteur= request.data['email_expediteur']
        numero_expediteur = request.data['numero_expediteur']
        pays_expediteur= request.data['pays_expediteur']
        nom_beneficiaire= request.data['nom_beneficiaire']
        postnom_beneficiaire= request.data['postnom_beneficiaire']
        prenom_beneficiaire= request.data['prenom_beneficiaire']
        adresse_beneficiaire= request.data['adresse_beneficiaire']
        numero_beneficiaire= request.data['numero_beneficiaire']
        pays_beneficiaire= request.data['pays_beneficiaire']
        montant_beneficiaire= request.data['montant_beneficiaire']
        montant_envoie = request.data['montant_pour_payer']
        frais_envoie = request.data['frais_envoie']
        frais_tva = request.data['frais_tva']
        type_service= request.data['type_service']
        
        retrait_donnes1 = [23244562,39430944,18034851,34890346,45860984,23409858,23849384,12435646,54677540,65467383]
        key_one = random.sample(retrait_donnes1,k=1)
        for x in key_one :
            a = int(x)
        retrait_donnes2 = [13456645,23456732,34985788,12938465,13746783,29384784,12837482,32657386,29837431,12337452,24357891,10236436,32657382]
        key_two = random.sample(retrait_donnes2,k=1)
        for z in key_two :
            b= int(z)

        retrait_donnes3 = [23,56,48,96,12,65,85,29,45,70,25,31,41,71,91]
        key_three = random.sample(retrait_donnes3,k=1)
        for x in key_three :
            c = int(x)
        retrait_donnes4 = [36,60,50,21,27,86,95,38,92,45,87,23,78,99,55,22,14,33,78]
        key_four = random.sample(retrait_donnes4,k=1)
        for z in key_four :
            d= int(z)
        code_retrait = a+b+c+d
        
        
        code_abonne_donnes1 =  [13452,23456,34985,12938,13746,29384,12837,32657,29837,12337,24357,10236,32657]
        key_one = random.sample(code_abonne_donnes1,k=1)
        for x in key_one :
            e = int(x)
        code_abonne_donnes2 = [23244,39430,18034,34890,45860,23409,23849,12435,54677,35467]
        key_two = random.sample(code_abonne_donnes2,k=1)
        for z in key_two :
            f= int(z)

        code_abonne_donnes3= [23,56,48,96,12,65,85,29,45,70,25,31,41,71,91]
        key_three = random.sample(code_abonne_donnes3,k=1)
        for x in key_three :
            g = int(x)
        code_abonne_donnes4 = [36,60,50,21,27,86,95,38,92,45,87,23,78,99,55,22,14,33,78]
        key_four = random.sample(code_abonne_donnes4,k=1)
        for z in key_four :
            h= int(z)
            
        code_abonne = e+f+g+h
        
        montant_envoi_convert = montant_envoie
        
        
        
        montant_total = float(montant_envoi_convert)
        
        frais_envoie = frais_envoie
        
        frais_tva = frais_tva
        
        
        serializer = Envoies_dataSerializer(data={'nom_expediteur': nom_expediteur,'postnom_expediteur':postnom_expediteur,'prenom_expediteur' : prenom_expediteur,'adresse_expediteur' : adresse_expediteur,'email_expediteur' : email_expediteur,'numero_expediteur' : numero_expediteur,'pays_expediteur' : pays_expediteur,'nom_beneficiaire' : nom_beneficiaire,'postnom_beneficiaire' : postnom_beneficiaire,'prenom_beneficiaire' : prenom_beneficiaire,'adresse_beneficiaire' : adresse_beneficiaire,'numero_beneficiaire' : numero_beneficiaire,'pays_beneficiaire' : pays_beneficiaire,'montant_beneficiaire':montant_beneficiaire,'type_service' : type_service, 'frais_envoie' : frais_envoie,'frais_tva':frais_tva,'montant_total': montant_total,'code_retrait':code_retrait,'code_abonne' : code_abonne,'month_year_operation':str(datetime.now().year)+"-"+"0"+str(datetime.now().month)})
        if serializer.is_valid() :
          serializer.save()
          return Response(serializer.data)
        return Response('',status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])   
def envoieFormulaireAbonne(request): 
        nom_expediteur= request.data['nom_expediteur']
        postnom_expediteur= request.data['postnom_expediteur']
        prenom_expediteur= request.data['prenom_expediteur']
        adresse_expediteur= request.data['adresse_expediteur']
        email_expediteur= request.data['email_expediteur']
        numero_expediteur = request.data['numero_expediteur']
        pays_expediteur= request.data['pays_expediteur']
        nom_beneficiaire= request.data['nom_beneficiaire']
        postnom_beneficiaire= request.data['postnom_beneficiaire']
        prenom_beneficiaire= request.data['prenom_beneficiaire']
        adresse_beneficiaire= request.data['adresse_beneficiaire']
        numero_beneficiaire= request.data['numero_beneficiaire']
        pays_beneficiaire= request.data['pays_beneficiaire']
        montant_beneficiaire = request.data['montant_beneficiaire']
        montant_envoie = request.data['montant_pour_payer']
        frais_envoie = request.data['frais_envoie']
        frais_tva = request.data['frais_tva']
        type_service= request.data['type_service']
        code_abonne= request.data['code_abonne']
        
        
        retrait_donnes1 = [23244562,39430944,18034851,34890346,45860984,23409858,23849384,12435646,54677540,65467383]
        key_one = random.sample(retrait_donnes1,k=1)
        for x in key_one :
            a = int(x)
        retrait_donnes2 = [13456645,23456732,34985788,12938465,13746783,29384784,12837482,32657386,29837431,12337452,24357891,10236436,32657382]
        key_two = random.sample(retrait_donnes2,k=1)
        for z in key_two :
            b= int(z)

        retrait_donnes3 = [23,56,48,96,12,65,85,29,45,70,25,31,41,71,91]
        key_three = random.sample(retrait_donnes3,k=1)
        for x in key_three :
            c = int(x)
        retrait_donnes4 = [36,60,50,21,27,86,95,38,92,45,87,23,78,99,55,22,14,33,78]
        key_four = random.sample(retrait_donnes4,k=1)
        for z in key_four :
            d= int(z)
        code_retrait = a+b+c+d
        
        
       
        
        montant_envoi_convert = montant_envoie
         
        montant_total = float(montant_envoi_convert)
        
        frais_envoie = frais_envoie
        
        frais_tva = frais_tva
        
        
        serializer = Envoies_dataSerializer(data={'nom_expediteur': nom_expediteur,'postnom_expediteur':postnom_expediteur,'prenom_expediteur' : prenom_expediteur,'adresse_expediteur' : adresse_expediteur,'email_expediteur' : email_expediteur,'numero_expediteur' : numero_expediteur,'pays_expediteur' : pays_expediteur,'nom_beneficiaire' : nom_beneficiaire,'postnom_beneficiaire' : postnom_beneficiaire,'prenom_beneficiaire' : prenom_beneficiaire,'adresse_beneficiaire' : adresse_beneficiaire,'numero_beneficiaire' : numero_beneficiaire,'pays_beneficiaire' : pays_beneficiaire,'montant_beneficiaire':montant_beneficiaire,'type_service' : type_service, 'frais_envoie' : frais_envoie,'frais_tva':frais_tva,'montant_total': montant_total,'code_abonne':code_abonne,'code_retrait':code_retrait,'month_year_operation':str(datetime.now().year)+"-"+"0"+str(datetime.now().month)})
        if serializer.is_valid() :
          serializer.save()
          return Response(serializer.data)
        return Response('',status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])   
def getRetraitInfo(request,pk): 
    code_retrait = pk
    try:
        envoies_data = Envoies_data.objects.filter(code_retrait=code_retrait)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
        
        
@api_view(['GET'])   
def getRetraitNonValideInfo(request,pk): 
    status_retrait = str(pk)
    try:
        envoies_data = Envoies_data.objects.filter(status_retrait=status_retrait)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
        
        

@api_view(['PUT'])   
def validateCodeRetrait(request,pk): 
    code_retrait = pk
    try:
        envoies_data = Envoies_data.objects.get(code_retrait=code_retrait)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='PUT':
            serializer = Envoies_dataSerializer(envoies_data,data={'status_retrait':'Code Retrait Valide'},partial=True)
            if serializer.is_valid() :
              serializer.save()
              return Response(serializer.data)
            return Response('',status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT'])   
def payerCodeRetrait(request,pk): 
    code_retrait = pk
    try:
        envoies_data = Envoies_data.objects.get(code_retrait=code_retrait)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='PUT':
            serializer = Envoies_dataSerializer(envoies_data,data={'status_retrait':'Code Retrait Payé'},partial=True)
            if serializer.is_valid() :
              serializer.save()
              return Response(serializer.data)
            return Response('',status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET'])   
def getCodeAbonneInfo(request,pk): 
    code_abonne = pk
    try:
        envoies_data = Envoies_data.objects.filter(code_abonne=code_abonne)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
@api_view(['GET'])   
def getAbonneInfo(request,pk): 
    numero_expediteur = pk
    try:
        envoies_data = Envoies_data.objects.filter(numero_expediteur=numero_expediteur) | Envoies_data.objects.filter(code_abonne=numero_expediteur) 
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
        

@api_view(['GET'])   
def getDailyRapportInfo(request,pk): 
    data_operation = pk
    try:
        envoies_data = Envoies_data.objects.filter(data_operation=data_operation)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
@api_view(['GET'])   
def getMonthlyRapportInfo(request,pk): 
    month_year_operation = pk
    try:
        envoies_data = Envoies_data.objects.filter(month_year_operation=month_year_operation)
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = Envoies_dataSerializer(envoies_data,many=True)
            return Response(serializer.data)
        
@api_view(['GET'])   
def getUsersInfo(request): 
    try:
        envoies_data = User.objects.all()
    except envoies_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method =='GET':
            serializer = UserSerializer(envoies_data,many=True)
            return Response(envoies_data)





