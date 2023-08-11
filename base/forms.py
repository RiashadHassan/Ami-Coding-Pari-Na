from django import forms
from .models import InputItem

class InputItemForm(forms.ModelForm):
    search_number = forms.IntegerField(label='Search Number')
    class Meta:
        model = InputItem
        fields = ['input_numbers']
    
    def check_search_input(self, sorted_input_numbers_list):
        search_number = self.cleaned_data['search_number']
        return search_number in sorted_input_numbers_list