import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import TechSurveyForm
from .models import HasilTechSurvey

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
            skor = int(form_data['que_1']) + int(form_data['que_2']) + int(form_data['que_3']) + int(form_data['que_4']) + int(form_data['que_5'])

            if skor >= 12:
                result = "Sobat Ngetech abiez"
            elif skor >= 9:
                result = "Tech enthusiasts"
            elif skor >= 6:
                result = "Great start!"
            elif skor >= 3:
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
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('tech_survey:show-tech-survey')
