from Blog.models import Artigo
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django import forms
from tags import aplicar_tags, tags_para_objeto

class FormArtigo(forms.ModelForm):
    class Meta:
        model = Artigo
    tags = forms.CharField(max_length = 30, required = False)
    def __init__(self, *args, **kwargs):
        super(FormArtigo, self).__init__(*args, **kwargs)
        
        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(self.instance)


class ArtigoAdmin(ModelAdmin):
    form = FormArtigo
    fieldsets = [ 
                    (None, {'fields': ['titulo', 'conteudo', 'publicacao', 'slug', 'tags',]}) 
                ]
    list_display = ('titulo', 'publicacao')
    def save_model(self, request, obj, form, change):
        super(ArtigoAdmin, self).save_model(request, obj, form, change)
    
        aplicar_tags(obj, form.cleaned_data['tags'])
    

         
admin.site.register(Artigo, ArtigoAdmin)
