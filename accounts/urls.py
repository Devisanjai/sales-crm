from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/add/', views.add_lead, name='add_lead'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('opportunities/', views.opportunity_list, name='opportunity_list'),
    path('opportunities/add/', views.add_opportunity, name='add_opportunity'),
    path('pipeline/', views.sales_pipeline, name='sales_pipeline'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('leads/delete/<int:lead_id>/', views.delete_lead, name='delete_lead'),
]