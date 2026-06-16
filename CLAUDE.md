# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Company profile website for **SMKN 5 Kota Tangerang** (a state vocational high school). Built with Django + SQLite, Django templates, Tailwind CSS (CDN), and vanilla JavaScript.

## Common Commands

```bash
source venv/bin/activate      # activate virtualenv

python manage.py runserver    # dev server at localhost:8000
python manage.py migrate      # apply migrations
python manage.py makemigrations core  # after changing models
python manage.py seed_data    # seed initial school data (run once)
python manage.py createsuperuser      # create admin user

# Run a single test
python manage.py test core.tests.TestClassName.test_method

# Collect static (production only)
python manage.py collectstatic
```

## Architecture

```
config/          # Django project: settings, root urls, wsgi
core/            # Main app — all school content lives here
  models.py      # SiteConfig, Program, News, Achievement, Gallery, Extracurricular
  views.py       # home, news_list, news_detail
  admin.py       # Admin registration for all models
  urls.py        # Mounted at "/" in config/urls.py
  management/commands/seed_data.py  # One-shot seed command
templates/
  base.html         # Sticky navbar + footer, Tailwind CDN, Poppins font
  core/home.html    # Single-page homepage (all sections)
  core/news_list.html
  core/news_detail.html
static/js/main.js   # Navbar scroll, mobile menu, counter animation, scroll-to-top
```

## Key Patterns

**SiteConfig singleton** — `SiteConfig.objects.first()` is passed as `config` to every view. All school-wide settings (name, address, vision/mission, social links) live there; mission field is newline-delimited and split via `config.get_missions()`.

**Facilities** — hardcoded in `views.py` as `FACILITIES` (list of `(name, svg_path)` tuples) and passed as `facilities_data`. No model needed.

**Default missions** — `DEFAULT_MISSIONS` list in `views.py` used as template fallback when `SiteConfig` has no mission text.

**News slugs** — auto-generated from title on first save with collision handling in `News.save()`.

**Tailwind** — uses CDN Play CDN with custom config block defining `primary` (navy `#1a3b6e`) and `accent` (amber `#f59e0b`) colors. No build step required.

**Navbar behavior** — transparent over hero, transitions to white (`#navbar.scrolled`) after 60px scroll via JS in `static/js/main.js`.

## Content Management

All content is managed via Django Admin at `/admin/`. After running `seed_data`, update `SiteConfig` with:
- Real address, phone, email
- Google Maps embed URL (iframe src value only)
- Social media URLs
- Upload logo and hero image

Programs, news, achievements, and gallery photos are all managed through admin.
