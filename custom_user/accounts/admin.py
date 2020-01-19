from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ('first_name', 'email', 'mobile_number')

    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('mobile_number','profile_picture')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'mobile_number', 'email',
                       'gender', 'dob', 'address', 'profile_picture', 'city',
                       'is_staff', 'is_active', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


