from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy

from .forms import *
from jobapp.permission import user_is_employee 


def get_success_url(request):

    """
    Handle Success Url After LogIN

    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('jobapp:home')



def employee_registration(request):

    """
    Handle Employee Registration

    """
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            employee_instance = form.save()
            return redirect('account:login')
    else:
        form = EmployeeRegistrationForm()

    context = {
        'form': form
    }

    return render(request,'account/employee-registration.html',context)


def employer_registration(request):

    """
    Handle Employee Registration 

    """

    form = EmployerRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'account/employer-registration.html',context)


@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_employee
def employee_edit_profile(request, id=id):

    """
    Handle Employee Profile Update Functionality

    """
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = EmployeeProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():       
            if 'resume' in request.FILES:
                user.resume = request.FILES['resume']
            form.save()
            messages.success(request, 'Your Profile Was Successfully Updated!')
            return redirect(reverse("account:edit-profile", kwargs={'id': user.id}))
    else:
        form = EmployeeProfileEditForm(instance=user)
    context={
        
            'form':form,
            'user':user,
        }

    return render(request,'account/employee-edit-profile.html',context)



def user_logIn(request):

    """
    Provides users to logIn

    """

    form = UserLoginForm(request.POST or None)
    

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request,'account/login.html',context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')