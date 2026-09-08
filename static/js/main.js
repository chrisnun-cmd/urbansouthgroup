// Curtain loader
window.addEventListener('load', () => {
  setTimeout(() => {
    const curtain = document.getElementById('curtain');
    if (curtain) curtain.classList.add('lift');
  }, 1400);
});

// Nav scrolled state
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 100) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  });
}

// Sell form
const sellForm = document.getElementById('sellForm');
if (sellForm) {
  sellForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
      name: sellForm.querySelector('[name=name]').value,
      email: sellForm.querySelector('[name=email]').value,
      message: sellForm.querySelector('[name=message]').value,
    };
    try {
      const r = await fetch('/api/contact', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data),
      });
      const j = await r.json();
      if (j.ok) {
        sellForm.innerHTML = '<p style="font-family:var(--f-display); font-style:italic; font-size:1.4rem; color:var(--gold); text-align:center; padding:2rem;">Message received. We will be in touch shortly.</p>';
      } else {
        alert(j.error || 'Error');
      }
    } catch (err) { alert('Network error'); }
  });
}
