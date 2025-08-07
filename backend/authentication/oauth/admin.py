from django.contrib import admin
from .models import OAuthUser

@admin.register(OAuthUser)
class OAuthUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'provider', 'email', 'created_at')
    list_filter = ('provider', 'created_at')
    search_fields = ('user__email', 'email', 'provider_id')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
