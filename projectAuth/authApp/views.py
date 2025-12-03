from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context ={}
    return render(request,'authApp/home.html',context)

@login_required(login_url='login')
def promoProducts(request):
    context ={}
    return render(request,'authApp/promo_products.html',context)


def loginUser(request):
    """
    - get user inputs
    - validate whether user exists
    - authenticate user 
    - login user  them to the home
    - redirect
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exists!")
        
        user = authenticate(request, username= username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('promoProducts')
        else:
            print('Wrong Credentials!!')

    context ={}
    return render(request,'authApp/login_form.html',context)

def logoutUser(request):
    context ={}
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.username = f"@{user.username}"
            user.save()
            login(request, user)
            return redirect('promoProducts')

    context ={"form":form}
    return render(request,'authApp/register_form.html',context)