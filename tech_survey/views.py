import json
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from .forms import TechSurveyForm
from .models import HasilTechSurvey
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def show_tech_survey(request):
    form = TechSurveyForm()

    if request.user.is_authenticated:
        riwayat = HasilTechSurvey.objects.filter(owner=request.user).first()
    else:
        riwayat = None
    
    context = {'form':form, 'riwayat':riwayat}
    return render(request, "tech_survey.html", context)

def get_result_json(request):
    if request.method == 'POST':
        form = TechSurveyForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['que_1']) + int(form_data['que_2']) + int(form_data['que_3']) + int(
                form_data['que_4']) + int(form_data['que_5']) + int(form_data['que_6']) + int(
                form_data['que_7']) + int(form_data['que_8'])
            date = datetime.date.today().strftime("%b %d, %Y, %I:%M %p")

            if skor >= 20:
                result = "Sobat Ngetech abiez!"
            elif skor >= 15:
                result = "Tech enthusiasts"
            elif skor >= 10:
                result = "Great start!"
            elif skor >= 5:
                result = "Ngetech lagi yuk!"
            else:
                result = "Kurang ngetech"

            if request.user.is_authenticated:
                riwayat = HasilTechSurvey.objects.filter(owner=request.user).first()
                if riwayat:
                    riwayat.result = result
                    riwayat.save()
                else:
                    riwayat = HasilTechSurvey(owner=request.user, result=result)
                    riwayat.save()
                date = riwayat.date.astimezone().strftime("%b %d, %Y, %I:%M %p")
            return JsonResponse({'result': result, 'date': date})
        else:
            return JsonResponse({'error': form.errors})
    else:
        return redirect('tech_survey:show-tech-survey')

@csrf_exempt
def get_current_result_for_flutter(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            riwayat = HasilTechSurvey.objects.filter(owner=request.user).first()
            if riwayat:
                return JsonResponse({
                    'user': riwayat.owner.username,
                    'result': riwayat.result
                })
            else: 
                return JsonResponse({
                    'result': '', 
                    'date': ''
                })
        else:
            JsonResponse({
                'status': False,
                'message': 'error'
            })
    return HttpResponseBadRequest("Bad request")  

@csrf_exempt
def post_survey_result_for_flutter(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            result = data['result']
            
            history = HasilTechSurvey.objects.filter(owner=request.user).first()
            if history:
                history.result = result
                history.save()
            else:
                history = HasilTechSurvey(owner=request.user, result=result)
                history.save()
                
        return JsonResponse({"status": "success"})

    return HttpResponseBadRequest("Bad request")

        
