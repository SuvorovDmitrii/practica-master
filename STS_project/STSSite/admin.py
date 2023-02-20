from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Uslugi)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Персональная информация', {
            'fields': ('first_name', 'last_name', 'patronomyc', 'avatar')}
        ),
        ('Остальная информация',
            {
                'classes': ('wide',),
                'fields': ('email', 'username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined'), }
        ),
    )
admin.site.register(Status)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'view_usluga', 'date_to', 'time_order', 'status')

    @admin.display()
    def view_usluga(self, obj):
        return ('%s' % (obj.usluga)).upper()
# Register your models here.
