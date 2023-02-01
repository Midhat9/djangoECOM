from django.http import HttpResponse
from django.shortcuts import render


def layout(request):
    return render(request,"adminPages/Layout.html")



def userform(request):
    return render(request,"adminPages/Forms/form.html")

def userfetch(request):
    return render(request,"adminPages/Forms/fetchuser.html")