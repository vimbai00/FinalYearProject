from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum

from . models import Dam,Department,Staff, Fish, TimeLine,Sales,Debtors
from django.contrib.auth.views import  TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import  DamForm,StaffForm,DebtorsForm, DepartmentForm,FishForm,HarvestForm,SalesForm

# Create your views here.

class Index(TemplateView):
    template_name = 'fmsapp/home/index.html'
class Dashboard(TemplateView):
    template_name = 'fmsapp/dashboard/index.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context['depts'] = Department.objects.all().count()
        context['fishes'] = Fish.objects.all().aggregate(Sum('total'))
        return context
    
class DamNew(CreateView):
   
    model = Dam
    form_class = DamForm
    template_name = 'fmsapp/dam/create.html'
    success_url = reverse_lazy('FishFarmingApp:all_dam')

class DamList(ListView):
    model = Dam
   
    template_name = 'fmsapp/dam/index.html'
    context_object_name = 'damlist'

class DamEdit(UpdateView):
    model = Dam
   
    template_name = 'fmsapp/dam/edit.html'
    form_class = DamForm
    success_url = reverse_lazy('FishFarmingApp:all_dam')    

#Staff Controller
class StaffNew(CreateView):
    model  = Staff
   
    form_class = StaffForm
    template_name = 'fmsapp/staff/create.html'
    
class StaffSingle(DetailView):
    model = Staff
   
    template_name = 'fmsapp/staff/single.html'
    context_object_name = 'staffer'

class Staffers(ListView):
    model = Staff
   
    template_name = 'fmsapp/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(UpdateView):
    model =Staff
   
    template_name = 'fmsapp/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (View):
   
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('FishFarmingApp:all_staff')

#Department Controller
class DepartmentNew(CreateView):
    model = Department
   
    form_class = DepartmentForm
    template_name  = 'fmsapp/department/create.html'

class DepartmentDetail(DetailView):
    model = Department
   
    template_name = 'fmsapp/department/index.html'
    context_object_name = 'dept'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff 
        return context
    

class DepartmentUpdate(UpdateView):
    model = Department
   
    template_name = 'fmsapp/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(View):
   
    def get(self, request,pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('FishFarmingApp:dashboard')

#Fish Views

class AddFish(CreateView):
    model = Fish
   
    form_class = FishForm
    template_name = 'fmsapp/fish/create.html'
    success_url = reverse_lazy('FishFarmingApp:all_fish')

class UpdateFish(UpdateView):
    model = Fish
   
    form_class = FishForm
    template_name = 'fmsapp/fish/edit.html'
    success_url = reverse_lazy('FishFarmingApp:dashboard')

class ListFish(ListView):
    model = Fish
   
    template_name = 'fmsapp/fish/index.html'
    context_object_name = 'fishes'


class FishDestroy(View):
   
    def get(self, request,pk):
        fish = Fish.objects.get(pk=pk)
        fish.delete()
        return redirect('FishFarmingApp:dashboard')

#Harvest Views
class AllHarvest(ListView):
    model = TimeLine
   
    template_name = 'fmsapp/timeline/index.html'
    context_object_name = 'timelines'

class AddHarvest(CreateView):
   
    model = TimeLine
    template_name = 'fmsapp/timeline/create.html'
    form_class = HarvestForm
    success_url = reverse_lazy('FishFarmingApp:harvests')

class EditHarvest(UpdateView):
   
    model = TimeLine
    template_name = 'fmsapp/timeline/edit.html'
    form_class = HarvestForm
    success_url = reverse_lazy ('FishFarmingApp:harvests')


class DeleteHarvest(View):
   

    def get(self, request,pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect('FishFarmingAppharvests')

class SingleHarvest(DetailView):
    model = TimeLine
   
    template_name = 'fmsapp/timeline/single.html'
    context_object_name = 'harvest'

# Sales All
class SalesAdd(CreateView):
    model = Sales
   
    form_class = SalesForm
    template_name = 'fmsapp/sales/create.html'
    success_url = reverse_lazy('FishFarmingAppsales')
class SalesAll(ListView):
   
    model = Sales
    template_name = 'fmsapp/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (UpdateView):
    model = Sales
   
    form_class = SalesForm
    template_name = 'fmsapp/sales/edit.html'
    success_url = reverse_lazy ('FishFarmingAppsales')

class DeleteSales(View):
   

    def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('FishFarmingAppsales')

#Creditors/Debitors
class DebtorsAdd(CreateView):
    model = Debtors
   
    form_class = DebtorsForm
    template_name = 'fmsapp/credit/create.html'
    success_url = reverse_lazy('FishFarmingAppdebts')
class DebtorsAll(ListView):
    model = Debtors
   
    template_name = 'fmsapp/credit/index.html'
    context_object_name = 'debts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum('amount'))
        return context
    

class DebtorsUpdate (UpdateView):
    model = Debtors
   
    form_class = DebtorsForm
    template_name = 'fmsapp/credit/edit.html'
    success_url = reverse_lazy ('FishFarmingAppdebts')

class DeleteDebtors(View):
   
    def get(self, request,pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect('FishFarmingAppdebts')
