from django.contrib import admin
from .models import Genre, Movies

class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class MoviesAdmin(admin.ModelAdmin):
    exclude = ("date_created", )
    list_display = ("title","release_year","number_in_stock","daily_rate", )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies,MoviesAdmin)

# Register your models here.
