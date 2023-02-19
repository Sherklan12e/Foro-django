
from django.forms import ModelForm 
from . models import Room 
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
                    
        self.fields['name'].widget.attrs['class'] = 'w-full border rounded-lg py-2 px-3'
        self.fields['name'].widget.attrs['placeholder'] = 'Room Name'