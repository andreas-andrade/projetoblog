from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, StackedInline
from models import Album, Imagem
from tags import tags_para_objeto, aplicar_tags
try:
    import Image
except ImportError:
    from Blog.PIL import Image

class ImagemInline(StackedInline):
    model = Imagem

class AlbumAdmin(ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
    inlines = [ImagemInline]
    save_on_top = True
    
class FormImagem(forms.ModelForm):
    class Meta:
        model = Imagem
    tags = forms.CharField(max_length = 30, required = False)
    
    def __init__(self, *args, **kwargs):
        super(FormImagem, self).__init__(*args, **kwargs)
        
        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(self.instance)

class ImagemAdmin(ModelAdmin):
    list_display = ('titulo','album', 'miniatura')
    list_display_links = ('titulo','miniatura')
    list_filter = ('album',)
    search_fields = ('titulo', 'descricao',)
    form = FormImagem
    
    def save_model(self, request, obj, form, change):
        """Metodo declarado para criar miniatura da imagem depois de salvar"""
        super(ImagemAdmin, self).save_model(request, obj, form, change)
        
        if 'original' in form.changed_data:
            extensao = obj.original.name.split('.')[-1] #-1 garante que a extensao pega a ultima parte da string splitada. ex: carro.jpg ['carro', 'jpg']. -1 faz o indice ir ao contrario, de frente pra tras
            obj.thumbnail = 'galeria/thumbnail/%s.%s'%(obj.id, extensao)
            
            miniatura = Image.open(obj.original.path)
            miniatura.thumbnail((180,180), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)
            obj.save()
            
        aplicar_tags(obj, form.cleaned_data['tags'])
            
admin.site.register(Album, AlbumAdmin)
admin.site.register(Imagem, ImagemAdmin)