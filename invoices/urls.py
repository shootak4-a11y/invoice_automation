from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/companies/', views.admin_companies, name='admin_companies'),
    path('admin/invoice-items/', views.admin_invoice_items, name='admin_invoice_items'),
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/create-invoice/', views.admin_create_invoice, name='admin_create_invoice'),
    path('admin/export-history/', views.admin_export_history, name='admin_export_history'),
    path('admin/add-company/', views.add_company, name='add_company'),
    path('admin/add-invoice-item/', views.add_invoice_item_template, name='add_invoice_item_template'),
    path('admin/add-user/', views.add_user, name='add_user'),
    path('admin/delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/delete-company/<int:company_id>/', views.delete_company, name='delete_company'),
    path('create-invoice/', views.create_invoice_view, name='create_invoice_view'),
    path('get-company-info/', views.get_company_info, name='get_company_info'),
    path('generate-invoice/', views.generate_invoice, name='generate_invoice'),
    path('export-monthly-history/', views.export_monthly_history, name='export_monthly_history'),
]
