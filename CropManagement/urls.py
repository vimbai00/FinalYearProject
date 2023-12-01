from django.urls import path
from .import views

app_name = 'CropManagement'

urlpatterns = [

   
   path("", views.CropsDashboard.as_view(), name="Crops_dashboard"),
   

   
   #Field Routes

   path("dashboard/Field/new", views.FieldNew.as_view(), name="create_Field"),
   path("dashboard/Field/", views.FieldList.as_view(), name="all_Fields"),
   path("dashboard/Field/<int:pk>/edit/", views.FieldEdit.as_view(), name="Field_edit"),

   #Staff Path
   path("dashboard/staff/new/",views.StaffNew.as_view(), name="create_staff"),
   path("dashboard/staff/<int:pk>/single/", views.StaffSingle.as_view(), name="staff_single"),
   path("dashboard/staff/<int:pk>/edit/", views.StaffEdit.as_view(), name="staff_edit"),
   path("dashboard/staff/<int:pk>/delete/", views.StaffDestroy.as_view(), name="staff_delete"),
   path("dashboard/staff/", views.Staffers.as_view(), name="all_staff"),


   #Farm Routes

   path("dashboard/Farm/new/",views.FarmNew.as_view(), name="create_Farm"),
   path("dashboard/Farm/<int:pk>/single/",views.FarmDetail.as_view(), name="Farm_single"),
   path("dashboard/Farm/<int:pk>/edit/",views.FarmUpdate.as_view(), name="Farm_edit"),
   path("dashboard/Farm/<int:pk>/delete/",views.FarmDestroy.as_view(), name="Farm_delete"),

   #Crops Routes
   path("dashboard/Crops/add/",views.AddCrops.as_view(), name="create_crops"),
   path("dashboard/Crops/all/",views.ListCrops.as_view(), name="all_Crops"),
   path("dashboard/Crops/<int:pk>/edit/",views.UpdateCrops.as_view(), name="edit_crops"),
   path("dashboard/Crops/<int:pk>/delete/",views.CropsDestroy.as_view(), name="delete_crops"),

   #Harvest TimeLine
   path("dashboard/harvest/all/",views.AllHarvest.as_view(), name="harvests"),
   path("dashboard/harvest/add/",views.AddHarvest.as_view(), name="add_harvest"),
   path("dashboard/harvest/<int:pk>/edit/",views.EditHarvest.as_view(), name="edit_harvest"),
   path("dashboard/harvest/<int:pk>/delete/",views.DeleteHarvest.as_view(), name="delete_harvest"),
   path("dashboard/harvest/<int:pk>/single/",views.SingleHarvest.as_view(), name="single_harvest"),

   #Sales Routes
   path("dashboard/sales/all/",views.SalesAll.as_view(), name="crop_sales"),
   path("dashboard/sales/add/",views.SalesAdd.as_view(), name="create_sale"),
   path("dashboard/sales/<int:pk>/edit/",views.SalesUpdate.as_view(), name="edit_sale"),
   path("dashboard/sales/<int:pk>/delete/",views.DeleteSales.as_view(), name="delete_sale"),

   #Credit Sales
   path("dashboard/credit-sales/all/",views.DebtorsAll.as_view(), name="debts"),
   path("dashboard/credit-sales/add/",views.DebtorsAdd.as_view(), name="create_debt"),
   path("dashboard/credit-sales/<int:pk>/edit/",views.DebtorsUpdate.as_view(), name="edit_debt"),
   path("dashboard/credit-sales/<int:pk>/delete/",views.DeleteDebtors.as_view(), name="delete_debt")

]
