from django.contrib.auth.models import User

try: 
    User.objects.create_superuser('admin', 'test@mail.ru', 'admin')
except:
    pass