from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views import View

# Create your views here.

class Index(View):
    template_name = 'index.html'
    context = {}
    name = _('index')

    def get(self, request):
        request.session['breadcrumb'] = [self.name,]
        self.context['request'] = request
        return render(request, self.template_name, self.context)

    def post(self, request):
        return self.get(request)

# def index(request):
#     context = {}
#     request.session['breadcrumb'] = ['']
#     return render(request, 'index.html', {})

def students(request):
    return render(request, 'students.html', {})

def classes(request):
    return render(request, 'classes.html', {})

def settings(request):
    return render(request, 'settings.html', {})
