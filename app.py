import streamlit as st
from pathlib import Path

# =========================
# KONFIGURACJA STRONY
# =========================

st.set_page_config(
    page_title="GastroMatch",
    page_icon="🥗",
    layout="centered"
)

# =========================
# STYLE
# =========================


st.markdown("""
<style>
    /* =========================
       GŁÓWNY MOTYW
    ========================= */

    .stApp {
        background: #FAFAF7;
        color: #26352B;
    }

    /* =========================
       TEKST GLOBALNY
    ========================= */

    [data-testid="stMarkdownContainer"] {
        color: #26352B !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #26352B !important;
        font-size: 16px;
        line-height: 1.6;
    }

    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4 {
        color: #1F3D2B !important;
        font-weight: 850 !important;
    }

    /* =========================
       ZAKŁADKI
    ========================= */

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.6rem;
    }

    .stTabs [data-baseweb="tab"] {
        color: #4F5D55 !important;
        font-weight: 750 !important;
        border-radius: 12px 12px 0 0;
        padding: 0.6rem 0.9rem;
    }

    .stTabs [data-baseweb="tab"] p {
        color: #4F5D55 !important;
        font-weight: 750 !important;
        font-size: 15px !important;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #EAF7EA !important;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] p {
        color: #1F3D2B !important;
        font-weight: 850 !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #4CAF50 !important;
    }

    /* =========================
       HERO
    ========================= */

    .hero {
        padding: 2.2rem;
        border-radius: 28px;
        background: linear-gradient(135deg, #EAF7EA 0%, #FFFFFF 100%);
        box-shadow: 0 10px 32px rgba(0,0,0,0.07);
        margin-bottom: 1.5rem;
        border: 1px solid #E4EFE4;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 900;
        color: #1F3D2B !important;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 22px;
        color: #4F5D55 !important;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .hero-text {
        font-size: 17px;
        color: #4F5D55 !important;
        line-height: 1.6;
    }

    /* =========================
       KARTY STARTOWE
    ========================= */

    .feature-card {
        padding: 1.2rem;
        border-radius: 22px;
        background-color: #FFFFFF;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        border: 1px solid #EEF1ED;
        min-height: 145px;
    }

    .feature-card h4 {
        color: #1F3D2B !important;
        font-weight: 850 !important;
        margin-bottom: 0.5rem;
    }

    .feature-card p {
        color: #4F5D55 !important;
        font-size: 15px;
        line-height: 1.5;
    }

    /* =========================
       PYTANIA
    ========================= */

    .question-card {
        padding: 2rem;
        border-radius: 26px;
        background: #FFFFFF;
        box-shadow: 0 8px 26px rgba(0,0,0,0.06);
        border: 1px solid #EEF1ED;
        margin-bottom: 1rem;
    }

    .question-label {
        font-size: 13px;
        color: #78907C !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 850;
        margin-bottom: 0.5rem;
    }

    .question-title {
        font-size: 30px;
        font-weight: 900;
        color: #1F3D2B !important;
        margin-bottom: 0.6rem;
    }

    .question-subtitle {
        font-size: 16px;
        color: #5D6B62 !important;
        margin-bottom: 0.8rem;
    }

    /* =========================
       WYNIK
    ========================= */

    .result-card {
        padding: 2rem;
        border-radius: 28px;
        background-color: #FFFFFF;
        box-shadow: 0 12px 34px rgba(0,0,0,0.08);
        border-left: 9px solid #4CAF50;
        margin-bottom: 1.4rem;
    }

    .small-label {
        font-size: 13px;
        color: #7A857D !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 850;
    }

    .big-result {
        font-size: 34px;
        font-weight: 900;
        color: #1F3D2B !important;
        margin-top: 0.25rem;
        margin-bottom: 0.6rem;
    }

    .result-description {
        font-size: 17px;
        color: #4F5D55 !important;
        line-height: 1.6;
    }

    /* =========================
       METRYKI: PROCENTY I 7/7
    ========================= */

    [data-testid="stMetric"] {
        background-color: transparent !important;
        padding: 0.4rem 0 !important;
    }

    [data-testid="stMetricLabel"] {
        color: #4F5D55 !important;
        font-weight: 850 !important;
        font-size: 15px !important;
    }

    [data-testid="stMetricLabel"] p {
        color: #4F5D55 !important;
        font-weight: 850 !important;
        font-size: 15px !important;
    }

    [data-testid="stMetricValue"] {
        color: #1F3D2B !important;
        font-size: 42px !important;
        font-weight: 900 !important;
        line-height: 1.1 !important;
    }

    [data-testid="stMetricValue"] div {
        color: #1F3D2B !important;
        font-size: 42px !important;
        font-weight: 900 !important;
        line-height: 1.1 !important;
    }

    /* =========================
       NOTATKA POD METRYKAMI
    ========================= */

    .metric-note {
        color: #4F5D55 !important;
        font-size: 14px;
        line-height: 1.5;
        background-color: #F1FAF1;
        border-left: 4px solid #4CAF50;
        padding: 0.8rem 1rem;
        border-radius: 12px;
        margin-top: 0.8rem;
        margin-bottom: 1.2rem;
    }

    .metric-note b {
        color: #1F3D2B !important;
        font-weight: 850 !important;
    }

    /* =========================
       SEKCJE W WYNIKU
    ========================= */

    .section-title {
        color: #1F3D2B !important;
        font-size: 24px;
        font-weight: 900;
        margin-top: 1.8rem;
        margin-bottom: 0.8rem;
    }

    .reason {
        padding: 0.5rem 0;
        font-size: 17px;
        color: #26352B !important;
    }

    /* =========================
       ALTERNATYWY
    ========================= */

    .alternative-card {
        padding: 1.2rem;
        border-radius: 20px;
        background-color: #FFFFFF;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        border: 1px solid #EEF1ED;
        min-height: 145px;
    }

    .alternative-card h4 {
        color: #1F3D2B !important;
        font-weight: 850 !important;
    }

    .alternative-card p {
        color: #4F5D55 !important;
        line-height: 1.5 !important;
    }

    .alternative-card b {
        color: #1F3D2B !important;
        font-weight: 850 !important;
    }

    /* =========================
       PRZYCISKI
    ========================= */

    div.stButton > button {
        width: 100%;
        border-radius: 16px;
        min-height: 3.3rem;
        font-weight: 800;
        border: 1px solid #DDE8DD;
        background-color: #FFFFFF;
        color: #1F3D2B;
        transition: all 0.15s ease-in-out;
    }
    div.stButton > button p {
        color: #1F3D2B !important;
        font-weight: 800 !important;
}
    div.stButton > button:hover {
        border-color: #4CAF50;
        color: #1F3D2B;
        background-color: #F1FAF1;
        transform: translateY(-1px);
    }

    /* =========================
       STOPKA
    ========================= */

    .footer-note {
        font-size: 13px;
        color: #7A857D !important;
        margin-top: 1rem;
    }
    

    /* =========================
       PASEK POSTĘPU
    ========================= */

    .stProgress > div > div {
        background-color: #E6F1E6 !important;
        border-radius: 999px !important;
    }

    .stProgress > div > div > div {
        background-color: #4CAF50 !important;
        border-radius: 999px !important;
    }
        /* =========================
       KAFELKI PODSUMOWANIA
    ========================= */

    .choice-summary-card {
        background: #FFFFFF;
        border: 1px solid #E4EFE4;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.045);
        padding: 1rem 1.1rem;
        margin-bottom: 0.9rem;
        min-height: 105px;
    }

    .choice-summary-label {
        color: #78907C !important;
        font-size: 12px;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.45rem;
    }

    .choice-summary-value {
        color: #1F3D2B !important;
        font-size: 16px;
        font-weight: 800;
        line-height: 1.45;
    }
        /* =========================
       KARTA ZAŁĄCZNIKA XLSX
    ========================= */

    .xlsx-card {
        background: linear-gradient(135deg, #F1FAF1 0%, #FFFFFF 100%);
        border: 1px solid #DDE8DD;
        border-radius: 22px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.055);
        padding: 1.3rem 1.4rem;
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }

    .xlsx-card-label {
        color: #78907C !important;
        font-size: 12px;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.35rem;
    }

    .xlsx-card-title {
        color: #1F3D2B !important;
        font-size: 22px;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }

    .xlsx-card-text {
        color: #4F5D55 !important;
        font-size: 16px;
        line-height: 1.55;
        margin-bottom: 0.7rem;
    }

    .xlsx-card-list {
        color: #26352B !important;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 0.7rem;
    }

    .xlsx-card-list span {
        display: block;
        margin-bottom: 0.25rem;
    }

    div.stDownloadButton > button {
        width: auto !important;
        min-height: 3.1rem;
        padding: 0.7rem 1.2rem;
        border-radius: 16px !important;
        border: 1px solid #DDE8DD !important;
        background-color: #FFFFFF !important;
        color: #1F3D2B !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        transition: all 0.15s ease-in-out;
    }
    div.stDownloadButton > button p {
        color: #1F3D2B !important;
        font-weight: 800 !important;
}

    div.stDownloadButton > button:hover {
        background-color: #F1FAF1 !important;
        border-color: #4CAF50 !important;
        color: #1F3D2B !important;
        transform: translateY(-1px);
    }

    div.stDownloadButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.18) !important;
    }
    .xlsx-card-list-title {
        color: #1F3D2B !important;
        font-size: 15px;
        font-weight: 850;
        margin-top: 0.9rem;
        margin-bottom: 0.35rem;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# DANE APLIKACJI
# =========================

TOTAL_STEPS = 7

DIET_DESCRIPTIONS = {
    "Wybór Menu": "Dla osób, które chcą samodzielnie wybierać dania i mieć większą różnorodność posiłków.",
    "Klasyk": "Dla osób bez specjalnych ograniczeń żywieniowych, które chcą prostego i codziennego rozwiązania.",
    "Wege": "Dla osób, które nie jedzą mięsa i chcą dopasować ofertę do preferencji roślinnych.",
    "Sportowa": "Dla osób aktywnych fizycznie, które trenują i potrzebują bardziej sportowego podejścia do odżywiania.",
    "Keto / Low Carb": "Dla osób, które chcą ograniczać węglowodany i szukają bardziej specjalistycznego wariantu.",
    "Niski IG": "Dla osób, które zwracają uwagę na stabilny poziom energii i niski indeks glikemiczny.",
    "Bez glutenu i nabiału": "Dla osób, które chcą unikać glutenu i nabiału w codziennych posiłkach."
}

PACKAGE_DESCRIPTIONS = {
    "Paczka Standardowa": "Pełniejszy wariant na cały dzień — dobry, gdy chcesz otrzymywać większą liczbę posiłków.",
    "Paczka Optymalna": "Dobry kompromis między pełnym pakietem a prostszym planem dnia.",
    "Paczka Podstawowa": "Prostsza opcja dla osób, które chcą wygodnego rozwiązania bez nadmiaru konfiguracji.",
    "Paczka na Etacie": "Wariant dla osób pracujących poza domem, które potrzebują wygodnych posiłków w ciągu dnia.",
    "Paczka Home Office": "Wariant dla osób pracujących z domu, które chcą jeść regularnie bez gotowania.",
    "Paczka Obiadowa": "Opcja dla osób, które potrzebują głównie obiadu lub mniejszego zakresu posiłków.",
    "Paczka Rodzinna": "Wariant dla osób, które szukają rozwiązania dla więcej niż jednej osoby."
}

QUESTIONS = [
    {
        "key": "cel",
        "title": "Jaki jest Twój główny cel?",
        "subtitle": "To pytanie pomaga ustalić, czego użytkownik najbardziej oczekuje od cateringu.",
        "options": [
            ("Chcę schudnąć", "🎯"),
            ("Chcę zdrowo i regularnie jeść", "🥗"),
            ("Chcę budować masę / dużo trenuję", "🏋️"),
            ("Chcę oszczędzić czas", "⏱️"),
            ("Szukam rozwiązania dla rodziny", "👨‍👩‍👧"),
            ("Nie wiem", "🤔")
        ]
    },
    {
        "key": "tryb",
        "title": "Jak wygląda Twój typowy dzień?",
        "subtitle": "Tryb dnia pomaga dobrać wariant paczki, a nie tylko typ diety.",
        "options": [
            ("Pracuję w biurze / poza domem", "🏢"),
            ("Pracuję z domu", "🏠"),
            ("Studiuję", "🎓"),
            ("Dużo trenuję", "🏃"),
            ("Mam nieregularny plan dnia", "🔄"),
            ("Szukam rozwiązania dla rodziny", "👨‍👩‍👧")
        ]
    },
    {
        "key": "posilki",
        "title": "Ile posiłków dziennie chcesz otrzymywać?",
        "subtitle": "Liczba posiłków pozwala zawęzić wybór do konkretnego wariantu.",
        "options": [
            ("2 posiłki", "🍽️"),
            ("3 posiłki", "🍱"),
            ("4 posiłki", "🥙"),
            ("5 posiłków", "🥗"),
            ("Nie wiem", "🤔")
        ]
    },
    {
        "key": "wybor_menu",
        "title": "Czy chcesz samodzielnie wybierać dania?",
        "subtitle": "To ważne, bo część klientów chce elastyczności, a część woli gotową propozycję.",
        "options": [
            ("Tak, chcę mieć duży wybór", "🧩"),
            ("Nie, wolę gotową propozycję", "✅"),
            ("Czasami", "⚖️")
        ]
    },
    {
        "key": "priorytet",
        "title": "Co jest dla Ciebie najważniejsze?",
        "subtitle": "Priorytet użytkownika wpływa na końcową rekomendację i uzasadnienie.",
        "options": [
            ("Cena", "💸"),
            ("Wygoda", "🛋️"),
            ("Różnorodność", "🍲"),
            ("Efekt sylwetkowy", "📈"),
            ("Zdrowie", "💚"),
            ("Oszczędność czasu", "⏱️")
        ]
    },
    {
        "key": "kalorie",
        "title": "Czy znasz swoją kaloryczność?",
        "subtitle": "Jeśli użytkownik jej nie zna, aplikacja może zasugerować kolejny krok: kalkulator kalorii.",
        "options": [
            ("Tak, wiem czego szukam", "✅"),
            ("Nie, potrzebuję pomocy", "🧮"),
            ("Nie mam pewności", "🤔")
        ]
    }
]


# =========================
# STAN APLIKACJI
# =========================

if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


def reset_quiz():
    st.session_state.step = 0
    st.session_state.answers = {}


def go_back():
    if st.session_state.step > 0:
        st.session_state.step -= 1


def choose_answer(key, value):
    st.session_state.answers[key] = value
    st.session_state.step += 1


# =========================
# LOGIKA REKOMENDACJI
# =========================

def calculate_recommendation(answers):
    diet_scores = {
        "Wybór Menu": 0,
        "Klasyk": 0,
        "Wege": 0,
        "Sportowa": 0,
        "Keto / Low Carb": 0,
        "Niski IG": 0,
        "Bez glutenu i nabiału": 0
    }

    package_scores = {
        "Paczka Standardowa": 0,
        "Paczka Optymalna": 0,
        "Paczka Podstawowa": 0,
        "Paczka na Etacie": 0,
        "Paczka Home Office": 0,
        "Paczka Obiadowa": 0,
        "Paczka Rodzinna": 0
    }

    reasons = []
    next_steps = []

    cel = answers.get("cel")
    tryb = answers.get("tryb")
    posilki = answers.get("posilki")
    wybor_menu = answers.get("wybor_menu")
    preferencje = answers.get("preferencje", [])
    priorytet = answers.get("priorytet")
    kalorie = answers.get("kalorie")

    # Cel
    if cel == "Chcę schudnąć":
        diet_scores["Wybór Menu"] += 2
        diet_scores["Niski IG"] += 2
        package_scores["Paczka Optymalna"] += 2
        reasons.append("chcesz lepiej kontrolować sposób odżywiania")

    elif cel == "Chcę zdrowo i regularnie jeść":
        diet_scores["Klasyk"] += 3
        diet_scores["Wybór Menu"] += 2
        package_scores["Paczka Standardowa"] += 2
        package_scores["Paczka Optymalna"] += 1
        reasons.append("zależy Ci na regularnych posiłkach i prostym wyborze")

    elif cel == "Chcę budować masę / dużo trenuję":
        diet_scores["Sportowa"] += 5
        package_scores["Paczka Standardowa"] += 2
        reasons.append("masz wyższą aktywność fizyczną lub cel sportowy")

    elif cel == "Chcę oszczędzić czas":
        diet_scores["Klasyk"] += 2
        package_scores["Paczka na Etacie"] += 2
        package_scores["Paczka Home Office"] += 2
        package_scores["Paczka Podstawowa"] += 1
        reasons.append("najważniejsza jest dla Ciebie wygoda i oszczędność czasu")

    elif cel == "Szukam rozwiązania dla rodziny":
        package_scores["Paczka Rodzinna"] += 5
        diet_scores["Klasyk"] += 2
        reasons.append("szukasz rozwiązania dla więcej niż jednej osoby")

    else:
        diet_scores["Wybór Menu"] += 2
        diet_scores["Klasyk"] += 1
        package_scores["Paczka Optymalna"] += 1
        reasons.append("nie masz jeszcze sprecyzowanego celu, więc warto zacząć od elastycznej opcji")

    # Tryb dnia
    if tryb == "Pracuję w biurze / poza domem":
        package_scores["Paczka na Etacie"] += 5
        reasons.append("pracujesz poza domem i potrzebujesz wygodnych posiłków na dzień pracy")

    elif tryb == "Pracuję z domu":
        package_scores["Paczka Home Office"] += 5
        reasons.append("pracujesz z domu i chcesz jeść regularnie bez gotowania")

    elif tryb == "Studiuję":
        package_scores["Paczka Podstawowa"] += 3
        package_scores["Paczka Obiadowa"] += 2
        reasons.append("szukasz prostego wariantu pasującego do zmiennego planu dnia")

    elif tryb == "Dużo trenuję":
        diet_scores["Sportowa"] += 4
        package_scores["Paczka Standardowa"] += 2
        reasons.append("Twój tryb dnia jest związany z aktywnością fizyczną")

    elif tryb == "Mam nieregularny plan dnia":
        diet_scores["Wybór Menu"] += 3
        package_scores["Paczka Optymalna"] += 2
        reasons.append("masz nieregularny plan dnia, więc przyda Ci się elastyczność")

    elif tryb == "Szukam rozwiązania dla rodziny":
        package_scores["Paczka Rodzinna"] += 4
        reasons.append("potrzebujesz rozwiązania, które można dopasować do więcej niż jednej osoby")

    # Posiłki
    if posilki == "2 posiłki":
        package_scores["Paczka Obiadowa"] += 4
        package_scores["Paczka Podstawowa"] += 1
        reasons.append("preferujesz mniejszą liczbę posiłków")

    elif posilki == "3 posiłki":
        package_scores["Paczka Podstawowa"] += 2
        package_scores["Paczka na Etacie"] += 2
        package_scores["Paczka Home Office"] += 2
        reasons.append("3 posiłki dobrze pasują do pracy, nauki albo home office")

    elif posilki == "4 posiłki":
        package_scores["Paczka Optymalna"] += 4
        reasons.append("4 posiłki to kompromis między pełnym planem a prostszą paczką")

    elif posilki == "5 posiłków":
        package_scores["Paczka Standardowa"] += 4
        reasons.append("chcesz bardziej pełny plan żywieniowy na cały dzień")

    else:
        package_scores["Paczka Optymalna"] += 2
        diet_scores["Wybór Menu"] += 1
        reasons.append("nie wiesz jeszcze, ile posiłków wybrać, więc warto zacząć od uniwersalnej opcji")

    # Wybór menu
    if wybor_menu == "Tak, chcę mieć duży wybór":
        diet_scores["Wybór Menu"] += 6
        reasons.append("zależy Ci na samodzielnym wyborze dań")

    elif wybor_menu == "Nie, wolę gotową propozycję":
        diet_scores["Klasyk"] += 3
        package_scores["Paczka Podstawowa"] += 1
        reasons.append("wolisz gotową propozycję bez codziennego podejmowania decyzji")

    elif wybor_menu == "Czasami":
        diet_scores["Wybór Menu"] += 2
        diet_scores["Klasyk"] += 1
        reasons.append("chcesz mieć trochę elastyczności, ale bez nadmiaru wyboru")

    # Preferencje
    if "Brak ograniczeń" in preferencje and len(preferencje) == 1:
        diet_scores["Klasyk"] += 3
        reasons.append("nie masz specjalnych ograniczeń żywieniowych")

    if "Wege" in preferencje:
        diet_scores["Wege"] += 6
        reasons.append("wskazałaś preferencję: dieta wege")

    if "Bez glutenu / bez nabiału" in preferencje:
        diet_scores["Bez glutenu i nabiału"] += 6
        reasons.append("wskazałaś ograniczenie: bez glutenu / bez nabiału")

    if "Keto / low carb" in preferencje:
        diet_scores["Keto / Low Carb"] += 6
        reasons.append("interesuje Cię dieta z ograniczeniem węglowodanów")

    if "Niski IG" in preferencje:
        diet_scores["Niski IG"] += 6
        reasons.append("zwracasz uwagę na niski indeks glikemiczny")

    if "Dieta sportowa" in preferencje:
        diet_scores["Sportowa"] += 5
        reasons.append("wskazałaś preferencję sportową")

    # Priorytet
    if priorytet == "Cena":
        package_scores["Paczka Podstawowa"] += 4
        package_scores["Paczka Obiadowa"] += 1
        reasons.append("ważna jest dla Ciebie cena")

    elif priorytet == "Wygoda":
        package_scores["Paczka na Etacie"] += 2
        package_scores["Paczka Home Office"] += 2
        diet_scores["Klasyk"] += 1
        reasons.append("najważniejsza jest dla Ciebie wygoda")

    elif priorytet == "Różnorodność":
        diet_scores["Wybór Menu"] += 4
        reasons.append("ważna jest dla Ciebie różnorodność posiłków")

    elif priorytet == "Efekt sylwetkowy":
        diet_scores["Sportowa"] += 2
        diet_scores["Niski IG"] += 2
        package_scores["Paczka Standardowa"] += 1
        reasons.append("zależy Ci na efekcie sylwetkowym")

    elif priorytet == "Zdrowie":
        diet_scores["Niski IG"] += 2
        diet_scores["Klasyk"] += 1
        reasons.append("ważny jest dla Ciebie aspekt zdrowotny")

    elif priorytet == "Oszczędność czasu":
        package_scores["Paczka na Etacie"] += 2
        package_scores["Paczka Home Office"] += 2
        package_scores["Paczka Podstawowa"] += 1
        reasons.append("chcesz ograniczyć czas poświęcany na planowanie jedzenia")

    # Kalorie
    if kalorie == "Nie, potrzebuję pomocy":
        next_steps.append("sprawdź kalkulator kaloryczności przed finalnym zamówieniem")
        reasons.append("nie znasz jeszcze kaloryczności, więc warto dodać kalkulator jako kolejny etap")

    elif kalorie == "Nie mam pewności":
        next_steps.append("porównaj rekomendację z kalkulatorem kalorii")
        reasons.append("nie masz pewności co do kaloryczności, więc przyda się dodatkowa walidacja")

    else:
        next_steps.append("przejdź do konfiguracji zamówienia z wybraną kalorycznością")

    sorted_diets = sorted(diet_scores.items(), key=lambda item: item[1], reverse=True)
    sorted_packages = sorted(package_scores.items(), key=lambda item: item[1], reverse=True)

    diet_total = sum(diet_scores.values())
    package_total = sum(package_scores.values())

    diet_conf = sorted_diets[0][1] / diet_total if diet_total else 0
    package_conf = sorted_packages[0][1] / package_total if package_total else 0

    match_score = int(65 + ((diet_conf + package_conf) / 2) * 30)
    match_score = max(72, min(match_score, 94))

    return {
        "top_diet": sorted_diets[0][0],
        "top_package": sorted_packages[0][0],
        "alt_diets": sorted_diets[1:3],
        "alt_packages": sorted_packages[1:3],
        "reasons": reasons[:6],
        "next_steps": next_steps,
        "match_score": match_score,
        "diet_scores": diet_scores,
        "package_scores": package_scores
    }


# =========================
# WIDOKI
# =========================

def render_progress():
    if st.session_state.step > 0:
        progress = min(st.session_state.step / TOTAL_STEPS, 1.0)
        st.progress(progress)
        st.caption(f"Krok {min(st.session_state.step, TOTAL_STEPS)} z {TOTAL_STEPS}")


def render_start():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">🥗 GastroMatch</div>
        <div class="hero-subtitle">Dobierz dietę pudełkową w mniej niż 2 minuty.</div>
        <div class="hero-text">
            Nie wiesz, którą opcję wybrać? Odpowiedz na kilka pytań,
            a GastroMatch zaproponuje dietę i wariant paczki dopasowane do Twojego stylu życia,
            celu oraz preferencji.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Szybko</h4>
            <p>Krótki proces zamiast przeglądania wielu opcji.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Trafnie</h4>
            <p>Rekomendacja oparta na celu, trybie dnia i preferencjach.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>💡 Zrozumiale</h4>
            <p>Wynik pokazuje, dlaczego dana opcja pasuje.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("To jest prototyp aplikacji do wspierania decyzji zakupowych. Wynik nie jest poradą dietytyczną")

    if st.button("Rozpocznij quiz 🚀"):
        st.session_state.step = 1
        st.rerun()


def render_choice_question(question_index):
    question = QUESTIONS[question_index]

    st.markdown(f"""
    <div class="question-card">
        <div class="question-label">Pytanie {st.session_state.step} z {TOTAL_STEPS}</div>
        <div class="question-title">{question["title"]}</div>
        <div class="question-subtitle">{question["subtitle"]}</div>
    </div>
    """, unsafe_allow_html=True)

    options = question["options"]
    cols = st.columns(2)

    for index, (label, icon) in enumerate(options):
        with cols[index % 2]:
            if st.button(f"{icon} {label}", key=f"{question['key']}_{index}"):
                choose_answer(question["key"], label)
                st.rerun()

    st.divider()

    if st.button("← Wstecz"):
        go_back()
        st.rerun()


def render_preferences_question():
    st.markdown("""
    <div class="question-card">
        <div class="question-label">Pytanie 5 z 7</div>
        <div class="question-title">Czy masz preferencje żywieniowe?</div>
        <div class="question-subtitle">
            Najpierw wybierz, czy masz ograniczenia lub preferencje. Jeśli tak,
            wskaż jedną lub kilka opcji.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "has_preferences" not in st.session_state.answers:
        st.session_state.answers["has_preferences"] = None

    if "preferencje" not in st.session_state.answers:
        st.session_state.answers["preferencje"] = []

    st.markdown(
        '<div class="preference-grid-title">Wybierz jedną opcję:</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Nie mam ograniczeń", key="btn_no_preferences"):
            st.session_state.answers["has_preferences"] = "Nie"
            st.session_state.answers["preferencje"] = ["Brak ograniczeń"]
            st.rerun()

    with col2:
        if st.button("🥗 Mam preferencje", key="btn_has_preferences"):
            st.session_state.answers["has_preferences"] = "Tak"

            if st.session_state.answers.get("preferencje") == ["Brak ograniczeń"]:
                st.session_state.answers["preferencje"] = []

            st.rerun()

    if st.session_state.answers["has_preferences"] == "Tak":
        st.markdown(
            '<div class="preference-grid-title">Wskaż preferencje:</div>',
            unsafe_allow_html=True
        )

        options = [
            ("Wege", "🥦"),
            ("Bez glutenu / bez nabiału", "🌾"),
            ("Keto / low carb", "🥑"),
            ("Niski IG", "📉"),
            ("Dieta sportowa", "🏋️")
        ]

        selected = st.session_state.answers.get("preferencje", [])
        cols = st.columns(2)

        for index, (option, icon) in enumerate(options):
            is_selected = option in selected
            prefix = "✅" if is_selected else "○"

            with cols[index % 2]:
                if st.button(
                    f"{prefix} {icon} {option}",
                    key=f"btn_preference_option_{index}"
                ):
                    current = st.session_state.answers.get("preferencje", [])

                    if option in current:
                        current.remove(option)
                    else:
                        current.append(option)

                    st.session_state.answers["preferencje"] = current
                    st.rerun()

    selected_text = ", ".join(st.session_state.answers.get("preferencje", []))

    if not selected_text:
        selected_text = "Nie wybrano jeszcze preferencji"

    st.markdown(
        f"""
        <div class="selected-preferences">
            <span>Wybrane:</span> {selected_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Wstecz", key="btn_preferences_back"):
            go_back()
            st.rerun()

    with col2:
        if st.button("Dalej", key="btn_preferences_next"):
            if st.session_state.answers["has_preferences"] is None:
                st.warning("Wybierz, czy masz preferencje żywieniowe.")
                return

            if (
                st.session_state.answers["has_preferences"] == "Tak"
                and not st.session_state.answers.get("preferencje")
            ):
                st.warning(
                    "Wskaż przynajmniej jedną preferencję albo wybierz „Nie mam ograniczeń”."
                )
                return

            st.session_state.step += 1
            st.rerun()


def render_result():
    result = calculate_recommendation(st.session_state.answers)

    top_diet = result["top_diet"]
    top_package = result["top_package"]

    st.markdown(f"""
    <div class="result-card">
        <div class="small-label">Twoja rekomendacja</div>
        <div class="big-result">🥗 {top_diet} + {top_package}</div>
        <div class="result-description">
            {DIET_DESCRIPTIONS[top_diet]}<br><br>
            {PACKAGE_DESCRIPTIONS[top_package]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Siła rekomendacji", f"{result['match_score']}%")

    with col2:
        st.metric("Ukończone kroki", "7/7")

    st.markdown("""
    <div class="metric-note">
        <b>Jak czytać siłę rekomendacji?</b><br>
        Procent pokazuje siłę rekomendacji w ramach zastosowanej matrycy punktowej.
        Aplikacja przyznaje punkty różnym dietom i wariantom paczek na podstawie Twoich odpowiedzi.
        Im bardziej jedna opcja wyróżnia się na tle pozostałych, tym wyższa siła rekomendacji.
        <br><br>
        Wynik nie oznacza skuteczności diety ani porady dietetycznej.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Dlaczego ta opcja?</div>',
        unsafe_allow_html=True
    )

    for reason in result["reasons"]:
        st.markdown(
            f"<div class='reason'>✅ {reason}</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">Alternatywne propozycje</div>',
        unsafe_allow_html=True
    )

    alt_diet_1 = result["alt_diets"][0][0]
    alt_diet_2 = result["alt_diets"][1][0]
    alt_pack_1 = result["alt_packages"][0][0]
    alt_pack_2 = result["alt_packages"][1][0]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="alternative-card">
            <h4>Opcja 2</h4>
            <p><b>{alt_diet_1} + {alt_pack_1}</b></p>
            <p>{DIET_DESCRIPTIONS[alt_diet_1]}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="alternative-card">
            <h4>Opcja 3</h4>
            <p><b>{alt_diet_2} + {alt_pack_2}</b></p>
            <p>{PACKAGE_DESCRIPTIONS[alt_pack_2]}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Następny krok</div>',
        unsafe_allow_html=True
    )

    for step in result["next_steps"]:
        st.write(f"➡️ {step}")

    st.info(
        "W pełnej wersji aplikacji ten ekran mógłby prowadzić użytkownika do kalkulatora kalorii, "
        "porównywarki pakietów lub bezpośrednio do konfiguracji zamówienia."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Zacznij od nowa"):
            reset_quiz()
            st.rerun()

    with col2:
        if st.button("Wróć do poprzedniego pytania"):
            go_back()
            st.rerun()

    st.markdown(
        '<div class="section-title">Twoja ścieżka decyzyjna</div>',
        unsafe_allow_html=True
    )

    labels = {
        "cel": ("Cel", "🎯"),
        "tryb": ("Tryb dnia", "🕒"),
        "posilki": ("Liczba posiłków", "🍽️"),
        "wybor_menu": ("Wybór dań", "🧩"),
        "preferencje": ("Preferencje żywieniowe", "🥗"),
        "priorytet": ("Priorytet", "⭐"),
        "kalorie": ("Kaloryczność", "🧮")
    }

    answers = st.session_state.answers

    rows = list(labels.items())

    for i in range(0, len(rows), 2):
        col1, col2 = st.columns(2)

        for col, item in zip([col1, col2], rows[i:i + 2]):
            key, (label, icon) = item
            value = answers.get(key, "Brak odpowiedzi")

            if isinstance(value, list):
                value = ", ".join(value)

            with col:
                st.markdown(f"""
                <div class="choice-summary-card">
                    <div class="choice-summary-label">{icon} {label}</div>
                    <div class="choice-summary-value">{value}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(
        "<div class='footer-note'>Prototyp przygotowany w ramach projektu  GastroMatch.</div>",
        unsafe_allow_html=True
    )


def render_about_project():
    st.header("📌 O projekcie GastroMatch")

    st.markdown("""
    ### Cel projektu

    GastroMatch to prototyp asystenta decyzyjnego dla oferty Gastro Paczki,
    który wspiera użytkownika w wyborze diety pudełkowej oraz odpowiedniego
    wariantu paczki.

    Projekt odpowiada na problem pierwszego kontaktu z ofertą. Nowy użytkownik
    może czuć się zagubiony, ponieważ musi porównać wiele możliwości: typ diety,
    liczbę posiłków, tryb dnia, preferencje żywieniowe, kaloryczność oraz wariant
    paczki. Duża liczba opcji jest wartością oferty, ale może też wydłużać proces
    decyzyjny.

    Celem GastroMatch jest skrócenie tej ścieżki. Użytkownik odpowiada na kilka
    prostych pytań, a aplikacja przedstawia rekomendację główną, alternatywne
    propozycje oraz sugerowany kolejny krok.
    """)

    st.markdown(
        '<div class="section-title">Logika rekomendacji</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    Prototyp działa na podstawie matrycy punktowej. Każda odpowiedź użytkownika
    zwiększa wynik wybranych typów diet lub wariantów paczek.

    Punkty są naliczane osobno dla dwóch obszarów:

    - typu diety, np. Wybór Menu, Klasyk, Sportowa, Wege,
    - wariantu paczki, np. Home Office, Na Etacie, Standardowa, Obiadowa.

    Po zakończeniu quizu aplikacja wybiera najwyżej punktowaną dietę oraz
    najwyżej punktowany wariant paczki. Dodatkowo prezentuje dwie alternatywy,
    które również uzyskały wysokie dopasowanie do odpowiedzi użytkownika.
    """)

    st.markdown(
        '<div class="section-title">Siła rekomendacji</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    Procent widoczny przy wyniku jest orientacyjną siłą rekomendacji w ramach
    zastosowanego algorytmu punktowego.

    Wartość procentowa nie oznacza skuteczności diety ani porady dietetycznej.
    Pokazuje jedynie, jak wyraźnie najlepsza rekomendacja wyróżniła się na tle
    pozostałych opcji w ramach przyjętej matrycy decyzyjnej.
    """)

    st.markdown(
        '<div class="section-title">Dokumentacja logiki prototypu</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="xlsx-card">
        <div class="xlsx-card-label">Załącznik XLSX</div>
        <div class="xlsx-card-title">Matryca punktowa i symulator rekomendacji</div>
        <div class="xlsx-card-text">
    Szczegółowa logika działania prototypu została przygotowana jako osobny
    plik XLSX. Załącznik pokazuje, które odpowiedzi użytkownika wpływają
    na konkretne typy diet i warianty paczek, a arkusz „Symulator” pozwala
    sprawdzić przykładowe scenariusze wyboru.
</div>
        <div class="xlsx-card-list-title">W załączniku znajdują się:</div>
        <div class="xlsx-card-list">
            <span>✓ interaktywny symulator wyboru odpowiedzi,</span>
            <span>✓ szczegółowa matryca punktowa,</span>
            <span>✓ wyjaśnienie sposobu liczenia siły rekomendacji,</span>
            <span>✓ listy odpowiedzi używane w symulatorze,</span>
            <span>✓ opis założeń i sposobu korzystania z pliku.</span>
</div>
    </div>
    """, unsafe_allow_html=True)

    matrix_path = Path("GastroMatch_matryca_logiki_symulator.xlsx")

    if matrix_path.exists():
        with open(matrix_path, "rb") as file:
            st.download_button(
                label="📥 Pobierz matrycę logiki (XLSX)",
                data=file,
                file_name="GastroMatch_matryca_logiki_symulator.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.info(
            "Plik XLSX z matrycą logiki powinien zostać dołączony do folderu projektu."
        )

    st.markdown(
        '<div class="section-title">Zakres prototypu</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    Obecna wersja aplikacji jest prototypem. Jej zadaniem jest
    pokazanie koncepcji uproszczenia wyboru oferty, a nie pełne odwzorowanie
    wszystkich reguł dietetycznych, cenowych i operacyjnych.

    W kolejnych etapach projekt może zostać rozbudowany o aktualną ofertę,
    rzeczywisty cennik, kalkulator kaloryczności, dane sprzedażowe, testy A/B
    oraz integrację z procesem składania zamówienia.
    """)

    st.info(
        "GastroMatch nie zastępuje konsultacji dietetycznej. "
        "To prototyp narzędzia wspierającego pierwszy wybór oferty."
    )

def render_research_tab():
    st.header("📊 Badanie prototypu")

    st.markdown("""
    ### Czy GastroMatch faktycznie pomaga w wyborze?

    Po przygotowaniu prototypu przeprowadzono badanie pilotażowe na grupie 12 respondentów.
    Celem było sprawdzenie, czy krótki quiz rekomendacyjny może ułatwić nowemu użytkownikowi
    pierwszy wybór diety i wariantu paczki w ofercie Gastro Paczki.

    Respondenci porównywali dwa scenariusze:

    1. **Samodzielny wybór oferty bez GastroMatch**  
    2. **Wybór z wykorzystaniem prototypu GastroMatch**

    Badanie nie miało na celu pełnej walidacji gotowego produktu, lecz sprawdzenie,
    czy sama koncepcja asystenta pierwszego wyboru jest zrozumiała i użyteczna.
    """)

    st.markdown(
        '<div class="section-title">Najważniejsze wyniki</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Respondenci", "12", "badanie pilotażowe")

    with col2:
        st.metric("Łatwiejszy wybór", "83%", "z GastroMatch")

    with col3:
        st.metric("Quiz do 2 minut", "83%", "respondentów")

    with col4:
        st.metric("Zrozumiałość", "100%", "ocena 4 lub 5/5")

    st.markdown("""
    Wyniki wskazują, że GastroMatch najlepiej sprawdza się jako pierwszy filtr decyzyjny:
    pomaga szybciej zawęzić wybór, uporządkować potrzeby użytkownika i zrozumieć,
    dlaczego dana opcja została wskazana.
    """)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Porównanie przed i po użyciu GastroMatch</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Łatwość wyboru",
            "4,50 / 5",
            "+1,75 względem wyboru bez aplikacji"
        )
        st.caption("Bez GastroMatch: 2,75 / 5")

    with col2:
        st.metric(
            "Pewność decyzji",
            "3,58 / 5",
            "+0,58 względem wyboru bez aplikacji"
        )
        st.caption("Bez GastroMatch: 3,00 / 5")

    with col3:
        st.metric(
            "Zrozumienie rekomendacji",
            "4,75 / 5",
            "+1,75 względem wyboru bez aplikacji"
        )
        st.caption("Bez GastroMatch: 3,00 / 5")

    st.markdown("""
    Największa poprawa była widoczna w dwóch obszarach: **łatwości wyboru**
    oraz **zrozumieniu rekomendacji**. Pewność decyzji również wzrosła, ale słabiej,
    co wskazuje konkretny kierunek dalszego rozwoju prototypu.
    """)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Czas wyboru</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### Bez GastroMatch

        **67% respondentów** potrzebowało ponad 10 minut  
        albo nie udało im się jednoznacznie wybrać oferty.
        """)

    with col2:
        st.markdown("""
        #### Z GastroMatch

        **83% respondentów** przeszło quiz i otrzymało rekomendację  
        w czasie do 2 minut.
        """)

    st.success(
        "Wniosek: GastroMatch skraca ścieżkę decyzyjną i pomaga szybciej przejść "
        "od ogólnego zainteresowania ofertą do konkretnej rekomendacji."
    )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Co najbardziej pomogło użytkownikom?</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    W odpowiedziach otwartych respondenci najczęściej wskazywali:

    - krótką i prostą ścieżkę decyzyjną,
    - intuicyjny przebieg quizu,
    - pytania, które pomagały uporządkować potrzeby,
    - sekcję **„Dlaczego ta opcja?”**,
    - szybkie otrzymanie konkretnej rekomendacji bez samodzielnego porównywania wielu opisów.
    """)

    st.markdown("""
    Przykładowe anonimowe odpowiedzi respondentów:

    > „Krótka ścieżka decyzyjna.”  
    > „Szybki proces, przyjazny interfejs.”  
    > „Prosta i intuicyjna forma.”  
    > „Pytania dobrze kierowały.”  
    > „Szybko mogłem dostać plan żywieniowy dopasowany pod siebie, bez czytania opisów planów żywieniowych.”
    """)

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Wnioski z pilotażu</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    Badanie pokazało, że GastroMatch ma największą wartość jako narzędzie wspierające
    pierwszy wybór oferty. Prototyp ułatwia użytkownikowi przejście przez decyzję,
    ogranicza liczbę elementów do samodzielnego porównania i jasno wyjaśnia wynik.

    Jednocześnie odpowiedzi respondentów pokazały, że kolejna wersja powinna mocniej
    wspierać **pewność decyzji**. Najczęściej wskazywane kierunki rozwoju to:

    - dodanie cen i porównania wariantów,
    - pokazanie przykładowego menu,
    - dodanie zdjęć posiłków,
    - rozszerzenie filtrów składników i preferencji,
    - pełniejsze uzasadnienie rekomendacji.
    """)

    st.info(
        "Interpretacja: wyniki pilotażu wskazują, że GastroMatch może ułatwiać "
        "i przyspieszać pierwszy wybór oferty. Kolejna wersja powinna skupić się "
        "na dodaniu informacji, które zwiększą pewność użytkownika przed realnym zamówieniem."
    )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Podsumowanie</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    **GastroMatch nie zastępuje pełnej oferty ani konsultacji dietetycznej.**
    Jego rolą jest uproszczenie pierwszego kroku — pomoc użytkownikowi w zawężeniu
    wyboru i wskazaniu opcji, od której warto rozpocząć.

    Na podstawie badania pilotażowego można stwierdzić, że prototyp:

    - skraca czas wyboru,
    - zwiększa łatwość podjęcia decyzji,
    - poprawia zrozumienie rekomendacji,
    - pokazuje konkretne kierunki dalszego rozwoju produktu.
    """)
    st.markdown("---")

    st.markdown(
        '<div class="section-title">Materiały badawcze</div>',
        unsafe_allow_html=True
)

    st.markdown("""
    Formularz ankiety został przygotowany jako narzędzie do zebrania opinii użytkowników
    po przejściu dwóch scenariuszy: wyboru bez GastroMatch oraz wyboru z użyciem prototypu.
    """)

    st.link_button(
        "📝 Zobacz formularz badania pilotażowego",
        "TU_WKLEJ_LINK_DO_ANKIETY"
)

# =========================
# GŁÓWNA APLIKACJA
# =========================

tab_quiz, tab_project, tab_research = st.tabs(
    ["🥗 Quiz", "📌 O projekcie", "📊 Badanie"]
)

with tab_quiz:
    render_progress()

    if st.session_state.step == 0:
        render_start()

    elif st.session_state.step in [1, 2, 3, 4]:
        render_choice_question(st.session_state.step - 1)

    elif st.session_state.step == 5:
        render_preferences_question()

    elif st.session_state.step == 6:
        render_choice_question(4)

    elif st.session_state.step == 7:
        render_choice_question(5)

    elif st.session_state.step >= 8:
        render_result()

with tab_project:
    render_about_project()

with tab_research:
    render_research_tab()