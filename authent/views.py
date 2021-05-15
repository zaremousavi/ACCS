from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .models import User
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.views import LoginView

# Create your views here.
@login_required
def home(request):
    return render(request, 'registration/home.html')



class ProfileUpdateView(UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    
    success_url = reverse_lazy('authent:Profile')
        
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs= super(ProfileUpdateView,self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser :
            return reverse_lazy('company:home')
        else:
            return reverse_lazy('authent:Profile')