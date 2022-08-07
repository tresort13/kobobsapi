from .models import Envoies_data
from rest_framework import serializers
from django.contrib.auth.models import User



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
# Envoies_data Serializer
class Envoies_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envoies_data
        fields = ('id', 'nom_expediteur','postnom_expediteur','prenom_expediteur','email_expediteur','numero_expediteur','pays_expediteur',
                  'nom_beneficiare','postnom_beneficiare','prenom_beneficiare','adresse_beneficiare','numero_beneficiare','pays_beneficiare',
                  'montant_envoie','frais_envoie','montant_total','code_retrait','data_operation','date_heure_operation','code_abonne','status_retrait',
                  'agent_id')




        
