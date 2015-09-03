from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length = 30, unique = True)
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_nome': self.nome})
    
    def __unicode__(self):
        return self.nome
    
class TagItem(models.Model):
    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')#um objeto TagItem deve conter uma tag, um objeto dinamico(imagens ou artigos) e o id do objeto
        
    tag = models.ForeignKey('Tag')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index = True)
    objeto = GenericForeignKey('content_type', 'object_id')