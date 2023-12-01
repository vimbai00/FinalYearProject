from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model,logout
from . models import Field,Farm,Staff, Crops, TimeLine,Sales,Debtors
from django.contrib.auth.views import  TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import  FieldForm,StaffForm,DebtorsForm, FarmForm,CropsForm,HarvestForm,SalesForm

# Create your views here.

class Index(TemplateView):
    template_name = 'Crops/home/index.html'

class CropsDashboard(TemplateView):
    template_name = 'Crops/dashboard/index.html'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context['Farm'] = Farm.objects.all().count()
        context['Crops'] = Crops.objects.all().aggregate(Sum('total'))
        return context
    

class FieldNew(CreateView):
    model = Field
    form_class = FieldForm
    template_name = 'Crops/field/create.html'
    success_url = reverse_lazy('CropManagement:all_Field')

class FieldList(ListView):
    model = Field
    template_name = 'Crops/field/index.html'
    context_object_name = 'FieldList'

class FieldEdit(UpdateView):
    model = Field
    template_name = 'Crops/field/edit.html'
    form_class = FieldForm
    success_url = reverse_lazy('CropManagement:all_Field')    

#Staff Controller
class StaffNew(CreateView):
    model  = Staff
    form_class = StaffForm
    template_name = 'Crops/staff/create.html'
    
class StaffSingle(DetailView):
    model = Staff
    template_name = 'Crops/staff/single.html'
    context_object_name = 'staffer'

class Staffers(ListView):
    model = Staff
    template_name = 'Crops/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(UpdateView):
    model =Staff
    template_name = 'Crops/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (View):
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('CropManagement:all_staff')

#Farm Controller
class FarmNew(CreateView):
    model = Farm
    form_class = FarmForm
    template_name  = 'Crops/farm/create.html'

class FarmDetail(DetailView):
    model = Farm
    template_name = 'Crops/farm/index.html'
    context_object_name = 'Farm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(farm=pk)
        context["staffer"] = staff 
        return context
    

class FarmUpdate(UpdateView):
    model = Farm
    template_name = 'Crops/farm/edit.html'
    form_class = FarmForm

class FarmDestroy(View):
    def get(self, request,pk):
        farm = Farm.objects.get(pk=pk)
        farm.delete()
        return redirect('CropManagement:Crops_dashboard')

# Crops Views

class AddCrops(CreateView):
    model = Crops
    form_class = CropsForm
    template_name = 'Crops/Crops/create.html'
    success_url = reverse_lazy('CropManagement:all_Crops')

class UpdateCrops(UpdateView):
    model = Crops
    form_class = CropsForm
    template_name = 'Crops/Crops/edit.html'
    success_url = reverse_lazy('CropManagement:Crops_dashboard')

class ListCrops(ListView):
    model = Crops
    template_name = 'Crops/Crops/index.html'
    context_object_name = 'Crops'


class CropsDestroy(View):
    def get(self, request,pk):
        Crops = Crops.objects.get(pk=pk)
        Crops.delete()
        return redirect('CropManagement:Crops_dashboard')

#Harvest Views
class AllHarvest(ListView):
    model = TimeLine
    template_name = 'Crops/timeline/index.html'
    context_object_name = 'timelines'

class AddHarvest(CreateView):
    model = TimeLine
    template_name = 'Crops/timeline/create.html'
    form_class = HarvestForm
    success_url = reverse_lazy('CropManagement:harvests')

class EditHarvest(UpdateView):
    model = TimeLine
    template_name = 'Crops/timeline/edit.html'
    form_class = HarvestForm
    success_url = reverse_lazy ('CropManagement:harvests')


class DeleteHarvest(View):
    def get(self, request,pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect('CropManagement:harvests')

class SingleHarvest(DetailView):
    model = TimeLine
    template_name = 'Crops/timeline/single.html'
    context_object_name = 'harvest'

# Sales All
class SalesAdd(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = 'Crops/sales/create.html'
    success_url = reverse_lazy('CropManagement:sales')

class SalesAll(ListView):
    model = Sales
    template_name = 'Crops/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'Crops/sales/edit.html'
    success_url = reverse_lazy ('CropManagement:sales')

class DeleteSales(View):
       def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('CropManagement:sales')

#Creditors/Debitors
class DebtorsAdd(CreateView):
    model = Debtors
    form_class = DebtorsForm
    template_name = 'Crops/credit/create.html'
    success_url = reverse_lazy('CropManagement:debts')

class DebtorsAll(ListView):
    model = Debtors
    template_name = 'Crops/credit/index.html'
    context_object_name = 'debts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum('amount'))
        return context
    

class DebtorsUpdate (UpdateView):
    model = Debtors
    form_class = DebtorsForm
    template_name = 'Crops/credit/edit.html'
    success_url = reverse_lazy ('CropManagement:debts')

class DeleteDebtors(View):
    def get(self, request,pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect('CropManagement:debts')