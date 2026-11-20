/**
 * Nirogi Lanka Open-Source Clinical Calculators (ESM v2.0.0)
 * Reviewed by Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine)
 * Official Portal: https://nirogilanka.com/en/health-calculators/
 * License: MIT
 */

export function southAsianBMI(weightKg, heightCm) {
  const h = heightCm / 100;
  const bmi = Math.round((weightKg / (h * h)) * 100) / 100;
  const southAsianCategory =
    bmi < 18.5 ? 'Underweight (<18.5)' :
    bmi < 23.0 ? 'Normal / Optimal (18.5–22.9)' :
    bmi < 25.0 ? 'Overweight — South Asian Risk (23.0–24.9)' :
    bmi < 30.0 ? 'Obesity Class I — South Asian (>=25.0)' : 'Obesity Class II (>=30.0)';
  return { bmi, southAsianCategory, url: 'https://nirogilanka.com/en/bmi-calculator/' };
}

export function fib4Index(age, ast, alt, platelets10e9) {
  const fib4 = Math.round(((age * ast) / (platelets10e9 * Math.sqrt(alt))) * 100) / 100;
  const lowCutoff = age >= 65 ? 2.0 : 1.3;
  const risk = fib4 < lowCutoff ? 'Low fibrosis risk (F0–F1)' : fib4 <= 2.67 ? 'Indeterminate' : 'High advanced fibrosis risk (F3–F4)';
  return { fib4, risk, url: 'https://nirogilanka.com/en/fib-4-calculator/' };
}

export function ckdEpi2021Egfr(creatinineMgDl, age, sex = 'male') {
  const fem = String(sex).toLowerCase().startsWith('f');
  const k = fem ? 0.7 : 0.9;
  const a = fem ? -0.241 : -0.302;
  const mult = fem ? 1.012 : 1.0;
  const r = creatinineMgDl / k;
  const egfr = Math.round(142 * Math.pow(Math.min(r, 1), a) * Math.pow(Math.max(r, 1), -1.2) * Math.pow(0.9938, age) * mult * 10) / 10;
  return { egfr, url: 'https://nirogilanka.com/en/egfr-calculator/' };
}

export function sampsonLDL(totalChol, hdl, tg) {
  const nonHdl = totalChol - hdl;
  const ldl = Math.round(((totalChol / 0.948) - (hdl / 0.971) - ((tg / 8.56) + ((tg * nonHdl) / 2140) - ((tg * tg) / 16100)) - 9.44) * 10) / 10;
  return { sampsonLdl: ldl, nonHdl, url: 'https://nirogilanka.com/en/ldl-cholesterol-calculator/' };
}

export function homaIR(fastingGlucoseMgDl, fastingInsulinUiuMl) {
  const homa = Math.round(((fastingGlucoseMgDl * fastingInsulinUiuMl) / 405) * 100) / 100;
  return { homaIr: homa, url: 'https://nirogilanka.com/en/insulin-resistance-calculator/' };
}
