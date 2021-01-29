from django.shortcuts import render


def get_home_page(request):
    return render(request, template_name='base.html')
