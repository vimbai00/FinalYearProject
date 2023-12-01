from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model,logout
from . models import Paddock,Department,Staff, Livestock, TimeLine,Sales,Debtors
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import  PaddockForm,StaffForm,DebtorsForm, DepartmentForm,LivestockForm,HarvestForm,SalesForm

# Create your views here.

class Index(TemplateView):
    template_name = 'livestockapp/home/index.html'

class Dashboard(TemplateView):
    template_name = 'livestockapp/dashboard/index.html'
    
class PaddockNew(CreateView):
   
    model = Paddock
    form_class = PaddockForm
    template_name = 'livestockapp/paddocks/create.html'
    success_url = reverse_lazy('Livestock:all_paddocks')

class PaddockList(ListView):
    model = Paddock
    
    template_name = 'livestockapp/paddocks/index.html'
    context_object_name = 'paddocklist'

class PaddockEdit(UpdateView):
    model = Paddock
   
    template_name = 'livestockapp/paddocks/edit.html'
    form_class = PaddockForm
    success_url = reverse_lazy('Livestock:all_paddocks')    

#Staff Controller
class StaffNew(CreateView):
    model  = Staff
    
    form_class = StaffForm
    template_name = 'livestockapp/staff/create.html'
    
class StaffSingle(DetailView):
    model = Staff
   
    template_name = 'livestockapp/staff/single.html'
    context_object_name = 'staffer'

class Staffers(ListView):
    model = Staff
    
    template_name = 'livestockapp/staff/index.html'
    context_object_name = 'staffs'

class StaffEdit(UpdateView):
    model =Staff
    
    template_name = 'livestockapp/staff/edit.html'
    form_class =  StaffForm

class StaffDestroy (View):
   
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect('Livestock:all_staff')

#Department Controller
class DepartmentNew(CreateView):
    model = Department
    
    form_class = DepartmentForm
    template_name  = 'livestockapp/department/create.html'

class DepartmentDetail(DetailView):
    model = Department
    
    template_name = 'livestockapp/department/index.html'
    context_object_name = 'dpt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff 
        return context
    

class DepartmentUpdate(UpdateView):
    model = Department
    
    template_name = 'livestockapp/department/edit.html'
    form_class = DepartmentForm

class DepartmentDestroy(View):
    
    def get(self, request,pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect('Livestock:livestock_dashboard')

#Livestock Views

class AddLivestock(CreateView):
    model = Livestock
    
    form_class = LivestockForm
    template_name = 'livestockapp/livestock/create.html'
    success_url = reverse_lazy('Livestock:all_livestock')

class UpdateLivestock(UpdateView):
    model = Livestock
   
    form_class = LivestockForm
    template_name = 'livestockapp/livestock/edit.html'
    success_url = reverse_lazy('Livestock:livestock_dashboard')

class ListLivestock(ListView):
    model = Livestock
   
    template_name = 'livestockapp/livestock/index.html'
    context_object_name = 'livestock'


class LivestockDestroy(View):
   
    def get(self, request,pk):
        livestock = Livestock.objects.get(pk=pk)
        livestock.delete()
        return redirect('Livestock:livestock_dashboard')

#Harvest Views
class AllHarvest(ListView):
    model = TimeLine
    
    template_name = 'livestockapp/timeline/index.html'
    context_object_name = 'timelines'

class AddHarvest(CreateView):
    
    model = TimeLine
    template_name = 'livestockapp/timeline/create.html'
    form_class = HarvestForm
    success_url = reverse_lazy('Livestock:harvests')

class EditHarvest(UpdateView):
    
    model = TimeLine
    template_name = 'livestockapp/timeline/edit.html'
    form_class = HarvestForm
    success_url = reverse_lazy ('Livestock:harvests')


class DeleteHarvest(View):
    

    def get(self, request,pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect('Livestock:harvests')

class SingleHarvest(DetailView):
    model = TimeLine
    
    template_name = 'livestockapp/timeline/single.html'
    context_object_name = 'harvest'

# Sales All
class SalesAdd(CreateView):
    model = Sales
    
    form_class = SalesForm
    template_name = 'livestockapp/sales/create.html'
    success_url = reverse_lazy('Livestock:sales')

class SalesAll(ListView):
   
    model = Sales
    template_name = 'livestockapp/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (UpdateView):
    model = Sales
   
    form_class = SalesForm
    template_name = 'livestockapp/sales/edit.html'
    success_url = reverse_lazy ('Livestock:sales')

class DeleteSales(View):
    

    def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('Livestock:sales')

#Creditors/Debitors
class DebtorsAdd(CreateView):
    model = Debtors
    
    form_class = DebtorsForm
    template_name = 'livestockapp/credit/create.html'
    success_url = reverse_lazy('Livestock:debts')

class DebtorsAll(ListView):
    model = Debtors
    
    template_name = 'livestockapp/credit/index.html'
    context_object_name = 'debts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum('amount'))
        return context
    

class DebtorsUpdate (UpdateView):
    model = Debtors
    
    form_class = DebtorsForm
    template_name = 'livestockapp/credit/edit.html'
    success_url = reverse_lazy ('Livestock:debts')

class DeleteDebtors(View):
    
    def get(self, request,pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect('Livestock:debts')