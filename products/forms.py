from .models import Comment
from django.forms import ModelForm, Textarea


class CommentsForm(ModelForm):
    
    class Meta:
        model = Comment
    
        fields = ('text',)
    
        widgets = {
            'text': Textarea(attrs={
                'class':'form-control',
                'arial-label':'Comentarios',
                'placeholder':'Deja tu comentario',
                'id':'formComment'
            })
    }