from django.contrib import admin
from .models import SiteConfig, Program, News, Achievement, Gallery, Extracurricular


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'phone', 'email', 'accreditation']
    fieldsets = [
        ('Informasi Sekolah', {'fields': ['school_name', 'tagline', 'description', 'founded_year', 'accreditation', 'logo', 'hero_image']}),
        ('Kontak', {'fields': ['address', 'phone', 'email']}),
        ('Visi & Misi', {'fields': ['vision', 'mission']}),
        ('Statistik', {'fields': ['total_students', 'total_teachers']}),
        ('Media Sosial', {'fields': ['instagram_url', 'facebook_url', 'youtube_url']}),
        ('Google Maps', {'fields': ['maps_embed_url']}),
    ]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'level']
    list_filter = ['level', 'year']
    search_fields = ['title']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_editable = ['order']


@admin.register(Extracurricular)
class ExtracurricularAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
