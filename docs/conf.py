project = "Nirogi Lanka Clinical Calculators & ICD-10 Terminology"
copyright = "2026, Dr. Priya Sammani (MBBS, PG Dip. in Family Medicine) — Nirogi Lanka"
author = "Dr. Priya Sammani"
release = "2.0.0"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "alabaster"
html_theme_options = {
    "description": "Evidence-based South Asian & WHO clinical formulas and trilingual medical glossary.",
    "github_user": "drpriyasammani",
    "github_repo": "open-medical-calculators",
}
