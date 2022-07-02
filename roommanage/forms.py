from django import forms
from .models import reservation

class ReservationForm(forms.ModelForm):
	arrivedate=forms.DateField(widget = forms.SelectDateWidget)
	leavedate=forms.DateField(widget = forms.SelectDateWidget)

	class Meta(forms.ModelForm):
	    model = reservation
	    
	    fields= ('arrivedate','leavedate','serviceid')

	    
	    widgets = {

	        'roomid': forms.TextInput(attrs={'class':'input'})
	

	    }
	    