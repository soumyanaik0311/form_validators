from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('Webpage is Created')
            # webpage=Webpage.objects.all()
            # d1={'webpage':webpage}
            # return render(request,'display_webpages.html',d1)
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_webpage.html',d)