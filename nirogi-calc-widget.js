(function () {
  var containers = document.querySelectorAll('[data-nirogi-calc]');
  containers.forEach(function (el) {
    if (el.dataset.nirogiMounted) return;
    el.dataset.nirogiMounted = '1';
    var lang = (el.getAttribute('data-lang') || 'en').trim();
    var prefix = lang === 'si' ? '' : '/' + lang;
    el.innerHTML =
      '<div style="max-width:420px;font-family:system-ui,-apple-system,sans-serif;border:1.5px solid #cbd5e1;border-radius:16px;padding:18px;background:#fff;box-shadow:0 6px 20px rgba(15,23,42,.06);color:#0f172a;">' +
      '<div style="font-weight:800;font-size:1.05rem;margin-bottom:10px;">⚖️ Clinical BMI & Healthy Weight Calculator</div>' +
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px;">' +
      '<label style="font-size:.8rem;font-weight:700;color:#475569;">Height (cm)<input type="number" class="nl-w-h" placeholder="170" style="width:100%;margin-top:4px;padding:8px;border:1px solid #cbd5e1;border-radius:8px;box-sizing:border-box;"/></label>' +
      '<label style="font-size:.8rem;font-weight:700;color:#475569;">Weight (kg)<input type="number" class="nl-w-w" placeholder="68" style="width:100%;margin-top:4px;padding:8px;border:1px solid #cbd5e1;border-radius:8px;box-sizing:border-box;"/></label>' +
      '</div>' +
      '<button type="button" class="nl-w-btn" style="width:100%;padding:10px;border:none;border-radius:10px;background:#0d9488;color:#fff;font-weight:800;cursor:pointer;">Calculate BMI</button>' +
      '<div class="nl-w-res" style="display:none;margin-top:12px;padding:10px;border-radius:10px;background:#f0fdfa;border:1px solid #99f6e4;font-size:.9rem;font-weight:700;"></div>' +
      '<div style="margin-top:10px;font-size:.74rem;color:#64748b;text-align:right;">Powered by <a href="https://nirogilanka.com' + prefix + '/bmi-calculator/" target="_blank" rel="noopener" style="color:#0f766e;font-weight:700;text-decoration:none;">Nirogi Lanka Clinical Tools</a></div>' +
      '</div>';
    var btn = el.querySelector('.nl-w-btn');
    btn.addEventListener('click', function () {
      var h = parseFloat(el.querySelector('.nl-w-h').value) / 100;
      var w = parseFloat(el.querySelector('.nl-w-w').value);
      var out = el.querySelector('.nl-w-res');
      if (!h || !w || h <= 0.4 || w <= 5) return;
      var bmi = (w / (h * h)).toFixed(1);
      var cat = bmi < 18.5 ? 'Underweight' : bmi < 25 ? 'Normal Healthy Weight' : bmi < 30 ? 'Overweight' : 'Obesity Class';
      out.style.display = 'block';
      out.textContent = 'BMI: ' + bmi + ' kg/m² — ' + cat;
    });
  });
})();
