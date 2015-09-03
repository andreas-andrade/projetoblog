from django.conf.urls import patterns, url

urlpatterns = patterns('tags.views',
    url(r'^$', 'tags', name='tags'),
    url(r'^(?P<tag_nome>.*?)/$', 'tag', name='tag'),
)