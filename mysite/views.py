# I have created this website - kush
from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    return render(request, 'index.html')





def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')

    #Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    titlecase = request.POST.get('titlecase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    lowercase = request.POST.get('lowercase', 'off')



    # check which check box is on
    if removepunc == 'on':
        punctations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed




    if fullcaps == 'on':

        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to UPPERCASE  ', 'analyzed_text': analyzed}

        djtext = analyzed

    if lowercase == 'on':

        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'changed to lowercase ', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount == 'on':

        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'characters counter', 'analyzed_text': analyzed}


        djtext = analyzed
    if titlecase == "on":

        analyzed = ""

        for char in djtext:


            analyzed = analyzed + djtext.title()


        params = {'purpose': 'Changed to Titlecase', 'analyzed_text': analyzed}


        djtext = analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for Index, char in enumerate(djtext):
            if not (djtext[Index] == " " and djtext[Index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose' :Extraspaces Removed', 'analyzed_text': analyzed}


    if removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and lowercase!= 'on' and titlecase!= 'on' and charcount!= 'on':
        return HttpResponse(" Please enable the checkboxes and try again :)")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
