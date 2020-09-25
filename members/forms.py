from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from blogapp.models import Profile
from django.contrib.auth.models import User
from django import forms
# bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
# # profile_pic = forms.FileField(max_length=70, widget=forms.Media())
# website_url = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
# fb_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
# twitter_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check'}))
# pinterest_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check'}))

class Add_ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'fb_url', 'twitter_url', 'instagram_url', 'pinterest_url')

        widgets = {
                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                # 'profile_pic': forms.Media(),
                'website_url': forms.TextInput(attrs={'class': 'form-control'}),
                'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
                'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
                'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
                'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
            }


class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name =forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check'}))
    is_active= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    class Meta:
        model= User
        fields=('username','first_name','last_name','email','last_login','is_active')

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=70, widget=forms.PasswordInput(attrs={'class': 'form-control' ,'type':'password'}))
    new_password2 =forms.CharField(max_length=70,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model= User
        fields=('old_password','new_password1','new_password2')
