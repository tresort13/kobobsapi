from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Envoies_data(models.Model):
    nom_expediteur = models.CharField(max_length=100,default="")
    postnom_expediteur = models.CharField(max_length=100,default="")
    prenom_expediteur = models.CharField(max_length=100,default="")
    adresse_expediteur = models.CharField(max_length=100,default="")
    email_expediteur = models.CharField(max_length=100,default="")
    numero_expediteur = models.CharField(max_length=100,default="")
    pays_expediteur = models.CharField(max_length=100,default="")
    nom_beneficiaire = models.CharField(max_length=100,default="")
    postnom_beneficiaire = models.CharField(max_length=100,default="")
    prenom_beneficiaire = models.CharField(max_length=100,default="")
    pays_beneficiaire = models.CharField(max_length=100,default="")
    montant_beneficiaire = models.DecimalField(max_digits=15, decimal_places=2,default=0.00)
    type_service = models.CharField(max_length=100,default="")  
    frais_envoie = models.DecimalField(max_digits=15,decimal_places=2)
    frais_tva = models.DecimalField(max_digits=15,decimal_places=2,default=0.00)  
    montant_total = models.DecimalField(max_digits=15,decimal_places=2)
    code_retrait = models.CharField(max_length=8,null=True,unique=True)
    data_operation = models.DateField(auto_now_add=True)
    date_heure_operation =models.DateTimeField(auto_now_add=True)
    code_abonne = models.CharField(max_length=5, null=True)
    status_retrait = models.CharField(max_length=50,default="code retrait en attente de validation")
    numero_transfer = models.CharField(max_length=50,default="")
    month_year_operation = models.CharField(max_length=10,default="") 
    agent_id = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    
    