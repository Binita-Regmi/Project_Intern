from django.shortcuts import render
from . import views
from LandingPage.models import I_SlidingImage,Ii_Quantity_Title,Iii_Application_Areas,Iv_Media_Coverage,V_Media_Sliding,Vi_Companies_And_People,Vii_Companies_Logos
# Create your views here.
def index(request):
    sliding_images= I_SlidingImage.objects.all()
    qualities_titles=Ii_Quantity_Title.objects.all()
    application_areas=Iii_Application_Areas.objects.all()
    medias=Iv_Media_Coverage.objects.all()
    media_slidings=V_Media_Sliding.objects.all()
    companies_logos=Vi_Companies_And_People.objects.all()
    logos=Vii_Companies_Logos.objects.all()

    context={
        'sliding_images':sliding_images,
         'qualities_titles': qualities_titles,
         'application_areas':application_areas,
         'medias':medias,
         'media_slidings':media_slidings,
         'companies_logos':companies_logos,
         'logos':logos,
    }
    return render(request,'index.html',context)
