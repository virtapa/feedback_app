from django.contrib import admin
from .models import Feedback
from django.contrib.auth.models import User, auth
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','grade','good', 'bad', 'ideas')
    list_filter = ['date','topic','grade']
    search_fields = ['topic','grade','good', 'bad', 'ideas']
    
admin.site.register(Feedback, FeedbackAdmin)
                
