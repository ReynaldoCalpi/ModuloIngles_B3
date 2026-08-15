import streamlit as st
import pandas as pd
import random

# Configuración de la página
st.set_page_config(
    page_title="English for Accountants & Auditors (B3+)",
    page_icon="💼",
    layout="wide"
)

# Inicialización de variables de estado (Session State) para interactividad robusta
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
st.markdown("### Plataforma interactiva B3+ orientada a la contabilidad, auditoría y finanzas corporativas.")

# Menú Principal por Pestañas
tabs = st.tabs([
    "⚡ Flashcards Clave (60% Base)",
    "📊 12 Tiempos Verbales", 
    "⚙️ Auxiliares & Modales", 
    "🔗 Conectores & Linking Words", 
    "🎯 Simulador de Entrevistas",
    "📝 Examen de Dominio B3+"
])

# ----------------------------------------------------
# PESTAÑA 0: FLASHCARDS INTERACTIVAS DE MEMORIZACIÓN
# ----------------------------------------------------
with tabs[0]:
    st.header("Flashcards de Memorización Estratégica")
    st.write("Domina el vocabulario esencial, verbos, conectores y palabras de enlace extraídas de tus guías de estudio.")
    
    flashcards_db = [
        {"category": "Linking Words", "term": "Furthermore / Moreover", "translation": "Además / Es más (Adición formal)"},
        {"category": "Linking Words", "term": "Nevertheless / Nonetheless", "translation": "No obstante / Sin embargo (Contraste)"},
        {"category": "Linking Words", "term": "Consequently / Therefore", "translation": "Por consiguiente / Por lo tanto (Causa-Efecto)"},
        {"category": "Linking Words", "term": "In light of", "translation": "A la luz de / En vista de (Conclusión / Análisis)"},
        {"category": "Modal Verbs", "term": "Must", "translation": "Obligación estricta / Necesidad regulatoria"},
        {"category": "Modal Verbs", "term": "Should", "translation": "Recomendación / Consejo profesional"},
        {"category": "Auxiliary", "term": "Have you finalized...?", "translation": "¿Has finalizado...? (Present Perfect en auditoría)"},
        {"category": "Common Verbs", "term": "To disclose", "translation": "Revelar / Divulgar (Información financiera)"},
        {"category": "Common Verbs", "term": "To comply with", "translation": "Cumplir con (Normativa / Leyes)"},
        {"category": "Question Words", "term": "Whose signature...?", "translation": "¿De quién es la firma...? (Indagar posesión/autorización)"}
    ]
    
    current_card = flashcards_db[st.session_state.flashcard_idx]
    
    st.info(f"Categoría: **{current_card['category']}** (Tarjeta {st.session_state.flashcard_idx + 1} de {len(flashcards_db)})")
    
    # Contenedor visual tipo tarjeta
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
# PESTAÑA 1: TIEMPOS VERBALES
# ----------------------------------------------------
with tabs[1]:
    st.header("Los 12 Tiempos Verbales Aplicados a Finanzas")
    st.write("Estructuras clave para redactar informes de auditoría y estados financieros en inglés con precisión B3+.")
    
    tenses_data = {
        "Tiempo": ["Present Simple", "Present Continuous", "Present Perfect", "Past Simple", "Future Simple"],
        "Uso en Auditoría": ["Hechos y políticas contables generales", "Revisiones o auditorías en curso actualmente", "Acciones completadas con impacto financiero actual", "Hallazgos de auditoría de periodos anteriores", "Proyecciones y presupuestos futuros"],
        "Ejemplo Práctico": [
            "We **reconcile** the bank accounts monthly.",
            "The team **is auditing** the inventory right now.",
            "We **have identified** a material weakness in internal controls.",
            "Management **approved** the financial statements last week.",
            "The board **will approve** the fiscal budget tomorrow."
        ]
    }
    df_tenses = pd.DataFrame(tenses_data)
    st.table(df_tenses)

# ----------------------------------------------------
# PESTAÑA 2: AUXILIARES Y MODALES
# ----------------------------------------------------
with tabs[2]:
    st.header("Verbos Auxiliares y Modales en el Ámbito Corporativo")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Auxiliares (Be, Do, Have)")
        st.markdown("""
        * **BE**: *I am reviewing*, *The report was signed*. (Voz pasiva muy usada en auditoría).
        * **DO**: *Do you require additional documentation?*, *The company does not comply*.
        * **HAVE**: *Have you finalized the trial balance?*, *Management has implemented the changes*.
        """)
        
    with col2:
        st.subheader("Modal Verbs (Obligación y Certeza)")
        st.markdown("""
        * **Must**: *We must comply with IFRS standards.* (Obligación estricta).
        * **Should**: *The client should disclose related-party transactions.* (Recomendación/Consejo).
        * **Can / Could**: *Could you provide the supporting invoices?* (Petición formal).
        """)

# ----------------------------------------------------
# PESTAÑA 3: CONECTORES
# ----------------------------------------------------
with tabs[3]:
    st.header("Conectores y Linking Words para Informes Técnicos")
    st.write("Indispensables para dar fluidez, contraste y jerarquía a tus dictámenes profesionales.")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        st.markdown("#### ➕ Adición / Secuencia")
        st.markdown("- **Furthermore / Moreover** (Además)\n- **In addition to** (En adición a)\n- **Consequently** (Por consiguiente)\n- **Therefore** (Por lo tanto)")
    with col_c2:
        st.markdown("#### 🔄 Contraste")
        st.markdown("- **However** (Sin embargo)\n- **Nevertheless** (No obstante)\n- **On the contrary** (Por el contrario)\n- **Whereas** (Mientras que)")
    with col_c3:
        st.markdown("#### 🎯 Conclusión")
        st.markdown("- **To sum up / Ultimately** (En resumen)\n- **As a result** (Como resultado)\n- **In light of** (A la luz de)")

# ----------------------------------------------------
# PESTAÑA 4: SIMULADOR DE ENTREVISTAS TÉCNICAS
# ----------------------------------------------------
with tabs[4]:
    st.header("Simulador de Entrevistas y Reuniones de Auditoría")
    st.write("Practica cómo responder a preguntas comunes que te harán gerentes o socios en un entorno bilingüe.")
    
    scenario = st.selectbox(
        "Selecciona el escenario de auditoría:",
        [
            "Discutir una diferencia de inventario (Inventory Variance)",
            "Solicitar documentación faltante de conciliación bancaria",
            "Explicar un hallazgo de control interno"
        ]
    )
    
    if scenario == "Discutir una diferencia de inventario (Inventory Variance)":
        st.markdown("""
        > **Situación:** Estás reunido con el Gerente de Operaciones y debes seccionar el problema con seguridad.
        * **Pregunta del Gerente (Auditor):** *"Why is there a significant variance between the physical count and the ledger?"*
        * **Tu respuesta recomendada (Nivel B3+):**  
          *"In light of our review, **furthermore**, we noticed that several dispatch notes were not recorded in the system prior to the cut-off date. **Consequently**, this caused a temporary discrepancy in the final balance."*
        """)
    elif scenario == "Solicitar documentación faltante de conciliación bancaria":
        st.markdown("""
        > **Situación:** Necesitas pedir papeles de trabajo de forma formal y educada.
        * **Pregunta / Petición:**  
          *"Could you provide the outstanding check listings and bank confirmations for December, please? We **must** verify these balances before signing off."*
        """)
    else:
        st.markdown("""
        > **Situación:** Presentando debilidades de control al comité de gerencia.
        * **Hallazgo:**  
          *"Although management implemented strong segregation of duties in sales, **nevertheless**, we found that purchase orders lack proper secondary authorization."*
        """)

# ----------------------------------------------------
# PESTAÑA 5: EXAMEN DE DOMINIO B3+
# ----------------------------------------------------
with tabs[5]:
    st.header("Examen de Validación de Conocimientos (Nivel B3+)")
    st.write("Pon a prueba tu dominio técnico con este quiz interactivo diseñado para futuros contadores y auditores bilingües.")
    
    questions = [
        {
            "q": "Selecciona el conector correcto para indicar una consecuencia directa en un informe de auditoría:",
            "options": ["However", "Therefore", "Whereas", "Although"],
            "answer": "Therefore"
        },
        {
            "q": "¿Qué tiempo verbal describe una acción completada en el pasado que tiene impacto en el presente (ej. un hallazgo detectado)?",
            "options": ["Past Simple", "Present Perfect", "Future Simple", "Past Continuous"],
            "answer": "Present Perfect"
        },
        {
            "q": "Elige el verbo modal adecuado para expresar una obligación regulatoria estricta:",
            "options": ["Can", "May", "Must", "Could"],
            "answer": "Must"
        },
        {
            "q": "¿Cuál de las siguientes opciones funciona para mostrar contraste técnico formal?",
            "options": ["Furthermore", "Nevertheless", "Similarly", "Consequently"],
            "answer": "Nevertheless"
        }
    ]
    
    if not st.session_state.quiz_started:
        if st.button("🚀 Comenzar Examen"):
            st.session_state.quiz_started = True
            st.session_state.score = 0
            st.session_state.quiz_step = 0
            st.rerun()
    else:
        step = st.session_state.quiz_step
        if step < len(questions):
            current_q = questions[step]
            st.markdown(f"**Pregunta {step + 1} de {len(questions)}:**")
            st.write(current_q["q"])
            
            choice = st.radio("Selecciona tu respuesta:", current_q["options"], key=f"q_{step}")
            
            if st.button("Enviar Respuesta"):
                if choice == current_q["answer"]:
                    st.success("¡Correcto! Excelente dominio técnico.")
                    st.session_state.score += 25
                else:
                    st.error(f"Incorrecto. La respuesta correcta era: **{current_q['answer']}**")
                
                st.session_state.quiz_step += 1
                st.rerun()
        else:
            st.balloons()
            st.success(f"¡Examen Finalizado! Tu puntaje final es: **{st.session_state.score} / 100**")
            if st.session_state.score >= 75:
                st.markdown("🌟 **¡Nivel Aprobado!** Estás un paso más cerca de ser un contador-auditor bilingüe de élite.")
            else:
                st.markdown("💡 Te sugerimos repasar las flashcards y las pestañas teóricas para mejorar tu puntaje.")
            
            if st.button("🔄 Reiniciar Examen"):
                st.session_state.quiz_started = False
                st.session_state.score = 0
                st.session_state.quiz_step = 0
                st.rerun()
