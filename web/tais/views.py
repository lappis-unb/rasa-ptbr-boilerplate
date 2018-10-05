from django.shortcuts import render
from information.models import Maintainance

def index(request):
    maintainance = Maintainance.objects.all().first()
    maintainance_is_set = False

    if maintainance != None:
        maintainance_is_set = maintainance.set_maintainance_page

    return render(request, 'home.html', {
        'maintainance_is_set': maintainance_is_set,
    })

