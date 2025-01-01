from django.contrib import admin
from .models import Category,City,Ad

# Register your models here.
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','title','slug')
    search_fields=('title','slug',' parent')
    prepopulated_fields={
        'slug':('title',)
    }

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display=['title','owner','city','category','created_at','status','publish']
    list_filter=['title','status','city','category','created_at']
    search_fields=['title','created_at','overview','description']
    prepopulated_fields={
        'slug':('title',)
    }
    raw_id_fields=['owner','category']
    date_hierarchy='publish'
    ordering=['status','-publish']
    