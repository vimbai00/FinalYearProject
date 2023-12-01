from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . models import Field, Staff, Farm,Crops,TimeLine,Sales,Debtors
from django.contrib.auth import get_user_model

class FieldForm (forms.ModelForm):

    class Meta:
        model = Field
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Farm Unique Name'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'no_Field':forms.TextInput(attrs={'class':'form-control', 'placeholder':'No of Crops in this Field'}),
            'crop_categories':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categories'}),
            'location':forms.Textarea(attrs={'class':'form-control text-justify', 'placeholder':'Field Location','rows':2}),
            'about':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More Info','rows':2}),
        }

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = "__all__"
        widgets={
            
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'stipend':forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'state':forms.Select(attrs={'class':'form-control','placeholder':'Salary'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),
            'Farm':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'work_description':forms.Textarea(attrs={'class':'form-control','placeholder':'Work Description','rows':2, 'cols':4}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Farm Name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
        }

class CropsForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Crops Name'}),
            'types':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Crops Type'}),
            'HarvestDate':forms.TextInput(attrs={'class':'form-control mb-3 ','placeholder':'Harvest Date'}),
            'total':forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Total'}),
            'ímage':forms.FileInput(attrs={'class':'form-control mt-2'})
        }

class HarvestForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        fields = '__all__'
        widgets = {
            'number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Crops Harvested'}),
            'Field':forms.TextInput(attrs={'class':'form-control','placeholder':'From which Dam'}),
            'others':forms.Textarea(attrs={'class':'form-control','placeholder':'Other Note here'})
        }

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =['types','weight','quantity','amount','price']
        widgets = {
            'types':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g potatoes'}),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per one per weight','id':'amt'}),
            'weight':forms.NumberInput(attrs={'class':'form-control','placeholder':'Crops  weight'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Crops','id':'qty'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid','id':'prc','readonly':'readonly'})

        }

class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'file_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Staff-file No'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Birds'}),
            'Farm':forms.TextInput(attrs={'class':'form-control','placeholder':'Staffer Farm' }),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid'}),
            'signature':forms.ClearableFileInput(attrs={'class':'form-control'})

        }
        