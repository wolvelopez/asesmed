from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from encuestas.models import Pregunta


def index(request):
    ultimas_encuestas_lista = Pregunta.objects.all().order_by('-pregunta_fecha')[:5]
    context = {'ultimas_encuestas_lista': ultimas_encuestas_lista}
    return render(request, 'index.html', context)


def detalles(request, encuesta_id):
    pregunta = get_object_or_404(Pregunta, pk=encuesta_id)
    return render(request, 'detalle.html', {'pregunta':pregunta})


def resultados(request, encuesta_id):
    response = "Estas mirando los resultados de la encuesta %s."
    return HttpResponse(response % encuesta_id)


def votos(request, encuesta_id):
    return HttpResponse("Estas votando en la encuesta %s." % encuesta_id)