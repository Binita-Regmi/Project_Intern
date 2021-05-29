from django.shortcuts import render
from django.views import View
from Aboutpage.models import I_About_Us_Top_Content,Ii_Aboutus_Odd_Even_Content,Iii_Company_Progress,Iv_Working_Steps,V_Team_Box,Vi_Subscribe_To_Our_Newsletter
# Create your views here.
def About(request):
    tops=I_About_Us_Top_Content.objects.all()
    concepts=Ii_Aboutus_Odd_Even_Content.objects.all()
    progress=Iii_Company_Progress.objects.all()
    steps=Iv_Working_Steps.objects.all()
    team_boxs=V_Team_Box.objects.all()
    news_boxes=Vi_Subscribe_To_Our_Newsletter.objects.all()
    context={
        'tops':tops,
        'concepts':concepts,
        'progress':progress,
        'steps':steps,
        'team_boxs':team_boxs,
        'news_boxes':news_boxes,
    }
    return render(request,'aboutus.html',context)