from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        response = 'olá! Como posso ajudar?'
        return JsonResponse({'response': response})
    return JsonResponse({"error" : "metodo não permitido"}, status=405)
