from Blog.feeds import UltimosArtigos
from Blog.models import Artigo
from django.conf import settings
from django.conf.urls import patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blog.views.home', name='home'),
    # url(r'^Blog/', include('Blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'django.views.generic.date_based.archive_index', {'queryset': Artigo.objects.all(), 'date_field': 'publicacao'}),
    (r'^admin/', include(admin.site.urls)),

    (r'^rss/(?P<url>.*)/$', UltimosArtigos()),#essa url define a pagina de rss
    (r'^artigo/(?P<slug>[\w_-]+)/$', 'Blog.views.artigo'),
    (r'^contato/$', 'Blog.views.contato'),
    #(r'^media/(.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #(r'^comments/', include('django.contrib.comments.urls')), comentarios. nao funciona porque esta app esta "deprecated"
    (r'^galeria/', include('galeria.urls')),
    (r'^tags/', include('tags.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^contas/', include('contas.urls')),
    (r'^entrar/$', 'django.contrib.auth.views.login', {'template_name': 'entrar.html'}, 'entrar'), 
    (r'^sair/$', 'django.contrib.auth.views.logout', {'template_name': 'sair.html'}, 'sair'),
    (r'^registrar/$', 'Blog.views.registrar', {}, 'registrar'),
    (r'^todos_os_usuarios/$', 'Blog.views.todos_os_usuarios', {}, 'todos_os_usuarios'),
    (r'^mudar_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'mudar_senha.html'}, 'mudar_senha'),
    (r'^mudar_senha/concluido/$', 'django.contrib.auth.views.password_change_done',{'template_name': 'mudar_senha_concluido.html'}, 'mudar_senha_concluido'),
)

if settings.LOCAL:
    urlpatterns += patterns('',
           (r'^media/(.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )
