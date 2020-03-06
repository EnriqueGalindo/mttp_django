from django.shortcuts import render
from .models import FileFolder


def file_folder_view(request):
    return render(request, "tree.html", {'FileFolder': FileFolder.objects.all()})