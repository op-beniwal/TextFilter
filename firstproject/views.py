from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def chat(request):
    Text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newline = request.POST.get('newline', 'off')
    if removepunc == "on":
        punctuations = '''~!@#$%^&*()_+{}|":<>?/.,;'[]\=-`'''
        mess = ""
        for char in Text:
            if char not in punctuations:
                mess = mess + char
        params = {'purpose': 'check your Text :', 'mess_text': mess}
        Text = mess
    if uppercase == "on":
        mess = ""
        for char in Text:
            mess = mess + char.upper()
        params = {'purpose': 'check your Text :', 'mess_text': mess}
        Text = mess
    if lowercase == "on":
        mess = ""
        for char in Text:
            mess = mess + char.lower()
        params = {'purpose': 'check your Text :', 'mess_text': mess}
        Text = mess
    if newline == "on":
        mess = ""
        for char in Text:
            if char != "\n" and char != "\r":
                mess = mess + char
        params = {'purpose': 'check your Text :', 'mess_text': mess}
        Text = mess
    if lowercase == "on" and uppercase == "on":
        return HttpResponse("please choose any one lower/UPPER !")
    if removepunc != "on" and newline != "on" and lowercase != "on" and uppercase != "on":
        return HttpResponse("please choose any options thanks!")
    return render(request, 'text.html', params)
