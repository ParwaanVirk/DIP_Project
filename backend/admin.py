from django.contrib import admin
from backend.models import TransData, Transformer
# Register your models here.


admin.site.register(Transformer)
admin.site.register(TransData)