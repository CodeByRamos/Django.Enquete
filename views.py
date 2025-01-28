from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Perguntas, Escolha

def index(request):
    ultimasquestoes = Perguntas.objects.order_by('-datadepublicacao')[:5]
    conteudo = {'ultimasquestoes': ultimasquestoes}
    return render(request, 'Enquete/index.html', conteudo)

def votacao(request, question_id):
    pergunta = get_object_or_404(Perguntas, pk=question_id)

    try:
        escolha = pergunta.escolhas.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        return render(request, 'Enquete/votacao.html', {
            'Perguntas': pergunta,
            'error_message': "Você não escolheu uma alternativa.",
        })
    else:
        escolha.votos += 1
        escolha.save()
        return HttpResponseRedirect(reverse('Enquete:resultados', args=(pergunta.id,)))

def resultados(request, question_id):
    pergunta = get_object_or_404(Perguntas, pk=question_id)
    return render(request, 'Enquete/resultados.html', {'Perguntas': pergunta})
