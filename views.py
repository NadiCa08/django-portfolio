print('working on homework 5')
def index(request):
# menu display
    return HttpResponse('''
        <<h1>Welcome to my homepage</h1>
        <a href="../index">Welcome</a> <br />
        <a href="../aboutme">About me</a> <br />
        <a href="../education">Education</a> <br />
        <a href="../inclass">Activities</a> <br />
        <a href="../funfacts">funfacts</a> <br />
    ''')

def welcome(request):
    # display menus for pages
    content_html = open('content/aboutme.html').read()
    context = {
        'content': content_html,
    }
    return render(request, 'base.html', context)
    
def about_me(request):
    content_html = open('content/aboutme.html').read()
    context = {
        'content': content_html,
    }
    return render(request, 'aboutme.html', context)    
    

def education(request):
    content_html = open('content/education.html').read()
    context = {
        'content': content_html,
    }
    return render(request, 'education.html', context)

def fun_facts(request):
    content_html = open('content/funfacts.html').read()
    context = {
        'content': content_html,
    }
    return render(request, 'funfacts.html', context)
    
def inclass(request):
    content_html = open('content/inclass.html').read()
    context = {
        'content': content_html,
    }
    return render(request, 'inclass.html', context)   


