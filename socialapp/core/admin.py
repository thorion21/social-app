from django.contrib import admin
from .models import Post, Comment, UserProfile, Country
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['text', 'created_by']
    list_filter = ('created_by',)
    list_display = ['created_by', 'text', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['text', 'post']
    list_filter = ('created_by', 'post')
    list_display = ['created_by', 'text', 'post']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username','get_firstname', 'get_lastname', 'get_country',)
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'country__name']
    list_filter = ('user__is_superuser', 'country__name')

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'

    def get_country(self, obj):
        return obj.country.name

    get_country.short_description = 'Country'
    get_country.admin_order_field = 'country__name'

    def get_firstname(self, obj):
        return obj.user.first_name

    get_firstname.short_description = 'FirstName'
    get_firstname.admin_order_field = 'user__first_name'

    def get_lastname(self, obj):
        return obj.user.last_name

    get_lastname.short_description = 'LastName'
    get_firstname.admin_order_field = 'user__last_name'


class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ['code', 'name']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
