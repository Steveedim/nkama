from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Report
from django.contrib.auth.models import User


def reports_home(request):
    return render(request, 'reports/home.html')

@login_required
def create_report(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Report.objects.create(client=request.user, title=title, content=content)
        return redirect('view_reports')
    return render(request, 'reports/create_report.html')

@login_required
def view_reports(request):
    reports = Report.objects.filter(client=request.user)
    return render(request, 'reports/view_reports.html', {'reports': reports})
