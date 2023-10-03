from django import forms
from .models import Autor, Categoria, Editora

class Frm_Autor(forms.ModelForm):
    
    class Meta:         
        model = Autor
        fields = ['nome', 'comentario']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class':'form-control'})
        self.fields['comentario'].widget.attrs.update({'class':'form-control'})

class Frm_Categoria(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ['nome']
        
    def __init__(self, *args, **kwargs):      
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class':'form-control'})

class Frm_Editora(forms.ModelForm):
    
    class Meta:
        model = Editora
        fields = ['nome', 'comentario']
        
    def __init__(self, *args, **kwargs):     
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class':'form-control'})      
    