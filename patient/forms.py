from django import forms
from . import models

GENDER_CHOICES = [
    ('مرد', 'مرد'),
    ('زن', 'زن'),
]


# class CBCForm(forms.Form):
#     age = forms.IntegerField()
#     gender = forms.ChoiceField()
#     height = forms.IntegerField()
#     weight = forms.IntegerField()
#     WBC = forms.FloatField()
#     RBC = forms.FloatField()
#     Hemoglobin = forms.FloatField()
#     Hematocrit = forms.FloatField()
#     MCV = forms.FloatField()
#     MPV = forms.FloatField()
#     MCH = forms.FloatField()
#     MCHC = forms.FloatField()
#     RDWCV = forms.FloatField()
#     Platelets = forms.FloatField()
#
# class CBCForm(forms.ModelForm):
#     class Meta:
#         model = models.CBC
#         fields = ['age', 'gender', 'height', 'weight', 'WBC', 'RBC', 'Hemoglobin', 'Hematocrit', 'MCV', 'MPV', 'MCH',
#                   'MCHC', 'RDWCV', 'Platelets']

class CBCForm(forms.Form):
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'سال',
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')",
                   'style': "border-color: #adadad"}),
        label="سن")
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "text-center",
                                                          'style': "border-color: #adadad"}), choices=GENDER_CHOICES,
                               label="جنسیت")
    height = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'سانتی متر',
                   'style': "border-color: #adadad",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}), label="قد")
    weight = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'کیلوگرم',
                   'style': "border-color: #adadad",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}),
        label="وزن")
    WBC = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*',
                   'placeholder': 'گلبول های سفید',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    RBC = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'گلبول های قرمز',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    Hemoglobin = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'هموگلوبین',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    Hematocrit = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*',
                   'placeholder': 'درصد گلبول های قرمز در خون',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    MCV = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'حجم متوسط هموگلوبین',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    MPV = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'حجم متوسط پلاکت ها',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    MCH = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'وزن متوسط هموگلوبین',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    MCHC = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'غلظت متوسط همو گلوبین',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    RDWCV = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*',
                   'placeholder': 'پهنای گلبول قرمز در منحنی',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
    Platelets = forms.FloatField(
        widget=forms.TextInput(
            attrs={'class': 'text-center', 'type': 'number', 'pattern': '\d*', 'placeholder': 'پلاکت ها',
                   'style': "border-color: #adadad", 'step': "any",
                   'oninvalid': "this.setCustomValidity('لطفا فیلد خالی را تکمیل کنید')"}))
