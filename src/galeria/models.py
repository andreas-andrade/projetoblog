# -*- coding: utf-8 -*-
from Blog.utils.signals_comuns import slug_pre_save
from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy

class Album(models.Model):
    """Um álbum é um pacote de imagens, ele tem um título e um slug para sua identificaçao """
    titulo = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, blank = True, unique = True)
    class Meta:
        ordering = ('titulo',)
        verbose_name_plural = 'Álbuns'
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('album', kwargs={'slug': self.slug})
    
class Imagem(models.Model):
    '''Cada instância desta classe contém uma imagem da galeria, com seu respectivo thumbnail
     (miniatura) e imagem em tamanho natural.
     Várias imagens podem conter dentro de um Álbum.'''
    
    class Meta:
        ordering = ('album', 'titulo',)
        verbose_name = ugettext_lazy('Imagem')
        verbose_name_plural = ugettext_lazy('Imagens')
        
    album = models.ForeignKey('Album')
    titulo = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, blank = True, unique = True)
    descricao = models.TextField(blank = True)
    original = models.ImageField(null = True, blank = True, upload_to = 'galeria/original')
    thumbnail = models.ImageField(null = True, blank = True, upload_to = 'galeria/thumbnail')
    publicacao = models.DateTimeField(default = datetime.now, blank = True)
    
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('imagem', kwargs={'slug': self.slug})
    def miniatura(self):
        return '<img src="%s"'% self.thumbnail.url
    miniatura.allow_tags = True
    
#SIGNALS
signals.pre_save.connect(slug_pre_save, sender = Album)
signals.pre_save.connect(slug_pre_save, sender = Imagem)