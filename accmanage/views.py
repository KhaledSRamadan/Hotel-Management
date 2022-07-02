from django.shortcuts import render, redirect

# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from roommanage.views import rooms_view,home_view
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# class login (CreateView):
# 	form_class=AuthenticationForm
# 	success_url=reverse_lazy(home_view)
# 	template_name = 'blog/login.html'
# #	return render(request, 'blog/login.html',{'form':form})

# 
def loginprocess(request):
	if request.method =='POST':
		username= request.POST.get('username')
		password= request.POST.get('password')
		usern=authenticate(request,username=username,password=password)

		if usern is not None:
			login(request, usern)
			return redirect(home_view)

	return render(request, 'blog/login.html')

def logoutprocess(request):
	logout(request)
	return redirect(home_view)

def profile(request):
	return render(request,'blog/profile.html')



# class signup(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy(loginprocess)
#     template_name = 'blog/contact-us.html'

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
        	form.save()
        	username = form.cleaned_data.get('username')
        	raw_password = form.cleaned_data.get('password1')
        	users = authenticate(username=username, password=raw_password)
        	if users is not None:
        		login(request, users)
        		return redirect(home_view)
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/contact-us.html', {'form': form})
# def register_view(request):
	# return render(request,'blog/contact-us.html')





#     from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})