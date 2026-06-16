from django.db import models
from django.utils.text import slugify


class SiteConfig(models.Model):
    school_name = models.CharField(max_length=200, default='SMKN 5 Kota Tangerang')
    tagline = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True, help_text='Satu misi per baris')
    logo = models.ImageField(upload_to='logo/', blank=True)
    hero_image = models.ImageField(upload_to='hero/', blank=True)
    total_students = models.PositiveIntegerField(default=0)
    total_teachers = models.PositiveIntegerField(default=0)
    founded_year = models.PositiveIntegerField(default=2003)
    accreditation = models.CharField(max_length=10, default='A')
    maps_embed_url = models.TextField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Konfigurasi Situs'
        verbose_name_plural = 'Konfigurasi Situs'

    def __str__(self):
        return self.school_name

    def get_missions(self):
        return [m.strip() for m in self.mission.splitlines() if m.strip()]


class Program(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='programs/', blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Program Keahlian'
        verbose_name_plural = 'Program Keahlian'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='news/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Berita'
        verbose_name_plural = 'Berita'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug, n = base, 1
            while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_excerpt(self):
        if self.excerpt:
            return self.excerpt
        return (self.content[:197] + '...') if len(self.content) > 200 else self.content


class Achievement(models.Model):
    LEVEL_CHOICES = [
        ('kota', 'Tingkat Kota'),
        ('provinsi', 'Tingkat Provinsi'),
        ('nasional', 'Tingkat Nasional'),
        ('internasional', 'Tingkat Internasional'),
    ]
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='achievements/', blank=True)

    class Meta:
        ordering = ['-year', 'title']
        verbose_name = 'Prestasi'
        verbose_name_plural = 'Prestasi'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, default='Umum')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return self.title


class Extracurricular(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ekskul/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Ekstrakurikuler'
        verbose_name_plural = 'Ekstrakurikuler'

    def __str__(self):
        return self.name
