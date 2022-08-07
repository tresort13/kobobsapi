from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Envoies_data(models.Model):
    nom_expediteur = models.CharField(max_length=100,default="")
    postnom_expediteur = models.CharField(max_length=100,default="")
    prenom_expediteur = models.CharField(max_length=100,default="")
    email_expediteur = models.CharField(max_length=100,default="")
    numero_expediteur = models.CharField(max_length=100,default="")
    pays_expediteur = models.CharField(max_length=100,default="")
    nom_beneficiaire = models.CharField(max_length=100,default="")
    postnom_beneficiaire = models.CharField(max_length=100,default="")
    prenom_beneficiaire = models.CharField(max_length=100,default="")
    adresse_beneficiare = models.CharField(max_length=100,default="")
    numero_beneficiaire = models.CharField(max_length=100,default="")
    pays_beneficiaire = models.CharField(max_length=100,default="")
    montant_envoie = models.DecimalField(max_digits=15, decimal_places=2)  
    frais_envoie = models.DecimalField(max_digits=15,decimal_places=2)
    montant_total = models.DecimalField(max_digits=15,decimal_places=2)
    code_retrait = models.CharField(max_length=8,null=True,unique=True)
    data_operation = models.DateField(auto_now_add=True)
    date_heure_operation =models.DateTimeField(auto_now_add=True)
    code_abonne = models.CharField(max_length=5, null=True,unique=True)
    status_retrait = models.CharField(max_length=30,default="retrait en attente")
    agent_id = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    