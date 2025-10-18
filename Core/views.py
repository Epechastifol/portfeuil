from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def Admin_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            return redirect('admin:login')
    else:
        form = UserCreationForm()
    return render(request, 'admin/register.html', {'form': form})
    
@login_required
def Profile(request):
    return render(request, "admin/profile.html")

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'admin/actions/user_form.html'
    success_url = reverse_lazy('admin:profile')
    success_message = "Vos informtions ont été modifiées avec succes."