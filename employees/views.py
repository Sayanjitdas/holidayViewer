from django.shortcuts import render

def employee_get_list(request):

    if request.method == "GET":
        return render(request,"employee_get_list.html")
