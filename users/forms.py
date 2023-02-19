from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ImageField, FileInput
from . models import User

class UpdateUserForm(ModelForm):
    avatar = ImageField(widget=FileInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'avatar','bio']
    def __init__(self, *args, **kwargs):
            super(UpdateUserForm, self).__init__(*args, **kwargs)
            
            self.fields['email'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['username'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['avatar'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['bio'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['email'].widget.attrs['placeholder'] = 'Email'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['bio'].widget.attrs['placeholder'] = 'Something about you'
        

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            
            self.fields['email'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['username'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
            self.fields['password1'].widget.attrs['class'] = 'text-negro text-sm rounded-lg block w-full p-2.5 placeholde-gray-400'
            self.fields['password2'].widget.attrs['class'] = 'text-negro text-sm rounded-lg block w-full p-2.5 placeholde-gray-400'
            self.fields['email'].widget.attrs['placeholder'] = 'Email'
            self.fields['name'].widget.attrs['placeholder'] = 'Usermame'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Repit Password'