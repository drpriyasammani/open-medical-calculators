Nirogi Lanka Clinical Calculators & Multilingual ICD-10 Library (v2.0)
======================================================================

Open-source Python and JavaScript clinical medical equations, adult hematology/biochemistry reference intervals, and trilingual (English–Sinhala–Tamil) ICD-10 medical terminology curated by **Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine)** at the `Nirogi Lanka Medical Encyclopedia <https://nirogilanka.com/en/>`_.

Official Clinical Portals & Permanent Identifiers
-------------------------------------------------

* **77 Interactive Clinical Calculators Hub:** `https://nirogilanka.com/en/health-calculators/ <https://nirogilanka.com/en/health-calculators/>`_
* **130-Language Symptom Triage Checker:** `https://nirogilanka.com/en/symptom-checker/ <https://nirogilanka.com/en/symptom-checker/>`_
* **Standardized Trilingual Medical Glossary (CSV / JSON):** `https://nirogilanka.com/medical-glossary/ <https://nirogilanka.com/medical-glossary/>`_
* **Clinical Review Series & Open Data Hub:** `https://nirogilanka.com/en/research/ <https://nirogilanka.com/en/research/>`_
* **CERN Zenodo Software DOI:** `10.5281/zenodo.24336278 <https://doi.org/10.5281/zenodo.24336278>`_
* **Center for Open Science (OSF DOI):** `10.17605/OSF.IO/WDH4C <https://doi.org/10.17605/OSF.IO/WDH4C>`_
* **Author ORCID iD:** `0009-0009-5051-1275 <https://orcid.org/0009-0009-5051-1275>`_
* **Wikidata Knowledge Graph Entity:** `Q142108990 (Nirogi Lanka) <https://www.wikidata.org/wiki/Q142108990>`_

Validated Clinical Calculator Specifications
--------------------------------------------

1. **South Asian vs. Global WHO BMI Stratification** (`Live BMI Calculator <https://nirogilanka.com/en/bmi-calculator/>`_)
   Implements WHO Asia-Pacific cardiometabolic thresholds (Overweight >= 23.0 kg/m², Obesity >= 25.0 kg/m²) alongside standard WHO cutoffs.

2. **Sterling FIB-4 Liver Fibrosis Index** (`Live FIB-4 Calculator <https://nirogilanka.com/en/fib-4-calculator/>`_)
   Non-invasive staging of hepatic fibrosis in MASLD / NAFLD and chronic viral hepatitis with age-adjusted cutoffs (< 1.30 vs. < 2.00 for age >= 65).

3. **Race-Free 2021 NKF/ASN CKD-EPI eGFR** (`Live eGFR Calculator <https://nirogilanka.com/en/egfr-calculator/>`_)
   Estimates glomerular filtration rate (mL/min/1.73m²) mapped to KDIGO G1–G5 chronic kidney disease stages.

4. **2020 NIH Sampson LDL-Cholesterol** (`Live LDL Calculator <https://nirogilanka.com/en/ldl-cholesterol-calculator/>`_)
   Accurate beta-quantification LDL-C estimation across hypertriglyceridemic states up to 800 mg/dL.

5. **HOMA-IR Insulin Resistance Index** (`Live HOMA-IR Calculator <https://nirogilanka.com/en/insulin-resistance-calculator/>`_)
   Evaluates fasting beta-cell demand and insulin sensitivity from fasting glucose and insulin.

6. **Payne Albumin-Corrected Calcium & Ganzoni Total Iron Deficit**
   * `Corrected Calcium Calculator <https://nirogilanka.com/en/corrected-calcium-calculator/>`_
   * `Ganzoni Iron Deficit Calculator <https://nirogilanka.com/en/iron-deficit-calculator/>`_
   * `WHO / Sri Lanka CHDR Baby Growth Percentile Calculator <https://nirogilanka.com/baby-growth-percentile-calculator/>`_

Installation & Usage
--------------------

.. code-block:: bash

   pip install git+https://github.com/drpriyasammani/open-medical-calculators.git

.. code-block:: python

   from nirogilanka_clinical import south_asian_bmi, fib4_index, ckd_epi_2021_egfr, lookup_icd10_term

   print(south_asian_bmi(68, 168))
   print(fib4_index(age=52, ast_u_l=48, alt_u_l=42, platelets_10e9_l=165))
   print(ckd_epi_2021_egfr(creatinine_mg_dl=1.1, age=58, sex="female"))
   print(lookup_icd10_term("dengue"))

Embed Any Calculator on Your Clinic or University Website
---------------------------------------------------------

Every interactive calculator on Nirogi Lanka supports a distraction-free, ad-free ``?embed=1`` mode:

.. code-block:: html

   <iframe src="https://nirogilanka.com/en/bmi-calculator/?embed=1" width="100%" height="660" style="border:1px solid #cbd5e1;border-radius:16px;" loading="lazy"></iframe>
   <p>Powered by <a href="https://nirogilanka.com/en/bmi-calculator/">Nirogi Lanka Clinical Calculators</a></p>
