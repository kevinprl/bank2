from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bank.models import Branch,City

# Create your views here.
def done(request):

    return render(request,'submit.html')

def new(request):
    return render(request,'new_page.html')

def apply(request):
    branches = Branch.objects.all()  # Get all branches
    cities = City.objects.none()
    selected_branch = None

    if request.method == 'POST':
        print(request.POST)  # Print POST data
        branch_id = request.POST.get('Branch')  # Get the selected branch ID from POST data
        print(branch_id)  # Print branch ID
        cities = City.objects.filter(Branch_id=branch_id)  # Filter cities by branch
        selected_branch = Branch.objects.get(id=branch_id)  # Get the selected branch
    elif 'Branch' in request.GET:
        cities = City.objects.filter(Branch_id=request.GET['Branch'])
        selected_branch = Branch.objects.get(id=request.GET['Branch'])  # Get the selected branch

    return render(request, 'form.html', {'branches': branches, 'cities': cities, 'selected_branch': selected_branch})

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'User Not Found')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password mismatch')
            return redirect('register')

    return render(request,'register.html')


# dependent dropdown




