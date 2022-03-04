from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import SalesData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SalesForm
import datetime
from django.db.models import Q

# Create your views here.


def index(request):
    search = request.POST.get('search')
    download = request.GET.get('download')
    if download:
        search = request.session['search']
    else:
        request.session['search'] = search
    if search is not None:
        priorities = {'high': 'H', 'medium': 'M', 'low': 'L', 'cancel': 'C'}

        try:
            if not search.isdigit():
                search = float(search)
        except:
            pass

        if isinstance(search, float):
            data = SalesData.objects.filter(Q(unit_price=search) | Q(unit_cost=search) | Q(total_revenue=search) | Q(total_cost=search) | Q(total_profit=search)).order_by("-id")
        elif search.isdigit():
            data = SalesData.objects.filter(units_sold=search).order_by("-id")
        elif search.lower() in priorities.keys():
            data = SalesData.objects.filter(order_priority=priorities[search.lower()]).order_by("-id")
        elif search.lower() in ['online', 'offline']:
            data = SalesData.objects.filter(sales_channel__iexact=search).order_by("-id")            
        else:
            valid_date = False
            try:
                search_date = datetime.datetime.strptime(search, "%d/%m/%Y").strftime("%Y-%m-%d")
                valid_date = True                
                data = SalesData.objects.filter(Q(order_date=search_date) | Q(ship_date=search_date)).order_by("-id")
            except ValueError:
                pass

            if valid_date == False:            
                data = SalesData.objects.filter(Q(region__icontains=search) | Q(country__icontains=search) | Q(item_type__icontains=search) | Q(order_id__icontains=search) | Q(ship_date__icontains=search)).order_by("-id")
    else:
        data = SalesData.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(data, 500)
    try:
        salesRecords = paginator.page(page)
    except PageNotAnInteger:
        salesRecords = paginator.page(1)
    except EmptyPage:
        salesRecords = paginator.page(paginator.num_pages)    
    
    if download:
        return render_to_csv_response(data)

    search = "" if search is None else search
    return render(request, 'index.html', {'salesRecords': salesRecords, 'salesRecordsCnt': len(salesRecords), 'search': search})

def add(request):
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            salesObj = form.save(commit=False)

            salesObj.total_revenue = salesObj.units_sold * salesObj.unit_price
            salesObj.total_cost = salesObj.units_sold * salesObj.unit_cost
            salesObj.total_profit = salesObj.total_revenue - salesObj.total_cost
            salesObj.order_id = (SalesData.objects.all().order_by("-order_id")[0]).order_id + 1

            salesObj.save()

            return redirect('dashboard')
    else:
        form = SalesForm(initial={'sales_channel':'Online'})
    return render(request, 'add.html', {'form': form})

def edit(request, id):
    recordObj = get_object_or_404(SalesData, pk=id)
    if request.method == "POST":
        form = SalesForm(request.POST, instance=recordObj)
        if form.is_valid():
            salesObj = form.save(commit=False)

            salesObj.total_revenue = salesObj.units_sold * salesObj.unit_price
            salesObj.total_cost = salesObj.units_sold * salesObj.unit_cost
            salesObj.total_profit = salesObj.total_revenue - salesObj.total_cost

            salesObj.save()

            return redirect('dashboard')
    else:
        form = SalesForm(instance=recordObj)
    return render(request, 'add.html', {'form': form, 'edit': True})