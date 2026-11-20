"""
Trilingual (English–Sinhala–Tamil) Clinical Medical Terminology & ICD-10 Mapping
Official Dataset: https://nirogilanka.com/medical-glossary/
DOI: https://doi.org/10.5281/zenodo.24028706
"""
from typing import Dict, List

CLINICAL_ICD10_GLOSSARY: List[Dict[str, str]] = [
    {"icd10": "E11", "en": "Type 2 Diabetes Mellitus", "si": "දෙවන වර්ගයේ දියවැඩියාව", "ta": "வகை 2 நீரிழிவு நோய்", "url": "https://nirogilanka.com/en/diabetes/"},
    {"icd10": "A90", "en": "Dengue Fever", "si": "ඩෙංගු උණ", "ta": "டெங்கு காய்ச்சல்", "url": "https://nirogilanka.com/en/dengue-fever/"},
    {"icd10": "I10", "en": "Essential Hypertension", "si": "අධි රුධිර පීඩනය", "ta": "உயர் இரத்த அழுத்தம்", "url": "https://nirogilanka.com/en/high-blood-pressure/"},
    {"icd10": "N18", "en": "Chronic Kidney Disease", "si": "නිදන්ගත වකුගඩු රෝගය", "ta": "நாள்பட்ட சிறுநீரக நோய்", "url": "https://nirogilanka.com/en/chronic-kidney-disease/"},
    {"icd10": "I64", "en": "Stroke (Cerebrovascular Accident)", "si": "ආඝාතය (අංශභාගය)", "ta": "பக்கவாதம்", "url": "https://nirogilanka.com/en/stroke/"},
    {"icd10": "I21", "en": "Acute Myocardial Infarction", "si": "හෘදයාබාධය", "ta": "மாரடைப்பு", "url": "https://nirogilanka.com/en/heart-attack/"},
    {"icd10": "J45", "en": "Bronchial Asthma", "si": "ඇදුම රෝගය", "ta": "ஆஸ்துமா", "url": "https://nirogilanka.com/en/asthma/"},
    {"icd10": "K29", "en": "Gastritis", "si": "ගැස්ට්‍රයිටිස් (ආමාශ ප්‍රදාහය)", "ta": "இரைப்பை அழற்சி", "url": "https://nirogilanka.com/en/gastritis/"},
    {"icd10": "G43", "en": "Migraine", "si": "ඉරුවාරදය (මයිග්‍රේන්)", "ta": "ஒற்றைத் தலைவலி", "url": "https://nirogilanka.com/en/migraine/"},
    {"icd10": "D50", "en": "Iron Deficiency Anemia", "si": "යකඩ ඌනතා රක්තහීනතාවය", "ta": "இரத்த சோகை", "url": "https://nirogilanka.com/en/anemia/"},
    {"icd10": "G40", "en": "Epilepsy", "si": "අපස්මාරය (මීමැස්මොරය)", "ta": "வலிப்பு நோய்", "url": "https://nirogilanka.com/en/epilepsy/"},
    {"icd10": "K64", "en": "Hemorrhoids", "si": "අර්ශස් රෝගය", "ta": "மூல நோய்", "url": "https://nirogilanka.com/en/hemorrhoids/"},
    {"icd10": "K76.0", "en": "Fatty Liver Disease (MASLD)", "si": "අක්මාවේ මේදය තැන්පත් වීම", "ta": "கல்லீரல் கொழுப்பு நோய்", "url": "https://nirogilanka.com/en/fatty-liver-disease/"},
    {"icd10": "E05", "en": "Hyperthyroidism", "si": "අතිතයිරොයිඩතාවය", "ta": "அதிதைராய்டு", "url": "https://nirogilanka.com/en/hyperthyroidism/"},
    {"icd10": "N20", "en": "Kidney Stone Disease (Nephrolithiasis)", "si": "වකුගඩු ගල්", "ta": "சிறுநீரக கற்கள்", "url": "https://nirogilanka.com/en/kidney-stones/"},
    {"icd10": "N39.0", "en": "Urinary Tract Infection (UTI)", "si": "මුත්‍රා ආසාදනය", "ta": "சிறுநீர் பாதை நோய்த்தொற்று", "url": "https://nirogilanka.com/en/urinary-tract-infection/"},
    {"icd10": "J03", "en": "Acute Tonsillitis", "si": "සෙම්ගෙඩි ප්‍රදාහය", "ta": "டான்சில் அழற்சி", "url": "https://nirogilanka.com/en/tonsillitis/"},
    {"icd10": "A09", "en": "Infectious Gastroenteritis", "si": "ආමාශ ආන්ත්‍රික ප්‍රදාහය", "ta": "இரைப்பை குடல் அழற்சி", "url": "https://nirogilanka.com/en/gastroenteritis/"},
    {"icd10": "M17", "en": "Osteoarthritis of Knee", "si": "ඔස්ටියෝආතරයිටිස් (අස්ථි සන්ධි ප්‍රදාහය)", "ta": "மூட்டு தேய்மானம்", "url": "https://nirogilanka.com/en/osteoarthritis/"},
    {"icd10": "G96.0", "en": "Cerebrospinal Fluid (CSF) Leak", "si": "මස්තිෂ්ක සුෂුම්නා තරල කාන්දුව", "ta": "மூளை முதுகுத் தண்டுவட திரவ கசிவு", "url": "https://nirogilanka.com/en/cerebrospinal-fluid-csf-leak/"},
]


def lookup_icd10_term(query: str) -> List[Dict[str, str]]:
    """Search ICD-10 code or English / Sinhala / Tamil clinical term."""
    q = str(query or "").strip().lower()
    if not q:
        return CLINICAL_ICD10_GLOSSARY
    return [
        row for row in CLINICAL_ICD10_GLOSSARY
        if q in row["icd10"].lower()
        or q in row["en"].lower()
        or q in row["si"]
        or q in row["ta"]
    ]
