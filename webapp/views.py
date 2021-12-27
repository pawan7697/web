from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import navbar,pages,category,enquiry
from django.core.mail import BadHeaderError, send_mail
# Create your views here.

def home(request):
    return render(request,'webhtml/index.html')
   # return HttpResponse('page')

def about_us(request):
    return render(request,'webhtml/about.html')
   
def vision_and_mission(request):
    return render(request,'webhtml/vision-mission.html')

def contact_us(request):
    return render(request,'webhtml/contact.html')

def why_choose_us(request):
    return render(request,'webhtml/why-choose-us.html')

def thank_you(request):
    return render(request,'webhtml/thank_you.html')

def our_services(request,cat):
    pid=navbar.objects.filter(menu_slug=cat)
    all_entries=category.get_categorty()
    for ids in pid:
        data=pages.objects.filter(menu_id=ids.id)
        for value in data:
            content={
                'text':value.page,
                'imgs':value.pic,
                'title':ids.menu,
                'menu':all_entries,
            }
    
    return render(request,'webhtml/service.html',content)


def form_submit(request):

    if request.method =="POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        mssage = request.POST.get('mssage')
        enquiry.objects.create(name=name,subject=subject,email=email,phone=phone,mssage=mssage)
        return redirect('/thank_you/')
        
        
