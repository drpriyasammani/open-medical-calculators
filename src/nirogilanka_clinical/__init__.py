"""
nirogilanka_clinical — Evidence-Based Clinical Calculators & Multilingual ICD-10 Medical Terminology
Curated by Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine)
Official Portal: https://nirogilanka.com/en/health-calculators/
"""
from .calculators import (
    south_asian_bmi,
    fib4_index,
    ckd_epi_2021_egfr,
    sampson_ldl,
    homa_ir,
    corrected_calcium,
    ganzoni_iron_deficit,
)
from .glossary import CLINICAL_ICD10_GLOSSARY, lookup_icd10_term

__version__ = "2.0.0"
__author__ = "Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine)"
__homepage__ = "https://nirogilanka.com/en/health-calculators/"

__all__ = [
    "south_asian_bmi",
    "fib4_index",
    "ckd_epi_2021_egfr",
    "sampson_ldl",
    "homa_ir",
    "corrected_calcium",
    "ganzoni_iron_deficit",
    "CLINICAL_ICD10_GLOSSARY",
    "lookup_icd10_term",
]
