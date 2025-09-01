from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def loja(request):
    latest_product_list = Produto.objects.all()
    
    print(latest_product_list)
    
    context = {
        "latest_product_list": latest_product_list
    }
    return render(request, 'loja.html', context)

def carrinho(request):
    carrinho_items = Carrinho.objects.all()

    preco_total = 0

    for item in carrinho_items:
        item.subtotal = item.Produto.preco * item.quantidade
        preco_total += item.subtotal

    context = {
        "carrinho_items": carrinho_items,
        "preco_total": preco_total
    }

    return render(request, 'carrinho.html', context)

def adicionar_carrinho(request):
    if request.method == 'POST':
        produto_id = int(request.POST.get('product_id'))

        produto = get_object_or_404(Produto, id=produto_id)
        carrinho_item, created = Carrinho.objects.get_or_create(Produto=produto)
        
        if not created:
            carrinho_item.quantidade += 1
            carrinho_item.save()

        print(f"Produto {produto_id} adicionado ao carrinho.")
        return redirect('/loja/') 

def aumentar_quantidade(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        
        carrinho_item = get_object_or_404(Carrinho, id=item_id)
        carrinho_item.quantidade += 1
        carrinho_item.save()
        
        print(f"Quantidade do item {item_id} aumentada.")
        return redirect('/loja/carrinho/')

def diminuir_quantidade(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))

        carrinho_item = get_object_or_404(Carrinho, id=item_id)
        
        if carrinho_item.quantidade > 1:
            carrinho_item.quantidade -= 1
            carrinho_item.save()
        else:
            carrinho_item.delete()

        print(f"Quantidade do item {item_id} diminuída.")
        return redirect('/loja/carrinho/')

def remover_item(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))

        produto = Produto.objects.filter(id=item_id).first()

        Carrinho.objects.filter(Produto=produto).delete()

        print(f"Item {item_id} removido do carrinho.")

        return redirect('/loja/carrinho/')

def finalizar_compra(request):
    if request.method == 'POST':
        carrinho_items = Carrinho.objects.all()
        
        if carrinho_items.exists():
            # Aqui você implementaria a lógica de finalização:
            # - Criar pedido
            # - Processar pagamento
            # - Limpar carrinho
            # - Enviar email de confirmação
            
            # Por enquanto, apenas limpa o carrinho:
            carrinho_items.delete()
            
            context = {
                'mensagem': 'Compra finalizada com sucesso!',
                'titulo': 'Pedido Confirmado'
            }
            return render(request, 'sucesso.html', context)
        
    return redirect('/loja/carrinho/')