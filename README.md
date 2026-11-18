# Open Multilingual Clinical Calculators & Adult Laboratory Reference Dataset (2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)
[![Medically Reviewed](https://img.shields.io/badge/Medically_Reviewed-Dr._Priya_Sammani_(MBBS)-7c3aed.svg)](https://nirogilanka.com/about/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--5051--1275-a6ce39.svg)](https://orcid.org/0009-0009-5051-1275)
[![Live Clinical Suite](https://img.shields.io/badge/Live_Tools-nirogilanka.com-0d9488.svg)](https://nirogilanka.com/en/health-calculators/)

Open-source clinical equations, 1-line embeddable medical calculator widget, and standardized adult laboratory reference intervals (SI & conventional units) maintained by the **Nirogi Lanka Clinical Engineering & Medical Review Team**, led by **Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine)**.

---

## Live Interactive Clinical Tools (21 Languages)

All 76 clinical calculators and the 118-symptom differential triage engine are freely accessible without registration:

- **English (Global):** [Clinical Health Calculators](https://nirogilanka.com/en/health-calculators/) · [Interactive Symptom Checker](https://nirogilanka.com/en/symptom-checker/) · [BMI Calculator](https://nirogilanka.com/en/bmi-calculator/) · [eGFR Kidney Calculator](https://nirogilanka.com/en/egfr-calculator/)
- **Sinhala (සිංහල):** [සෞඛ්‍ය ගණක යන්ත්‍ර](https://nirogilanka.com/health-calculators/) · [රෝග ලක්ෂණ පරීක්ෂකය](https://nirogilanka.com/symptom-checker/)
- **Deutsch:** [Medizinische Rechner](https://nirogilanka.com/de/health-calculators/) · [Symptom-Checker](https://nirogilanka.com/de/symptom-checker/)
- **Français:** [Calculateurs Médicaux](https://nirogilanka.com/fr/health-calculators/) · [Vérificateur de Symptômes](https://nirogilanka.com/fr/symptom-checker/)
- **Svenska:** [Hälsokalkylatorer](https://nirogilanka.com/sv/health-calculators/) · [Symtomkontroll](https://nirogilanka.com/sv/symptom-checker/)
- **Norsk:** [Helsekalkulatorer](https://nirogilanka.com/no/health-calculators/) · [Symptomvelger](https://nirogilanka.com/no/symptom-checker/)
- **Dansk:** [Sundhedsberegnere](https://nirogilanka.com/da/health-calculators/) · [Symptomtjekker](https://nirogilanka.com/da/symptom-checker/)
- **Nederlands:** [Medische Calculators](https://nirogilanka.com/nl/health-calculators/) · [Symptoomchecker](https://nirogilanka.com/nl/symptom-checker/)
- **Suomi:** [Terveyslaskurit](https://nirogilanka.com/fi/health-calculators/) · [Oirearvio](https://nirogilanka.com/fi/symptom-checker/)
- **Español:** [Calculadoras de Salud](https://nirogilanka.com/es/health-calculators/) · [Verificador de Síntomas](https://nirogilanka.com/es/symptom-checker/)
- **Italiano:** [Calcolatori Medici](https://nirogilanka.com/it/health-calculators/) · [Controllo Sintomi](https://nirogilanka.com/it/symptom-checker/)
- **Português:** [Calculadoras de Saúde](https://nirogilanka.com/pt/health-calculators/) · [Verificador de Sintomas](https://nirogilanka.com/pt/symptom-checker/)
- **日本語:** [医療・健康計算ツール](https://nirogilanka.com/ja/health-calculators/) · [症状チェッカー](https://nirogilanka.com/ja/symptom-checker/)
- **한국어:** [건강 계산기](https://nirogilanka.com/ko/health-calculators/) · [증상 체커](https://nirogilanka.com/ko/symptom-checker/)
- **繁體中文:** [臨床健康計算機](https://nirogilanka.com/zh-TW/health-calculators/) · [症狀檢查器](https://nirogilanka.com/zh-TW/symptom-checker/)
- **עברית:** [מחשבוני בריאות](https://nirogilanka.com/iw/health-calculators/) · [בודק תסמינים](https://nirogilanka.com/iw/symptom-checker/)

---

## Embed Free Clinical Calculators on Any Clinic or Health Website

Health educators, medical blogs, and clinics can embed our zero-dependency calculator widget (BMI, CKD-EPI 2021 eGFR, Mifflin-St Jeor BMR, HbA1c-to-eAG) with a single HTML snippet:

```html
<div data-nirogi-calc="bmi" data-lang="en"></div>
<script src="https://nirogilanka.com/embed/nirogi-calc-widget.js" async></script>
```

---

## Included Open Clinical Reference Dataset

`clinical-lab-reference-ranges-2026.json` provides structured, machine-readable adult normal, borderline, and critical clinical thresholds across 25 core biomarkers (HbA1c, Fasting Glucose, eGFR CKD-EPI 2021, Serum Creatinine, TSH, Free T4, Ferritin, Hemoglobin, MCV, RDW, Platelets, ALT/SGPT, AST, ALP, Total/LDL/HDL Cholesterol, Triglycerides, ApoB, Lp(a), hs-CRP, ESR, UACR, Vitamin D 25-OH, Vitamin B12).

Live JSON endpoint: `https://nirogilanka.com/datasets/clinical-lab-reference-ranges-2026.json`

---

## Citation

If you use this dataset or calculator formulas in academic, clinical informatics, or patient-education work, please cite:

> Sammani, P. (2026). *Nirogi Lanka Open Multilingual Clinical Calculators & Standardized Adult Laboratory Reference Dataset (v2026.11)*. Nirogi Lanka Medical Organization. https://nirogilanka.com/en/health-calculators/
