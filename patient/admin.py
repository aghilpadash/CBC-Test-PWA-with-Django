from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from csvexport.actions import csvexport
from .models import *


def published_fa(model):
    return datetime2jalali(model.published_at).strftime('%y/%m/%d , %H:%M:%S')


published_fa.short_description = 'زمان ثبت'


class PatientAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'gender', 'age', published_fa)
    ordering = ['id']


admin.site.register(Patient, PatientAdmin)


class CBCAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = (
        'id', 'age', 'gender', 'height', 'weight', 'WBC', 'RBC', 'Hemoglobin', 'Hematocrit', 'MCV', 'MCHC', 'RDWCV',
        'MPV', 'MCH', 'Platelets', published_fa)
    ordering = ['id']
    actions = [csvexport]


admin.site.register(CBC, CBCAdmin)


class ECGAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'person', 'ventRate', 'PR', 'Pms', 'QRSms', 'Tms', 'QTms', 'QTCms', 'Pdeg', 'QRSms', 'QRSdeg',
                    'Tdeg', 'RV1mv', 'SV5mv', 'RV5mv', 'SV1mv', published_fa]
    ordering = ['id']


admin.site.register(ECG, ECGAdmin)


class HeartAttackAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['id', 'ecg', 'probability', published_fa]
    ordering = ['id']


admin.site.register(HeartAttack, HeartAttackAdmin)
