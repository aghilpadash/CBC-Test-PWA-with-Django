from rest_framework import serializers
from patient.models import Patient, ECG, HeartAttack, CBC


class SubmitEcgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG
        fields = "__all__"


class SubmitCBCSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBC
        fields = "__all__"


class SubmitHeartAttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG
        fields = "__all__"


class SubmitPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
