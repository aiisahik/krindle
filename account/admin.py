from django.contrib import admin
from models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('id', 'user', 'gender', 'relationship_status')
    list_display = ('id', 'user', 'gender', 'relationship_status')
    list_display_links = ('id', 'user', 'gender', 'relationship_status')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)