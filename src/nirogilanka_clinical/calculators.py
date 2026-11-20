"""
Validated Clinical Risk & Laboratory Calculators
Reference Portal: https://nirogilanka.com/en/health-calculators/
"""
from typing import Dict, Union


def south_asian_bmi(weight_kg: float, height_cm: float) -> Dict[str, Union[float, str]]:
    """
    Compute Body Mass Index (BMI) with both WHO Asia-Pacific / South Asian cutoffs
    (Overweight >= 23.0 kg/m^2, Obesity >= 25.0 kg/m^2) and Global WHO cutoffs.
    Live Web Tool: https://nirogilanka.com/en/bmi-calculator/
    """
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("weight_kg and height_cm must be positive numbers.")
    h_m = height_cm / 100.0
    bmi = round(weight_kg / (h_m * h_m), 2)

    if bmi < 18.5:
        sa_cat, global_cat = "Underweight (<18.5)", "Underweight (<18.5)"
    elif bmi < 23.0:
        sa_cat, global_cat = "Normal / Optimal (18.5–22.9)", "Normal (18.5–24.9)"
    elif bmi < 25.0:
        sa_cat, global_cat = "Overweight — Increased Cardiometabolic Risk (23.0–24.9)", "Normal (18.5–24.9)"
    elif bmi < 30.0:
        sa_cat, global_cat = "Obesity Class I — South Asian Cutoff (>=25.0)", "Overweight (25.0–29.9)"
    else:
        sa_cat, global_cat = "Obesity Class II (>=30.0)", "Obesity (>=30.0)"

    return {
        "bmi": bmi,
        "south_asian_category": sa_cat,
        "global_who_category": global_cat,
        "reference_url": "https://nirogilanka.com/en/bmi-calculator/",
    }


def fib4_index(age: float, ast_u_l: float, alt_u_l: float, platelets_10e9_l: float) -> Dict[str, Union[float, str]]:
    """
    Compute Sterling FIB-4 Liver Fibrosis Index for MASLD / NAFLD & viral hepatitis staging.
    Formula: (Age * AST) / (Platelets * sqrt(ALT))
    Live Web Tool: https://nirogilanka.com/en/fib-4-calculator/
    """
    if age <= 0 or ast_u_l <= 0 or alt_u_l <= 0 or platelets_10e9_l <= 0:
        raise ValueError("All clinical inputs must be positive.")
    score = round((age * ast_u_l) / (platelets_10e9_l * (alt_u_l ** 0.5)), 2)
    low_cutoff = 2.0 if age >= 65 else 1.30
    if score < low_cutoff:
        risk = "Low risk of advanced fibrosis (F0–F1)"
    elif score <= 2.67:
        risk = "Indeterminate risk — consider FibroScan / elastography"
    else:
        risk = "High probability of advanced liver fibrosis / cirrhosis (F3–F4)"
    return {
        "fib4": score,
        "interpretation": risk,
        "reference_url": "https://nirogilanka.com/en/fib-4-calculator/",
    }


def ckd_epi_2021_egfr(creatinine_mg_dl: float, age: float, sex: str) -> Dict[str, Union[float, str]]:
    """
    Compute Race-Free 2021 NKF/ASN CKD-EPI Estimated Glomerular Filtration Rate (mL/min/1.73m^2).
    Live Web Tool: https://nirogilanka.com/en/egfr-calculator/
    """
    if creatinine_mg_dl <= 0 or age <= 0:
        raise ValueError("creatinine_mg_dl and age must be positive.")
    is_female = str(sex).strip().lower() in ("f", "female", "woman")
    kappa = 0.7 if is_female else 0.9
    alpha = -0.241 if is_female else -0.302
    sex_mult = 1.012 if is_female else 1.0
    ratio = creatinine_mg_dl / kappa
    egfr = 142.0 * (min(ratio, 1.0) ** alpha) * (max(ratio, 1.0) ** -1.200) * (0.9938 ** age) * sex_mult
    egfr_val = round(egfr, 1)

    if egfr_val >= 90:
        stage = "G1 — Normal or High (>=90)"
    elif egfr_val >= 60:
        stage = "G2 — Mildly Decreased (60–89)"
    elif egfr_val >= 45:
        stage = "G3a — Mild-to-Moderately Decreased (45–59)"
    elif egfr_val >= 30:
        stage = "G3b — Moderately-to-Severely Decreased (30–44)"
    elif egfr_val >= 15:
        stage = "G4 — Severely Decreased (15–29)"
    else:
        stage = "G5 — Kidney Failure (<15)"

    return {
        "egfr_ml_min_173m2": egfr_val,
        "kdigo_stage": stage,
        "reference_url": "https://nirogilanka.com/en/egfr-calculator/",
    }


def sampson_ldl(total_chol_mg_dl: float, hdl_mg_dl: float, triglycerides_mg_dl: float) -> Dict[str, Union[float, str]]:
    """
    Compute LDL-Cholesterol via the 2020 NIH Sampson Equation (accurate up to TG 800 mg/dL)
    alongside the classic Friedewald estimate.
    Live Web Tool: https://nirogilanka.com/en/ldl-cholesterol-calculator/
    """
    non_hdl = total_chol_mg_dl - hdl_mg_dl
    sampson = (
        (total_chol_mg_dl / 0.948)
        - (hdl_mg_dl / 0.971)
        - (
            (triglycerides_mg_dl / 8.56)
            + ((triglycerides_mg_dl * non_hdl) / 2140.0)
            - ((triglycerides_mg_dl ** 2) / 16100.0)
        )
        - 9.44
    )
    friedewald = total_chol_mg_dl - hdl_mg_dl - (triglycerides_mg_dl / 5.0)
    return {
        "sampson_ldl_mg_dl": round(sampson, 1),
        "friedewald_ldl_mg_dl": round(friedewald, 1),
        "non_hdl_mg_dl": round(non_hdl, 1),
        "reference_url": "https://nirogilanka.com/en/ldl-cholesterol-calculator/",
    }


def homa_ir(fasting_glucose_mg_dl: float, fasting_insulin_uiu_ml: float) -> Dict[str, Union[float, str]]:
    """
    Compute Homeostatic Model Assessment for Insulin Resistance (HOMA-IR).
    Live Web Tool: https://nirogilanka.com/en/insulin-resistance-calculator/
    """
    score = round((fasting_glucose_mg_dl * fasting_insulin_uiu_ml) / 405.0, 2)
    status = (
        "Optimal Insulin Sensitivity (<1.0)"
        if score < 1.0
        else "Normal Range (1.0–1.9)"
        if score < 2.0
        else "Early Insulin Resistance (2.0–2.9)"
        if score < 3.0
        else "Significant Insulin Resistance (>=3.0)"
    )
    return {
        "homa_ir": score,
        "interpretation": status,
        "reference_url": "https://nirogilanka.com/en/insulin-resistance-calculator/",
    }


def corrected_calcium(measured_ca_mg_dl: float, albumin_g_dl: float, normal_albumin: float = 4.0) -> Dict[str, Union[float, str]]:
    """
    Compute Albumin-Corrected Serum Calcium (Payne's equation).
    Live Web Tool: https://nirogilanka.com/en/corrected-calcium-calculator/
    """
    corr = round(measured_ca_mg_dl + 0.8 * (normal_albumin - albumin_g_dl), 2)
    return {
        "corrected_calcium_mg_dl": corr,
        "reference_interval": "8.5–10.2 mg/dL",
        "reference_url": "https://nirogilanka.com/en/corrected-calcium-calculator/",
    }


def ganzoni_iron_deficit(weight_kg: float, actual_hb_g_dl: float, target_hb_g_dl: float = 15.0, iron_stores_mg: float = 500.0) -> Dict[str, Union[float, str]]:
    """
    Compute Total Cumulative Body Iron Deficit (mg) using the Ganzoni Equation.
    Live Web Tool: https://nirogilanka.com/en/iron-deficit-calculator/
    """
    deficit = round(weight_kg * (target_hb_g_dl - actual_hb_g_dl) * 2.4 + iron_stores_mg, 0)
    return {
        "total_iron_deficit_mg": max(0.0, deficit),
        "reference_url": "https://nirogilanka.com/en/iron-deficit-calculator/",
    }
