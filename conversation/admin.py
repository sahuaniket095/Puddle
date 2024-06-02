from django.contrib import admin
from .models import conversation,ConversationMessage

admin.site.register(ConversationMessage)
admin.site.register(conversation)