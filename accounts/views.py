from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
    
    # Create your views here.
    
    
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'accounts/signup.html')
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
 
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'accounts/login.html')   

#예외사항까지 처리
# def signup(request):
#     if request.method == 'POST':
#         # User has info and wants an account now!
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('blog')
#         else:
#             return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
#     else:
#         # User wants to enter info
#         return render(request, 'accounts/signup.html')