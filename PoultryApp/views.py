from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model, logout
from .models import Flock, Department, Staff, Chicken, TimeLine, Sales, Debtors
from django.contrib.auth.views import TemplateView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from .forms import (
    FlockForm,
    StaffForm,
    DebtorsForm,
    DepartmentForm,
    ChickenForm,
    HarvestForm,
    SalesForm,
)

# Create your views here.


class Index(TemplateView):
    template_name = "poultry/home/index.html"


class PoultryDashboard(TemplateView):
    template_name = "poultry/dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workerscount"] = Staff.objects.all().count()
        context["workers"] = Staff.objects.all()
        context["depts"] = Department.objects.all().count()
        context["chicken"] = Chicken.objects.all().aggregate(Sum("total"))
        return context


class FlockNew(CreateView):
    model = Flock
    form_class = FlockForm
    template_name = "poultry/flock/create.html"
    success_url = reverse_lazy("PoultryApp:all_Flock")


class FlockList(ListView):
    model = Flock
    template_name = "poultry/flock/index.html"
    context_object_name = "FlockList"


class FlockEdit(UpdateView):
    model = Flock
    template_name = "poultry/flock/edit.html"
    form_class = FlockForm
    success_url = reverse_lazy("PoultryApp:flock_edit")


# Staff Controller
class StaffNew(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = "poultry/staff/create.html"


class StaffSingle(DetailView):
    model = Staff
    template_name = "poultry/staff/single.html"
    context_object_name = "staffer"


class Staffers(ListView):
    model = Staff
    template_name = "poultry/staff/index.html"
    context_object_name = "staffs"


class StaffEdit(UpdateView):
    model = Staff
    template_name = "poultry/staff/edit.html"
    form_class = StaffForm


class StaffDestroy(View):
    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return redirect("PoultryApp:all_staff")


# Department Controller
class DepartmentNew(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "poultry/department/create.html"


class DepartmentDetail(DetailView):
    model = Department
    template_name = "poultry/department/index.html"
    context_object_name = "dpt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        staff = Staff.objects.filter(department=pk)
        context["staffer"] = staff
        return context


class DepartmentUpdate(UpdateView):
    model = Department
    template_name = "poultry/department/edit.html"
    form_class = DepartmentForm


class DepartmentDestroy(View):
    def get(self, request, pk):
        dept = Department.objects.get(pk=pk)
        dept.delete()
        return redirect("PoultryApp:poultry_dashboard")


# Chicken Views


class AddChicken(CreateView):
    model = Chicken
    form_class = ChickenForm
    template_name = "poultry/chicken/create.html"
    success_url = reverse_lazy("PoultryApp:all_chicken")


class UpdateChicken(UpdateView):
    model = Chicken
    form_class = ChickenForm
    template_name = "poultry/chicken/edit.html"
    success_url = reverse_lazy("PoultryApp:poultry_dashboard")


class ListChicken(ListView):
    model = Chicken
    template_name = "poultry/chicken/index.html"
    context_object_name = "Chicken"


class ChickenDestroy(View):
    def get(self, request, pk):
        Chicken = Chicken.objects.get(pk=pk)
        Chicken.delete()
        return redirect("PoultryApp:poultry_dashboard")


# Harvest Views
class AllHarvest(ListView):
    model = TimeLine
    template_name = "poultry/timeline/index.html"
    context_object_name = "timelines"


class AddHarvest(CreateView):
    model = TimeLine
    template_name = "poultry/timeline/create.html"
    form_class = HarvestForm
    success_url = reverse_lazy("PoultryApp:harvests")


class EditHarvest(UpdateView):
    model = TimeLine
    template_name = "poultry/timeline/edit.html"
    form_class = HarvestForm
    success_url = reverse_lazy("PoultryApp:harvests")


class DeleteHarvest(View):
    def get(self, request, pk):
        harvest = TimeLine.objects.get(pk=pk)
        harvest.delete()
        return redirect("PoultryApp:harvests")


class SingleHarvest(DetailView):
    model = TimeLine
    template_name = "poultry/timeline/single.html"
    context_object_name = "harvest"


# Sales All
class SalesAdd(CreateView):
    model = Sales
    form_class = SalesForm
    template_name = "poultry/sales/create.html"
    success_url = reverse_lazy("PoultryApp:sales")


class SalesAll(ListView):
    model = Sales
    template_name = "poultry/sales/index.html"
    context_object_name = "sales"


class SalesUpdate(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = "poultry/sales/edit.html"
    success_url = reverse_lazy("PoultryApp:sales")


class DeleteSales(View):
    def get(self, request, pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect("PoultryApp:sales")


# Creditors/Debitors
class DebtorsAdd(CreateView):
    model = Debtors
    form_class = DebtorsForm
    template_name = "poultry/credit/create.html"
    success_url = reverse_lazy("PoultryApp:debts")


class DebtorsAll(ListView):
    model = Debtors
    template_name = "poultry/credit/index.html"
    context_object_name = "debts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Debtors.objects.all().aggregate(Sum("amount"))
        return context


class DebtorsUpdate(UpdateView):
    model = Debtors
    form_class = DebtorsForm
    template_name = "poultry/credit/edit.html"
    success_url = reverse_lazy("PoultryApp:debts")


class DeleteDebtors(View):
    def get(self, request, pk):
        debt = Debtors.objects.get(pk=pk)
        debt.delete()
        return redirect("PoultryApp:debts")
