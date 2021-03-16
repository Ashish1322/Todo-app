from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Tasks
import requests
# Create your views here.
def logine(request):
    if(request.method=="POST"):
        captcha = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LeNWXsaAAAAAJuaa2dNGGN6bkID2oYJB5buKBXq',
            'response': captcha
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
        result = r.json()
        if result['success']:
            username = request.POST['loginname']
            password = request.POST['loginpass']
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Logged in.")
                return redirect(f"http://127.0.0.1:8000/todo/{user}")
            else:
                messages.error(request,'Invalid credentials, Please try agian.')
                return redirect('home')
        else:
            messages.error(request,"Please fill the captcha correctly")
            return redirect("home")
    # Else return the 404 Error(on Manually opening this url when request is not Post )
    return HttpResponse("404","error")



def signup(request):
   
    if(request.method=="POST"):
        email = request.POST.get('signupemail')
        name = request.POST.get('signupfullname')
        username = request.POST.get('signupusername')
        pass1 = request.POST.get("signuppass")
        pass2 = request.POST.get("signupconfirmpass")

        if(User.objects.filter(username=username).exists()):
            messages.error(request,'Username Already Exists please choose some different name')
            return redirect("http://127.0.0.1:8000/")
        if(pass1!=pass2):
            messages.error(request,"Password does not matches please try again!")
            return redirect("http://127.0.0.1:8000/")
        else:
            user = User.objects.create_user(first_name=name,password=pass1,username=username,email=email)
            user.save()
            messages.success(request,"Account Created Successfully")
            return redirect("home")

    return HttpResponse("404 Error")


def showlist(request,slug):
    
    tasks = Tasks.objects.filter(user=slug)
    all_tasks = {'tasks':tasks}
    return render(request,'listtodo.html',all_tasks)

def addtolist(request):
    if(request.method=="POST"):
        data = request.POST['task']
        user = request.POST['who']
        task = Tasks(data=data,user=user)
        task.save()
        messages.success(request,"Task Added successfully to the list")
        return redirect(f"http://127.0.0.1:8000/todo/{user}")
    else:
        return HttpResponse("404 Error")

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect("home")

def delete_task(request):
    if(request.method=="POST"):
        sno = request.POST['delete']
        task = Tasks.objects.filter(sno=sno).first()
        user = task.user
        task.delete()
        messages.success(request,"Task Deleted Successfully")
        return redirect(f"http://127.0.0.1:8000/todo/{user}")
    else:
        return HttpResponse("404 Error")


def update_task(request):
    if(request.method=="POST"):
        sno = request.POST['done']
        task = Tasks.objects.filter(sno=sno).first()
        user = task.user
        task.status = "Done"
        task.save()
        messages.success(request,"Congratulations...You have completed the task")
        return redirect(f"http://127.0.0.1:8000/todo/{user}")
    else:
        return HttpResponse("404 Error")
        