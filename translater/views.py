from django.shortcuts import render

from translater.models import Word


def word_index(request):
    words = Word.objects.all()
    context = {
        'words' : words
    }
    return render(request, 'word_index.html', context)


def word_detail(request, pk):
    word = Word.objects.get(pk=pk)
    context = {
        'word': word
    }
    return render(request, 'word_detail.html', context)

