# formulário de dúvida
from django import forms
from .models import Comentario 

class DúvidaForm(forms.Form):
    assunto = forms.CharField(max_length=200, label="Assunto")
    mensagem = forms.CharField(widget=forms.Textarea, label="Sua dúvida")
    
    # formulário de comentário
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {'texto': 'Digite seu comentário'}

