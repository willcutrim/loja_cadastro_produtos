from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from my_aplication.forms import ProdutoForms
from loja_cadastro_produtos.models import Produto
from django.contrib import messages


#Criando e Listando produtos
def cadastrar_produtos(request):
    listar = Produto.objects.all()
    if request.method == "POST":
        form = ProdutoForms(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["nome"]
            pc = form.cleaned_data["preco_do_produto"]
            mp = form.cleaned_data["marca_do_produto"]
            cadastrar = Produto(nome=nm, preco_do_produto=pc, marca_do_produto=mp)
            cadastrar.save()
            messages.success(request, 'Produto adcionado com sucesso')
    else:
        form = ProdutoForms()
    return render(request, 'html/cadastro_produto.html', {'form': form, 'listar': listar, 'message': messages})


#editar Produto
def editar_produto(request, id):
    produto = Produto.objects.get(pk=id)
    if request.method == 'POST':
        form = ProdutoForms(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            atualizado = messages.success(request, 'Produto atualizado com sucesso!')
        else:
            produto = Produto.objects.get(pk=id)
    form = ProdutoForms(instance=produto)
    return render(request, 'html/editar_produto.html', {'produto': produto, 'form': form})


#deletndo produtos
def deletar_produto(request, id):
    if request.method == 'POST':
        produto = Produto.objects.get(pk=id)
        produto.delete()
        excluir = messages.warning(request, 'Excluído com sucesso')
        return HttpResponseRedirect('/', {'excluir': excluir})
    