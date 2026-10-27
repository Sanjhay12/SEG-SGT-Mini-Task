from django.shortcuts import get_object_or_404, redirect, render

from .forms import RequestForm
from .models import Request


def list_request(request):
    sort = request.GET.get('sort')
    qs = Request.objects.all()
    if request.GET.get('priority') == '1':
        qs = qs.filter(priority=True)
    return render(request, 'request_list.html', {
        'requests': qs,
        'sort': sort,
        'priority_filter': request.GET.get('priority') == '1',
    })


def view_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    return render(request, 'request_detail.html', {'service_request': service_request})


def create_request(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        service_request = form.save()
        return redirect('view_request', pk=service_request.pk)
    return render(request, 'request_form.html', {'form': form})


def update_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    form = RequestForm(request.POST or None, instance=service_request)
    if form.is_valid():
        form.save()
        return redirect('view_request', pk=service_request.pk)
    return render(request, 'request_form.html', {'form': form, 'service_request': service_request})


def delete_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        service_request.delete()
        return redirect('list_request')
    return render(request, 'request_confirm_delete.html', {'service_request': service_request})

