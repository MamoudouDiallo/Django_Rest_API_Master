#from django.shortcuts import render
#from django.http import JsonResponse

# Create your views here.
#def api_view(request, *args, **kwargs):
#    data = {
#        'name': 'Diallo',
#        'Langage' : 'Poulard',
#        } 
#   return JsonResponse(data)

from .models import Eleve
from django.http import JsonResponse
from django.forms.models import model_to_dict

def api_views(request):
    query = Eleve.objects.all().order_by('?').first()
    data = {}
    if query:
        #data['nom'] = query.nom
        #data['prenom'] = query.prenom
        #data['age'] = query.age
        data = model_to_dict(query, fields=('nom','age'))
    return JsonResponse(data)