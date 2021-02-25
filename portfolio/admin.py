from django.contrib import admin
from .models import Images
from .models import Photo, Location, Category


class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)


# Register your models here.
admin.site.register(Location)
admin.site.register(Photo, admin_class=PhotoAdmin)
admin.site.register(Category)
admin.site.register(Images)
