// ═══ Mobile menu ═══
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    hamburger.classList.toggle('active');
});
navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
    });
});

// ═══ Navbar scroll effect ═══
window.addEventListener('scroll', () => {
    document.getElementById('navbar').classList.toggle('scrolled', window.scrollY > 50);
});

// ═══ Counter animation ═══
const counters = document.querySelectorAll('.stat-item');
const observed = new Set();
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !observed.has(entry.target)) {
            observed.add(entry.target);
            const el = entry.target;
            const target = parseInt(el.dataset.target);
            const numEl = el.querySelector('.stat-number');
            let current = 0;
            const step = Math.max(1, Math.floor(target / 40));
            const interval = setInterval(() => {
                current += step;
                if (current >= target) { current = target; clearInterval(interval); }
                numEl.textContent = current;
            }, 30);
        }
    });
}, { threshold: 0.5 });
counters.forEach(c => observer.observe(c));

// ═══ Forms ═══
function handleForm(formId, statusId) {
    const form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const status = document.getElementById(statusId);
        const data = Object.fromEntries(new FormData(form));
        try {
            const res = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const json = await res.json();
            if (json.ok) {
                status.textContent = '✓ Message sent!';
                status.className = 'form-status ok';
                form.reset();
            } else {
                status.textContent = json.error || 'Error';
                status.className = 'form-status err';
            }
        } catch {
            status.textContent = 'Connection error';
            status.className = 'form-status err';
        }
    });
}
handleForm('contactForm', 'formStatus');
handleForm('sellForm', 'sellFormStatus');

// ═══ Smooth scroll for anchor links ═══
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
