from django.contrib import admin

# Register your models here.

from .models import Lead, GalleryImage

admin.site.register(Lead)
admin.site.register(GalleryImage)
