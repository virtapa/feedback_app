from django.contrib import admin
from .models import Feedback #FeedbackTopic
from django.contrib.auth.models import User, auth
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('id', 'topic', 'user','grade','good', 'bad', 'ideas')
    list_filter = ['date', 'topic','grade']
    search_fields = ['grade','good', 'bad', 'ideas']
    
admin.site.register(Feedback, FeedbackAdmin)
                
"""class FeedbackTopicAdmin(admin.ModelAdmin):
    list_display = ('id','topic')
    list_filter = ['topic']
    search_fields = ['topic']

admin.site.register(FeedbackTopic, FeedbackTopicAdmin)"""