from Blog.models import Artigo
from django.contrib.syndication.views import Feed

class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog do Andreas'
    link = '/'
    
    #todos os metodos abaixo sao previstos para a construcao do RSS. https://docs.djangoproject.com/en/dev/ref/contrib/syndication/
    def items(self):
        return Artigo.objects.all()
    
    def item_title(self, item):
        return item.titulo
    
    def item_description(self, item): 
        return item.conteudo
    
    """def item_link(self, artigo):
        return '/artigo/%d/' % artigo.id"""