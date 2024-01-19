from django.contrib import admin
from .models import trial,client,search,festival,package,payments

# Register your models here.

admin.site.register(trial)
admin.site.register(client)
admin.site.register(festival)
admin.site.register(search)
admin.site.register(package)
admin.site.register(payments)
