from django.shortcuts import render, redirect
from .models import Lead, Customer, Opportunity, Invoice
from .forms import LeadForm, CustomerForm, OpportunityForm, InvoiceForm

def home(request):
    context = {
        'total_leads': Lead.objects.count(),
        'total_customers': Customer.objects.count(),
        'total_opportunities': Opportunity.objects.count(),
        'total_invoices': Invoice.objects.count(),
    }
    return render(request, 'dashboard.html', context)

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'accounts/lead_list.html', {'leads': leads})

def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()
    return render(request, 'accounts/add_lead.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'accounts/add_customer.html', {'form': form})

def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'accounts/opportunity_list.html', {'opportunities': opportunities})

def add_opportunity(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')
    else:
        form = OpportunityForm()
    return render(request, 'accounts/add_opportunity.html', {'form': form})

def sales_pipeline(request):
    stages = ['proposal', 'negotiation', 'won', 'lost']
    pipeline = {}
    for stage in stages:
        pipeline[stage] = Opportunity.objects.filter(stage=stage)
    return render(request, 'accounts/sales_pipeline.html', {'pipeline': pipeline})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'accounts/invoice_list.html', {'invoices': invoices})

def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'accounts/add_invoice.html', {'form': form})

def delete_lead(request, lead_id):
    lead = Lead.objects.get(id=lead_id)
    lead.delete()
    return redirect('lead_list')