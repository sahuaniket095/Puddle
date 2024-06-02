from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignupForm


from django.urls import reverse_lazy
# Create your views here.
def Home(request):
    return render(request,'Home.html')




@csrf_exempt
def signup(request):
        
        if request.method == 'POST':
           form = SignupForm(request.POST)

           if form.is_valid():
                form.save()

                return redirect('/login')
        else:
             form =SignupForm()
        return render(request,'signup.html',{'form':form})     
        





