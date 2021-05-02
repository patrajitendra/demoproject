from django.shortcuts import render



def showindex(request):
    return render(request,"index.html")

def showdata(request):
    n=request.POST["t1"]
    a=request.POST["t2"]
    d1={"name":n,"age":a}
    return render(request,"display.html",d1)
