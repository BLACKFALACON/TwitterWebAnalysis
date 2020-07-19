from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['dosyaNumarası','user','hastag','time']

class TweetsAdmin(admin.ModelAdmin):
    list_display = ['userName','hastag','tweet','time']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['user','konu','mesaj','time']

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['Auser','Akonu','Amesaj','time']


admin.site.register(Post,PostAdmin)
admin.site.register(Tweets,TweetsAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Analysis,AnalysisAdmin)