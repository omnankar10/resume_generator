from urllib import response
from django.shortcuts import render
from pandas import options
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
 
 
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        about = request.POST.get("about","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        uni = request.POST.get("uni","")
        exp= request.POST.get("exp","")
        skills = request.POST.get("skills","")
 
        profile = Profile(name=name,email=email,phone=phone,about=about,degree=degree,school=school,uni=uni,exp=exp,skills=skills)
        profile.save()
 
    
    return render(request,'pdf/accept.html')


def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size': 'letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response

def list(request):
    profiles = Profile.objects.all()
    return render (request,'pdf/list.html',{'profiles':profiles})