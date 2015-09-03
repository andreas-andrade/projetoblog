from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
#from django.db.models import signals

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    
    class Meta:
        ordering = ("-publicacao",)
        #app_label = 'Teste1000'
        
    def get_absolute_url(self):
        return reverse('Blog.views.artigo', kwargs={'slug':self.slug})
    def __unicode__(self):
        return self.titulo
    
#SIGNALS
    
from django.db.models import signals
from Blog.utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Artigo)