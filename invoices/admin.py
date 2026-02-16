from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Company, Invoice, InvoiceDetail, InvoiceItemTemplate

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'created_at')
    list_filter = ('role', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('追加情報', {'fields': ('role',)}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('追加情報', {'fields': ('role',)}),
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_code', 'company_name', 'contact_person', 'phone', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('company_code', 'company_name', 'contact_person', 'email')
    ordering = ('company_code',)


@admin.register(InvoiceItemTemplate)
class InvoiceItemTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'company', 'customer_id', 'created_at', 'created_by')
    list_filter = ('created_at', 'company')
    search_fields = ('invoice_number', 'company__company_name', 'customer_id')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'item_name', 'quantity', 'unit_price', 'amount', 'order')
    list_filter = ('invoice__created_at',)
    search_fields = ('invoice__invoice_number', 'item_name')
    ordering = ('invoice', 'order')
