from django.contrib import admin

from .models import Genres, MusicModel

# Register your models here.
# class UserTaxExemptInline(admin.TabularInline):
#     model = MusicModel
# class MusicInline(admin.StackedInline):
#     model = MusicModel
#     fields = ('title',)
#     fk_name = 'genre'


# @admin.register(MusicModel)
# class MusicAdmin(admin.ModelAdmin):
#     inlines = [MusicInline]
#     list_display = ["title", "genre", "created_at"]
#     list_filter = ["title"]

admin.site.register(Genres)
admin.site.register(MusicModel)
