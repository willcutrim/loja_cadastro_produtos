from django import forms
from django.core import validators
from loja_cadastro_produtos.models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_do_produto', 'marca_do_produto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco_do_produto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_do_produto': forms.TextInput(attrs={'class': 'form-control'})
        }
        """
    nome = forms.CharField(label="")
    preco_do_produto = forms.DecimalField(label="")
    marca_do_produto = forms.CharField(label="")
    """
   
    