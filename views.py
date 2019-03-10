from django.shortcuts import render

print('working on homework 5')


def welcome(request):
    ## display menus for pages
#    content_html = open('content/index.html').read()
    context = {
#        'content': content_html,
    }
    return render(request, 'index.html', context)
    
def about_me(request):
    #content_html = open('content/aboutme.html').read()
    context = {
        #'content': content_html,
    }
    return render(request, 'aboutme.html', context)    
    

def education(request):
    #content_html = open('content/education.html').read()
    context = {
        #'content': content_html,
    }
    return render(request, 'education.html', context)
    
def inclass(request):
    #content_html = open('content/inclass.html').read()
    context = {
        #'content': content_html,
    }
    return render(request, 'inclass.html', context)   
    

def fun_facts(request):
    #content_html = open('content/funfacts.html').read()
    context = {
        #'content': content_html,
    }
    return render(request, 'funfacts.html', context)
    
