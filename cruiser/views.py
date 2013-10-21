from annoying.decorators import render_to

@render_to('pages/index.html')
def index(request):
    return {}