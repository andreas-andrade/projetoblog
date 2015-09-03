from Blog import settings
from Blog.models import Artigo
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from forms import FormRegistro, FormContato

def artigo(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug)
    return render_to_response('Blog/artigo.html', locals(), context_instance=RequestContext(request))

@csrf_exempt
def contato(request):
    a = settings.MEDIA_ROOT
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            mostrar = "Contato enviado!"
    else:
        form = FormContato()
    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))

def registrar(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)

        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormRegistro()

    return render_to_response('registrar.html', locals(), context_instance=RequestContext(request), )

@permission_required('contas.ver_todos_os_usuarios')
def todos_os_usuarios(request):
    usuarios = User.objects.all()
    return render_to_response('todos_os_usuarios.html', locals(), context_instance=RequestContext(request),)