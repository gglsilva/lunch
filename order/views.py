from account.models import Profile
from order.models import Order, OrderItem
from product.models import Product
from django.http import JsonResponse
import json


def action_fetch_create_order(request):
    
    if request.method != 'POST':
        return JsonResponse({'response': 'error', 'message': 'Método inválido. Apenas requisições POST são permitidas.'}, status=400)    
    
    data = json.loads(request.body)
    produtos = data.get('produtos')
    cliente = data.get('cliente')
    mensagem = data.get('msg')

    profile = Profile.objects.get(user__username=cliente)

    order = Order.objects.create(client=profile, note=mensagem)

    for item in produtos:
        produto = Product.objects.get(id=int(item))
        OrderItem.objects.create(order=order,
                                 product=produto,
                                 )
   
    return JsonResponse({'response': 'success'})