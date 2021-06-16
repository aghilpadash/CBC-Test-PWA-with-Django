from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

GENDER_CHOICES = [
    ('مرد', 'مرد'),
    ('زن', 'زن'),
]
PROBABILITY_CHOICES = [
    ('احتمال حمله قلبی بالاست', 'احتمال حمله قلبی بالاست'),
    ('احتمال حمله قلبی پایین است', 'احتمال حمله قلبی پایین است'),
]


class Patient(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ردیف")
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name="نام و نام خانوادگی")
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name="جنسیت")
    age = models.IntegerField(null=False, blank=False, verbose_name="سن")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "بیمار"
        verbose_name_plural = 'بیماران'


class ECG(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ردیف")
    person = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="نام بیمار")
    ventRate = models.IntegerField(null=False, blank=False)
    PR = models.IntegerField(null=False, blank=False)
    Pms = models.IntegerField(null=False, blank=False)
    QRSms = models.IntegerField(null=False, blank=False)
    Tms = models.IntegerField(null=False, blank=False)
    QTms = models.IntegerField(null=False, blank=False)
    QTCms = models.IntegerField(null=False, blank=False)
    Pdeg = models.IntegerField(null=False, blank=False)
    QRSdeg = models.IntegerField(null=False, blank=False)
    Tdeg = models.IntegerField(null=False, blank=False)
    RV1mv = models.FloatField(null=False, blank=False)
    SV5mv = models.FloatField(null=False, blank=False)
    RV5mv = models.FloatField(null=False, blank=False)
    SV1mv = models.FloatField(null=False, blank=False)
    published_at = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = "نتیجه ECG"
        verbose_name_plural = 'نتایج ECG'


class CBC(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ردیف")
    age = models.IntegerField(null=False, blank=False, verbose_name="سن")
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name="جنسیت")
    height = models.IntegerField(null=False, blank=False, verbose_name="قد")
    weight = models.IntegerField(null=False, blank=False, verbose_name="وزن")
    WBC = models.FloatField(null=False, blank=False)
    RBC = models.FloatField(null=False, blank=False)
    Hemoglobin = models.FloatField(null=False, blank=False)
    Hematocrit = models.FloatField(null=False, blank=False)
    MCV = models.FloatField(null=False, blank=False)
    MPV = models.FloatField(null=False, blank=False)
    MCH = models.FloatField(null=False, blank=False)
    MCHC = models.FloatField(null=False, blank=False)
    RDWCV = models.FloatField(null=False, blank=False)
    Platelets = models.FloatField(null=False, blank=False)
    published_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ثبت")
    created_at = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name = "آزمایش CBC"
        verbose_name_plural = 'آزمایش CBC'


class HeartAttack(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ردیف")
    ecg = models.ForeignKey(ECG, on_delete=models.CASCADE, verbose_name="نام بیمار")
    probability = models.CharField(max_length=128, choices=PROBABILITY_CHOICES, verbose_name="تشخیص حمله قلبی")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created_at = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name = "احتمال حمله قلبی"
        verbose_name_plural = 'تشخیص حمله قلبی'
