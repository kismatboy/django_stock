<<<<<<< HEAD
from django import forms
from .models import stocks


class StockForm(forms.ModelForm):
	class Meta:
		model =stocks
=======
from django import forms
from .models import stocks


class StockForm(forms.ModelForm):
	class Meta:
		model =stocks
>>>>>>> origin/master
		fields = ['ticker']