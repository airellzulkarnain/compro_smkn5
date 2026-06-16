// ── Navbar scroll effect ──────────────────────────────
const navbar = document.getElementById('navbar');
function updateNavbar() {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}
window.addEventListener('scroll', updateNavbar, { passive: true });
updateNavbar();

// ── Mobile menu ───────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
const iconOpen   = document.getElementById('icon-open');
const iconClose  = document.getElementById('icon-close');

if (hamburger) {
  hamburger.addEventListener('click', () => {
    const hidden = mobileMenu.classList.toggle('hidden');
    iconOpen.classList.toggle('hidden', !hidden);
    iconClose.classList.toggle('hidden', hidden);
  });
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      iconOpen.classList.remove('hidden');
      iconClose.classList.add('hidden');
    });
  });
}

// ── Counter animation ─────────────────────────────────
const counters = document.querySelectorAll('[data-count]');
if (counters.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el     = entry.target;
      const target = parseInt(el.dataset.count, 10);
      const duration = 1600;
      const step   = target / (duration / 16);
      let current  = 0;
      const tick   = () => {
        current = Math.min(current + step, target);
        el.textContent = Math.floor(current).toLocaleString('id-ID');
        if (current < target) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });
  counters.forEach(c => observer.observe(c));
}

// ── Scroll-to-top button ──────────────────────────────
const scrollTopBtn = document.getElementById('scrollTop');
if (scrollTopBtn) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none');
    } else {
      scrollTopBtn.classList.add('opacity-0', 'pointer-events-none');
    }
  }, { passive: true });
  scrollTopBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}
