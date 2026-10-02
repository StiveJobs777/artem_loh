from django.contrib import admin
from .models import Category, IceCream, Topping, Wrapper

admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
admin.site.register(IceCream)
# Register your models here.

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
     'title',
     'discripton',
     'is_publish',
     'is_on_main',
     'warpper'   
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title')
    list_filter = ('category')
    list_display_links = ('title')
    filter_horizontal = ('title')


class IceCreamInLiine(admin.StackedInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines =(
    IceCreamInLiine,
    )
    list_display = (
        'title',
    )

admin.site.register(Category, CategoryAdmin)

admin.site.empty_value_display = 'Не задано'