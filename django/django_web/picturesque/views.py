from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
#from django.template import loader
from django.db import connection
from picturesque import models

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
    if request.method == "GET": # получение фильма по if
        pic_id = request.GET.get("id", -1)
        
        try:
            if(pic_id == -1):
                all_pic = models.Picturesque.objects.all()
                return JsonResponse([{"id": picturesque.id, "name": picturesque.name, "genre": picturesque.genre.name, "date of post": picturesque.date} for picturesque in all_pic],safe=False)
            picturesque = models.Picturesque.objects.get(id=pic_id)
            return JsonResponse({"id": picturesque.id, "name": picturesque.name, "genre": picturesque.genre, "date of post": picturesque.date})
        except models.Picturesque.DoesNotExist:
            return JsonResponse({})
        
    elif request.method == "POST":
        name = request.GET.get("name", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})
        genre_name = request.GET.get("genre", None).lower().replace(" ", "")
        # Сохраняем в базу данных
        try:

            picturesque = models.Picturesque()
            try:
                genre = models.Genre.objects.get(name=genre_name)
            except models.Genre.DoesNotExis :
                return JsonResponse({"status": "Such genre does not exist"})
            picturesque.name = name
            picturesque.genre = genre
            #picturesque.date = date
            
            exists = True
            try:
                _ = models.Picturesque.objects.get(name=name, genre=genre)
            except models.Picturesque.DoesNotExist:
                picturesque.save()
                return JsonResponse({"status": "OK"})
            except models.Picturesque.MultipleObjectsReturned:
                pass
            return JsonResponse({"status": "Already exists"})
        except Exception as e:
            print(e)
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")