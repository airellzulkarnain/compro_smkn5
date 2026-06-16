from django.shortcuts import render, get_object_or_404
from .models import SiteConfig, Program, News, Achievement, Gallery, Extracurricular

FACILITIES = [
    ('Laboratorium Komputer',   'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z'),
    ('Perpustakaan',            'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253'),
    ('Bengkel / Workshop',      'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z'),
    ('Aula Serbaguna',          'M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4'),
    ('Lapangan Olahraga',       'M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z'),
    ('Mushola',                 'M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9'),
    ('Kantin',                  'M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z'),
    ('UKS',                     'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z'),
]

DEFAULT_MISSIONS = [
    'Menyelenggarakan pendidikan vokasi berbasis kompetensi yang relevan dengan kebutuhan industri',
    'Membentuk peserta didik yang berakhlak mulia, disiplin, dan berjiwa Pancasila',
    'Mengembangkan kemitraan strategis dengan dunia usaha dan dunia industri (DUDI)',
    'Menciptakan lingkungan belajar yang kondusif, inovatif, dan berbasis teknologi',
    'Meningkatkan kompetensi dan profesionalisme tenaga pendidik secara berkelanjutan',
]


def _base_context():
    return {'config': SiteConfig.objects.first()}


def home(request):
    ctx = _base_context()
    ctx.update({
        'programs': Program.objects.filter(is_active=True),
        'news': News.objects.filter(is_published=True)[:3],
        'achievements': Achievement.objects.all()[:6],
        'gallery': Gallery.objects.all()[:8],
        'ekskul': Extracurricular.objects.all(),
        'facilities_data': FACILITIES,
        'default_missions': DEFAULT_MISSIONS,
        'placeholder_range': range(6),
    })
    return render(request, 'core/home.html', ctx)


def news_list(request):
    ctx = _base_context()
    ctx['news_list'] = News.objects.filter(is_published=True)
    return render(request, 'core/news_list.html', ctx)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    ctx = _base_context()
    ctx['news'] = news
    ctx['recent_news'] = News.objects.filter(is_published=True).exclude(pk=news.pk)[:3]
    return render(request, 'core/news_detail.html', ctx)
