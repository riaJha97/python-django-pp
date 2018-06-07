from django.contrib import admin
from .models import Movie, Cinema
# Register your models here, provide admin interface to a model by adding the lines below

# from .models import Question

admin.site.register(Movie)
admin.site.register(Cinema)
