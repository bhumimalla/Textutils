# i created it
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!@#$%^&*()_;:'"\[]{}-*/<>~/.'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New line remove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if spaceremove == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space remove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == 'on':
        count = 0
        for char in djtext:
            if char != ' ':
                count = count + 1
        analyzed = count
        params = {'purpose': 'New line remove', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremove != "on" and spaceremove != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)