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

# Menú Principal por Pestañas (Estructura de Curso Profesional)
tabs = st.tabs([
    "⚡ Flashcards Clave",
    "📊 12 Tiempos Verbales", 
    "⚙️ Auxiliares & Modales", 
    "🔗 Conectores & Linking Words", 
    "❓ Question Words & Verbos",
    "🎯 Simulador & Examen B3+"
])

# ----------------------------------------------------
# PESTAÑA 0: FLASHCARDS INTERACTIVAS
# ----------------------------------------------------
with tabs[0]:
    st.header("Flashcards de Memorización Estratégica")
    st.write("Domina los conceptos clave que componen la base del inglés técnico corporativo.")
    
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
    st.write("Estructuras fundamentales extraídas de tu guía para redacción de informes financieros y de auditoría.")
    
    tenses_data = {
        "Categoría": ["Presente", "Presente", "Presente", "Presente", "Pasado", "Pasado", "Pasado", "Pasado", "Futuro", "Futuro", "Futuro", "Futuro"],
        "Tiempo Verbal": [
            "Simple", "Continuous", "Perfect", "Perfect Continuous", 
            "Simple", "Continuous", "Perfect", "Perfect Continuous", 
            "Simple", "Continuous", "Perfect", "Perfect Continuous"
        ],
        "Estructura / Ejemplo General": [
            "I go / We reconcile", "I am going / We are auditing", "I have gone / We have identified", "I have been going / We have been reviewing",
            "I went / Management approved", "I was going / The team was testing", "I had gone / We had verified", "I had been going / They had been checking",
            "I will go / The board will approve", "I will be going / We will be evaluating", "I will have gone / We will have finished", "I will have been going / ... "
        ],
        "Aplicación Práctica en Auditoría": [
            "Políticas contables regulares", "Revisiones en curso en este momento", "Hallazgos con impacto actual en estados financieros", "Procesos continuos de revisión interna",
            "Hechos históricos de periodos cerrados", "Actividades específicas durante la visita de campo", "Acciones completadas antes de otro evento pasado", "Duración de una tarea previa en la auditoría",
            "Proyecciones, presupuestos y planes futuros", "Acciones en desarrollo durante futuras auditorías", "Balances cerrados para fecha futura establecida", "Proyecciones de tendencia a largo plazo"
        ]
    }
    st.dataframe(pd.DataFrame(tenses_data), use_container_width=True)

# ----------------------------------------------------
# PESTAÑA 2: AUXILIARES Y MODALES
# ----------------------------------------------------
with tabs[2]:
    st.header("Verbos Auxiliares (Be, Do, Have) y Modales")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Auxiliary Verbs (BE, DO, HAVE)")
        st.markdown("""
        * **BE (Am, Are, Is, Was, Were)**: Esencial para la voz pasiva en informes técnicos (*"The financial statements **were audited**"*).
        * **DO (Do, Does, Did)**: Utilizado para formular preguntas e interrogar sobre procesos (*"**Do** you require additional documentation?"*).
        * **HAVE (Have, Has, Had)**: Clave para tiempos perfectos y reportar hallazgos cerrados (*"Management **has implemented** the corrective action"*).
        """)
        
    with col2:
        st.subheader("Modal Verbs (Obligación y Certeza)")
        st.markdown("""
        * **Must**: Obligación estricta y cumplimiento normativo (*"We **must** adhere to IFRS guidelines"*).
        * **Should**: Recomendación profesional y consejos de auditoría (*"The client **should** disclose related parties"*).
        * **Can / Could**: Habilidad, posibilidad y peticiones formales de papeles de trabajo (*"**Could** you provide the general ledger?"*).
        * **May**: Permiso o probabilidad formal (*"This variance **may** indicate a control deficiency"*).
        """)

# ----------------------------------------------------
# PESTAÑA 3: CONECTORES Y LINKING WORDS
# ----------------------------------------------------
with tabs[3]:
    st.header("Guía Maestra de Conectores (Linking Words)")
    st.write("Estructura clasificada para redactar informes fluidos, profesionales y de nivel ejecutivo.")
    
    c_col1, c_col2, c_col3 = st.columns(3)
    with c_col1:
        st.markdown("#### ➕ Adición & Secuencia")
        st.markdown("""
        * Furthermore / Moreover (Además)
        * In addition to (En adición a)
        * Firstly / Secondly (En primer / segundo lugar)
        * Subsequently / Afterwards (Posteriormente)
        """)
    with c_col2:
        st.markdown("#### 🔄 Contraste & Concesión")
        st.markdown("""
        * However / Nevertheless (Sin embargo / No obstante)
        * On the contrary (Por el contrario)
        * Whereas / While (Mientras que)
        * Despite this (A pesar de esto)
        """)
    with c_col3:
        st.markdown("#### 🎯 Causa, Efecto & Conclusión")
        st.markdown("""
        * Therefore / Consequently (Por lo tanto / En consecuencia)
        * Due to / Owing to (Debido a)
        * To sum up / Ultimately (En resumen / En última instancia)
        * In light of (A la luz de)
        """)

# ----------------------------------------------------
# PESTAÑA 4: QUESTION WORDS Y VERBOS COMUNES
# ----------------------------------------------------
with tabs[4]:
    st.header("Question Words y Verbos Clave de Auditoría")
    
    q_col1, q_col2 = st.columns(2)
    with q_col1:
        st.subheader("Question Words en Entrevistas")
        st.markdown("""
        * **WHO**: *Who authorized this journal entry?* (Investigar responsabilidades).
        * **WHAT**: *What caused the inventory shrinkage?* (Indagar causas).
        * **WHEN**: *When was the physical count performed?* (Verificar temporalidad).
        * **WHERE**: *Where are the supporting invoices stored?* (Localización física).
        * **WHY**: *Why is there a delay in bank reconciliations?* (Analizar justificaciones).
        * **WHOSE**: *Whose signature is on this voucher?* (Verificar autorizaciones).
        """)
    with q_col2:
        st.subheader("Verbos Esenciales del Entorno Contable")
        st.markdown("""
        * **To reconcile**: Conciliar cuentas o saldos.
        * **To report**: Informar o reportar hallazgos.
        * **To review**: Revisar documentación contable.
        * **To assess**: Evaluar riesgos o controles.
        * **To provide**: Proveer información o papeles de trabajo.
        * **To achieve**: Lograr metas financieras o de control.
        """)

# ----------------------------------------------------
# PESTAÑA 5: SIMULADOR Y EXAMEN DE DOMINIO B3+
# ----------------------------------------------------
with tabs[5]:
    st.header("🎯 Simulador de Entrevistas y Examen de Dominio B3+")
    
    with st.expander("📖 Repaso rápido teóricio antes del examen"):
        st.markdown("""
        * **Present Perfect**: Utilizado para hallazgos con impacto actual en los estados financieros.
        * **Linking Words**: Usa *'Therefore'* para causas directas y *'Nevertheless'* para contrastar hallazgos.
        * **Modals**: *'Must'* se reserva para exigencias normativas ineludibles.
        """)
    
    quiz_data = [
        {
            "q": "El cliente presenta errores materiales en sus cuentas. ¿Qué tiempo verbal refleja mejor un hallazgo con impacto actual?",
            "options": [
                "Management has presented inaccurate financial statements.", 
                "Management had presented inaccurate financial statements.", 
                "Management presents inaccurate financial statements.", 
                "Management will present inaccurate financial statements."
            ],
            "answer": "Management has presented inaccurate financial statements.",
            "explanation": "El *Present Perfect* conecta un evento pasado (el error cometido) con su consecuencia directa y vigente en la auditoría actual."
        },
        {
            "q": "Complete la oración técnica: 'The internal controls showed significant weaknesses; ________, we increased substantive testing.'",
            "options": ["Therefore", "However", "In spite of", "Whereas"],
            "answer": "Therefore",
            "explanation": "Se requiere un conector de consecuencia lógica (*Therefore* / Por lo tanto) derivado de la debilidad de los controles."
        },
        {
            "q": "Elige el verbo modal correcto para indicar un requisito normativo obligatorio en auditoría:",
            "options": ["Can", "May", "Must", "Could"],
            "answer": "Must",
            "explanation": "*'Must'* denota una obligación estricta bajo normativas internacionales (IFRS/GAAP)."
        }
    ]
    
    if not st.session_state.quiz_started:
        if st.button("🚀 Comenzar Examen de Dominio"):
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.quiz_step = 0
            st.rerun()
    else:
        step = st.session_state.quiz_step
        if step < len(quiz_data):
            current_q = quiz_data[step]
            st.markdown(f"**Pregunta {step + 1} de {len(quiz_data)}:**")
            st.write(current_q["q"])
            
            choice = st.radio("Elige una opción:", current_q["options"], key=f"q_{step}")
            
            if st.button("Verificar respuesta"):
                if choice == current_q["answer"]:
                    st.success("¡Correcto! Excelente aplicación técnica.")
                    st.session_state.score += int(100 / len(quiz_data))
                else:
                    st.error(f"Incorrecto. La respuesta correcta era: **{current_q['answer']}**")
                
                st.info(f"**¿Por qué?:** {current_q['explanation']}")
                
                if st.button("Siguiente pregunta / Finalizar"):
                    st.session_state.quiz_step += 1
                    st.rerun()
        else:
            st.markdown(f"### 🏆 Puntaje Final: {st.session_state.score} / 100")
            if st.session_state.score >= 70:
                st.balloons()
                st.success("¡Felicidades! Has demostrado un nivel sólido para interactuar en entornos bilingües de auditoría.")
            else:
                st.info("Buen intento. Repasa las pestañas de teoría y flashcards para afianzar los conceptos.")
                
            if st.button("🔄 Reiniciar Examen"):
                st.session_state.quiz_started = False
                st.session_state.score = 0
                st.session_state.quiz_step = 0
                st.rerun()
