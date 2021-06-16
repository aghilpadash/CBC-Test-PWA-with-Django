from django.core.paginator import Paginator
from django.forms import forms
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from . import models
from . import forms
from .forms import CBCForm
from .models import Patient
from .models import CBC


def index(request):
    patients = Patient.objects.all()
    paginator = Paginator(patients, 7)

    page_number = request.GET.get('page', )
    page_obj = paginator.get_page(page_number)

    context = {
        'patients': page_obj, 'page_number': page_number
    }

    return render(request, 'index.html', context)


def CBC_test(request):
    form = forms.CBCForm()
    if request.method == 'POST':
        form = forms.CBCForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'cbc.html', {'form': form})
    # if request.method == 'POST':
    #     new_CBC = models.CBC.objects.create(
    #         age=request.POST.get('age'),
    #         gender=request.POST.get('gender'),
    #         height=request.POST.get('height'),
    #         weight=request.POST.get('weight'),
    #         WBC=request.POST.get('WBC'),
    #         RBC=request.POST.get('RBC'),
    #         Hemoglobin=request.POST.get('Hemoglobin'),
    #         Hematocrit=request.POST.get('Hematocrit'),
    #         MCV=request.POST.get('MCV'),
    #         MPV=request.POST.get('MPV'),
    #         MCH=request.POST.get('MCH'),
    #         MCHC=request.POST.get('MCHC'),
    #         RDWCV=request.POST.get('RDWCV'),
    #         Platelets=request.POST.get('Platelets'),
    #     )
    #
    #     new_CBC.save()
    # return render(request, 'cbc.html')


def cbc_result(request):
    context = {
        "cbcs": CBC.objects.filter(id=2)
    }
    return render(request, "cbc_result.html", context)


def cbc_save(request):
    cbc = get_object_or_404(models.CBC)
    print(cbc.id)
    return render(request, 'cbc_result.html')


def serviceworker(request, js):
    template = get_template('serviceworker.js')
    html = template.render()
    return HttpResponse(html, content_type="application/x-javascript")


# class HematologyView(TemplateView):
#     template_name = 'hematology.html'
#
#     def post(self, request):
#         form = HematologyForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             number = form.cleaned_data['post']
#             form = HematologyForm()
#         args = {'form': form, 'number': number}
#         return render(request, self.template_name, args)


class AllPatientAPIView(APIView):

    def get(self, request, format=None):
        try:
            patients = Patient.objects.all().order_by('id')[:4]
            data = []

            for patient in patients:
                data.append({
                    "id": patient.id,
                    "name": patient.name,
                    "gender": patient.gender,
                    "age": patient.age,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitEcgAPIView(APIView):

    def post(self, request, format=None):

        try:
            serializer = serializers.SubmitEcgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'ECG ثبت شد'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitCBCAPIView(APIView):

    def post(self, request, format=None):

        try:
            serializer = serializers.SubmitCBCSerializer(data=request.data)
            if serializer.is_valid():
                obj = serializer.save()
                context = {
                    "cbcs": CBC.objects.filter(id=obj.id)
                }
                return render(request, "cbc_result.html", context)
            # return JsonResponse(serializer.data, {'id': })
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass


class SubmitHeartAttackAPIView(APIView):

    def post(self, request, format=None):

        try:
            serializer = serializers.SubmitHeartAttackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'احتمال حمله قلبی ثبت شد'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitPatientAPIView(APIView):

    def post(self, request, format=None):

        try:
            serializer = serializers.SubmitPatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'ثبت نام کاربر انجام شد'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
