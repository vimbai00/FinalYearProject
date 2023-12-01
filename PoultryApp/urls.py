from django.urls import path
from . import views

app_name = "PoultryApp"

urlpatterns = [
    path("", views.PoultryDashboard.as_view(), name="poultry_dashboard"),
    # Flock Routes
    path("dashboard/flock/new", views.FlockNew.as_view(), name="create_flock"),
    path("dashboard/flock/", views.FlockList.as_view(), name="all_Flock"),
    path(
        "dashboard/flock/<int:pk>/edit/", views.FlockEdit.as_view(), name="flock_edit"
    ),
    # Staff Path
    path("dashboard/staff/new/", views.StaffNew.as_view(), name="create_staff"),
    path(
        "dashboard/staff/<int:pk>/single/",
        views.StaffSingle.as_view(),
        name="staff_single",
    ),
    path(
        "dashboard/staff/<int:pk>/edit/", views.StaffEdit.as_view(), name="staff_edit"
    ),
    path(
        "dashboard/staff/<int:pk>/delete/",
        views.StaffDestroy.as_view(),
        name="staff_delete",
    ),
    path("dashboard/staff/", views.Staffers.as_view(), name="all_staff"),
    # Department Routes
    path(
        "dashboard/department/new/", views.DepartmentNew.as_view(), name="create_dept"
    ),
    path(
        "dashboard/department/<int:pk>/single/",
        views.DepartmentDetail.as_view(),
        name="dept_single",
    ),
    path(
        "dashboard/department/<int:pk>/edit/",
        views.DepartmentUpdate.as_view(),
        name="dept_edit",
    ),
    path(
        "dashboard/department/<int:pk>/delete/",
        views.DepartmentDestroy.as_view(),
        name="dept_delete",
    ),
    # Chicken Routes
    path("dashboard/chicken/add/", views.AddChicken.as_view(), name="create_chicken"),
    path("dashboard/chicken/all/", views.ListChicken.as_view(), name="all_chicken"),
    path(
        "dashboard/chicken/<int:pk>/edit/",
        views.UpdateChicken.as_view(),
        name="edit_chicken",
    ),
    path(
        "dashboard/chicken/<int:pk>/delete/",
        views.ChickenDestroy.as_view(),
        name="delete_chicken",
    ),
    # Harvest TimeLine
    path("dashboard/harvest/all/", views.AllHarvest.as_view(), name="harvests"),
    path("dashboard/harvest/add/", views.AddHarvest.as_view(), name="add_harvest"),
    path(
        "dashboard/harvest/<int:pk>/edit/",
        views.EditHarvest.as_view(),
        name="edit_harvest",
    ),
    path(
        "dashboard/harvest/<int:pk>/delete/",
        views.DeleteHarvest.as_view(),
        name="delete_harvest",
    ),
    path(
        "dashboard/harvest/<int:pk>/single/",
        views.SingleHarvest.as_view(),
        name="single_harvest",
    ),
    # Sales Routes
    path("dashboard/sales/all/", views.SalesAll.as_view(), name="sales"),
    path("dashboard/sales/add/", views.SalesAdd.as_view(), name="create_sale"),
    path(
        "dashboard/sales/<int:pk>/edit/", views.SalesUpdate.as_view(), name="edit_sale"
    ),
    path(
        "dashboard/sales/<int:pk>/delete/",
        views.DeleteSales.as_view(),
        name="delete_sale",
    ),
    # Credit Sales
    path("dashboard/credit-sales/all/", views.DebtorsAll.as_view(), name="debts"),
    path("dashboard/credit-sales/add/", views.DebtorsAdd.as_view(), name="create_debt"),
    path(
        "dashboard/credit-sales/<int:pk>/edit/",
        views.DebtorsUpdate.as_view(),
        name="edit_debt",
    ),
    path(
        "dashboard/credit-sales/<int:pk>/delete/",
        views.DeleteDebtors.as_view(),
        name="delete_debt",
    ),
]
