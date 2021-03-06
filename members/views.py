from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
# Create your views here.
from blogapp.models import Profile
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, Add_ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
class AddProfilePageView(generic.CreateView):
    add_profile = Profile
    form_class = Add_ProfileForm
    template_name = 'registration/add_profile.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url','fb_url','instagram_url','twitter_url','pinterest_url']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model=Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self,*args,**kwargs):
        # user=Profile.objects.all()
        context= super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user= get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')
def password_success(request):
    return render(request,'registration/password_success.html',{})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
# class UserLoginView():
#     form_class=LoginForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')
def UserLoginView(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            success_url = reverse_lazy('home')
        else:
            messages.info(request,'username or password is invalid.')
            return redirect('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
