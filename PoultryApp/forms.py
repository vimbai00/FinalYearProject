from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Flock, Staff, Department, Chicken, TimeLine, Sales, Debtors
from django.contrib.auth import get_user_model


class FlockForm(forms.ModelForm):
    class Meta:
        model = Flock
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Flock Unique Name"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "no_flock": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "No of Chicken in this Flock",
                }
            ),
            "bird_categories": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Categories"}
            ),
            "location": forms.Textarea(
                attrs={
                    "class": "form-control text-justify",
                    "placeholder": "Flock Location",
                    "rows": 2,
                }
            ),
            "about": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "More Info", "rows": 2}
            ),
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "stipend": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Salary"}
            ),
            "mobile_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Mobile Number"}
            ),
            "state": forms.Select(
                attrs={"class": "form-control", "placeholder": "Salary"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "country"}
            ),
            "department": forms.Select(
                attrs={"class": "form-control", "placeholder": ""}
            ),
            "work_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Work Description",
                    "rows": 2,
                    "cols": 4,
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Department Name"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
        }


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Chicken Name"}
            ),
            "types": forms.TextInput(
                attrs={"class": "form-control mb-2", "placeholder": "Chicken Type"}
            ),
            "HarvestDate": forms.TextInput(
                attrs={"class": "form-control mb-3 ", "placeholder": "Slaughter Date"}
            ),
            "total": forms.NumberInput(
                attrs={"class": "form-control mb-3", "placeholder": "Total"}
            ),
            "ímage": forms.FileInput(attrs={"class": "form-control mt-2"}),
        }


class HarvestForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        fields = "__all__"
        widgets = {
            "number": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Number of Chicken Slaughtered/Sold",
                }
            ),
            "Flock": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "From which Flock"}
            ),
            "others": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Other Note here"}
            ),
        }


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ["types", "weight", "quantity", "amount", "price"]
        widgets = {
            "types": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g Hen"}
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Price per one per weight",
                    "id": "amt",
                }
            ),
            "weight": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Chicken  weight"}
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Number of Chicken",
                    "id": "qty",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Amount to be paid",
                    "id": "prc",
                    "readonly": "readonly",
                }
            ),
        }


class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "file_no": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Staff-file No"}
            ),
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Total Number of Birds"}
            ),
            "department": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Staffer Department"}
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Total Amount to be paid",
                }
            ),
            "signature": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
