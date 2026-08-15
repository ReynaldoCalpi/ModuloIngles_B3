import streamlit as st
import pandas as pd
import random

# Configuración de la página
st.set_page_config(
    page_title="English for Accountants & Auditors (B3+)",
    page_icon="💼",
    layout="wide"
)

# Inicialización de estado (Session State)
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "flashcard_idx" not in st.session_state:
    st.session_state.flashcard_idx = 0
if "show_translation" not in st.session_state:
    st.session_state.show_translation = False

st.title("💼 English Platform for Professional Accountants & Auditors")
st.markdown("### Domina el inglés nivel B3+ basado en las guías técnicas esenciales para contadores y auditores.")

# Base de datos de Flashcards
flashcards_db = [
    {"category": "Linking Words", "term": "Furthermore / Moreover", "translation": "Además / Es más (Adición formal en informes)"},
    {"category": "Linking Words", "term": "Nevertheless / Nonetheless", "translation": "No obstante / Sin embargo (Contraste)"},
    {"category": "Linking Words", "term": "Consequently / Therefore", "translation": "Por consiguiente / Por lo tanto (Causa-Efecto)"},
    {"category": "Linking Words", "term": "In light of", "translation": "A la luz de / En vista de (Análisis de hallazgos)"},
    {"category": "Modal Verbs", "term": "Must", "translation": "Obligación estricta / Cumplimiento normativo (IFRS/GAAP)"},
    {"category": "Modal Verbs", "term": "Should", "translation": "Recomendación / Consejo en control interno"},
    {"category": "Auxiliary", "term": "Have you finalized...?", "translation": "¿Has finalizado...? (Present Perfect en auditoría)"},
    {"category": "Core Verbs", "term": "To disclose", "translation": "Revelar / Divulgar información financiera"},
    {"category": "Core Verbs", "term": "To comply with", "translation": "Cumplir con regulaciones o leyes fiscales"}
]

# Validación de seguridad para evitar IndexError
if st.session_state.flashcard_idx >= len(flashcards_db):
    st.session_state.flashcard_idx = 0

# Menú Principal por Pestañas ampliadas
tabs = st.tabs([
    "⚡ Flashcards Clave",
    "📊 12 Tiempos Verbales", 
    "⚙️ Auxiliares & Modales", 
    "🔗 Conectores & Linking", 
    "❓ Question Words",
    "💬 Phrasal Verbs & Expresiones", # NUEVA PESTAÑA DINÁMICA
    "🎯 Simulador & Examen"
])

# ----------------------------------------------------
# PESTAÑA 0: FLASHCARDS INTERACTIVAS
# ----------------------------------------------------
with tabs[0]:
    st.header("Flashcards de Memorización Estratégica")
    current_card = flashcards_db[st.session_state.flashcard_idx]
    
    st.info(f"Categoría: **{current_card['category']}** (Tarjeta {st.session_state.flashcard_idx + 1} de {len(flashcards_db)})")
    
    with st.container(border=True):
        st.markdown(f"<h3 style='text-align: center; color: #1f77b4;'>{current_card['term']}</h3>", unsafe_allow_html=True)
        
        if st.session_state.show_translation:
            st.markdown(f"<p style='text-align: center; font-size: 1.2em; color: #2ca02c;'><b>Traducción / Uso:</b> {current_card['translation']}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: center; color: gray;'>Haz clic en el botón para revelar el significado técnico.</p>", unsafe_allow_html=True)
            
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        if st.button("🔄 Mostrar / Ocultar Significado"):
            st.session_state.show_translation = not st.session_state.show_translation
            st.rerun()
    with col_f2:
        if st.button("➡️ Siguiente Tarjeta"):
            st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % len(flashcards_db)
            st.session_state.show_translation = False
            st.rerun()
    with col_f3:
        if st.button("⬅️ Anterior Tarjeta"):
            st.session_state.flashcard_idx = (st.session_state.flashcard_idx - 1) % len(flashcards_db)
            st.session_state.show_translation = False
            st.rerun()

# ----------------------------------------------------
# PESTAÑA 1: LOS 12 TIEMPOS VERBALES
# ----------------------------------------------------
with tabs[1]:
    st.header("Los 12 Tiempos Verbales en Contexto Contable")
    tenses_data = {
        "Categoría": ["Presente", "Presente", "Pasado", "Pasado", "Futuro"],
        "Tiempo": ["Simple", "Perfect", "Simple", "Continuous", "Simple"],
        "Ejemplo": ["We reconcile", "We have identified", "Management approved", "The team was testing", "The board will approve"],
        "Uso en Auditoría": ["Políticas contables", "Hallazgos con impacto actual", "Hechos históricos", "Actividades de campo", "Proyecciones y presupuestos"]
    }
    st.dataframe(pd.DataFrame(tenses_data), use_container_width=True)

# ----------------------------------------------------
# PESTAÑA 2: AUXILIARES Y MODALES
# ----------------------------------------------------
with tabs[2]:
    st.header("Verbos Auxiliares (Be, Do, Have) y Modales")
    st.markdown("""
    * **BE**: *The financial statements **were audited*** (Voz pasiva).
    * **DO**: ***Do** you require additional documentation?* (Interrogativo).
    * **HAVE**: *Management **has implemented** the action* (Perfect Tense).
    * **MUST**: *We **must** adhere to IFRS* (Obligación normativa).
    * **SHOULD**: *The client **should** disclose this* (Recomendación).
    """)

# ----------------------------------------------------
# PESTAÑA 3: CONECTORES Y LINKING WORDS
# ----------------------------------------------------
with tabs[3]:
    st.header("Guía Maestra de Conectores")
    st.markdown("""
    * **Adición:** Furthermore, Moreover, In addition to.
    * **Contraste:** However, Nevertheless, On the contrary.
    * **Causa/Efecto:** Therefore, Consequently, Due to.
    """)

# ----------------------------------------------------
# PESTAÑA 4: QUESTION WORDS Y VERBOS COMUNES
# ----------------------------------------------------
with tabs[4]:
    st.header("Question Words en Entrevistas")
    st.markdown("""
    * **WHO**: *Who authorized this journal entry?*
    * **WHAT**: *What caused the variance?*
    * **WHEN**: *When was the count performed?*
    """)

# ----------------------------------------------------
# PESTAÑA 5: PHRASAL VERBS & EXPRESIONES (NUEVO - DINÁMICO)
# ----------------------------------------------------
with tabs[5]:
    st.header("💬 Phrasal Verbs & Business Expressions")
    st.write("Expresiones avanzadas aplicadas al entorno financiero. Usa el buscador para filtrar en tiempo real.")
    
    # Base de datos dinámica para Phrasal Verbs
    phrasal_data = [
        {"Término": "Write off", "Tipo": "Phrasal Verb", "Significado": "Cancelar / Dar de baja (un activo o deuda incursionada)", "Contexto": "We need to write off these bad debts."},
        {"Término": "Carry forward", "Tipo": "Phrasal Verb", "Significado": "Trasladar un saldo al siguiente periodo contable", "Contexto": "The net loss can be carried forward."},
        {"Término": "Break down", "Tipo": "Phrasal Verb", "Significado": "Desglosar cifras, datos o facturas", "Contexto": "Could you break down these travel expenses?"},
        {"Término": "Bail out", "Tipo": "Phrasal Verb", "Significado": "Rescatar financieramente (a una empresa en quiebra)", "Contexto": "The government bailed out the struggling bank."},
        {"Término": "Rule of thumb", "Tipo": "Expresión", "Significado": "Regla general / Principio práctico", "Contexto": "As a rule of thumb, we keep 3 months of cash reserves."},
        {"Término": "Bottom line", "Tipo": "Expresión", "Significado": "Línea final (Beneficio neto) o la conclusión más importante", "Contexto": "How will this new tax impact our bottom line?"}
    ]
    df_phrasals = pd.DataFrame(phrasal_data)
    
    # Input interactivo
    busqueda = st.text_input("🔍 Buscar término, significado o tipo (Ej: 'write', 'saldo', 'Expresión'):")
    
    if busqueda:
        # Filtrado dinámico usando Pandas
        df_filtrado = df_phrasals[
            df_phrasals.apply(lambda row: row.astype(str).str.contains(busqueda, case=False).any(), axis=1)
        ]
        st.dataframe(df_filtrado, use_container_width=True)
    else:
        st.dataframe(df_phrasals, use_container_width=True)

# ----------------------------------------------------
# PESTAÑA 6: SIMULADOR Y EXAMEN DE DOMINIO B3+
# ----------------------------------------------------
with tabs[6]:
    st.header("🎯 Examen de Dominio B3+")
    if not st.session_state.quiz_started:
        if st.button("🚀 Comenzar Examen"):
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.quiz_step = 0
            st.rerun()
    else:
        # Lógica resumida del quiz existente para mantener el archivo listo para usar
        st.write("Examen en progreso... (Integraremos más preguntas en la siguiente iteración).")
        if st.button("🔄 Reiniciar"):
            st.session_state.quiz_started = False
            st.rerun()
