from .models import Envoies_data
from rest_framework import serializers
from django.contrib.auth.models import User



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','email','is_superuser','last_login','date_joined')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],validated_data['is_superuser'])

        return user
    
# Envoies_data Serializer
class Envoies_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envoies_data
        fields = ('id', 'nom_expediteur','prenom_expediteur','adresse_expediteur','email_expediteur','numero_expediteur','pays_expediteur',
                  'nom_beneficiaire','prenom_beneficiaire','pays_beneficiaire',
                 'montant_beneficiaire','type_service','frais_envoie','frais_tva','montant_total','code_retrait','data_operation','date_heure_operation','code_abonne','status_retrait','numero_transfer','month_year_operation',
                  'agent_id')




        
