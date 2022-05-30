from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
#from django.template import loader


# Create your views here.

def index(request):
    
    context ={
        "data":"cool and all",
        "list":[i for i in range(1,10,2)]
    }

    return render(request, "django.html", context)
    #template = loader.get_template('django.html')
    #return HttpResponse(template.render(context, request))

@csrf_exempt # разрешаем делать POST запрос без куки
def pictures(request):
    if request.method == "GET":
        pic_id = request.GET.get("pic_id", 411)
        name = request.GET.get("name", "Мона Лиза")
        style = request.GET.get("style", "Классический")
        return JsonResponse({"pic_id": pic_id, "name": name, "style": style})
    elif request.method == "POST":
        pic_id = request.GET.get("pic_id", 911)
        name = request.GET.get("name", "Крик")
        style = request.GET.get("style", "Модерн")
        # Сохраняем в базу данных
        return JsonResponse({"pic_id": pic_id, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")