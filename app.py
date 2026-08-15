import streamlit as st
import pandas as pd
import random

# Configuración de la página
st.set_page_config(
    page_title="English for Accountants & Auditors (B3+)",
    page_icon="💼",
    layout="wide"
)

# Inicialización de estado para la gamificación / examen
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

st.title("💼 English Platform for Professional Accountants & Auditors")
st.markdown("### Domina el inglés nivel B3+ enfocado en auditoría, finanzas y negocios corporativos.")

# Menú Principal por Pestañas
tabs = st.tabs([
    "📊 12 Tiempos Verbales", 
    "⚙️ Auxiliares & Modales", 
    "🔗 Conectores & Linking Words", 
    "❓ Question Words", 
    "📝 Examen de Dominio B3+"
])

with tabs[0]:
    st.header("Los 12 Tiempos Verbales Aplicados a Finanzas")
    st.write("Estructuras clave para redactar informes de auditoría y estados financieros en inglés.")
    
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

with tabs[1]:
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

with tabs[2]:
    st.header("Conectores y Linking Words para Informes Técnicos")
    st.write("Indispensables para dar fluidez, contraste y jerarquía a tus dictámenes de auditoría.")
    
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

with tabs[3]:
    st.header("Question Words para Entrevistas de Auditoría (Inquiries)")
    st.markdown("""
    * **WHO**: *Who authorized this disbursement?* (Investigar responsabilidades).
    * **WHAT**: *What caused the variance in the ledger?* (Analizar desviaciones).
    * **WHEN**: *When was the inventory count performed?* (Verificar fechas clave).
    * **WHERE**: *Where are the physical fixed assets located?* (Comprobación física).
    * **WHY**: *Why is there a delay in bank reconciliations?* (Evaluar controles internos).
    * **WHOSE**: *Whose signature is on this payment voucher?* (Revisar autorizaciones).
    """)

with tabs[4]:
    st.header("Examen de Validación de Conocimientos (Nivel B3+)")
    st.write("Pon a prueba tu dominio técnico con este quiz interactivo diseñado para futuros auditores bilingües.")
    
    questions = [
        {
            "q": "Selecciona el conector correcto para indicar una consecuencia directa en un informe:",
            "options": ["However", "Therefore", "Whereas", "Although"],
            "answer": "Therefore"
        },
        {
            "q": "¿Qué tiempo verbal describe una acción completada en el pasado que tiene impacto en el presente (ej. un hallazgo detectado)?",
            "options": ["Past Simple", "Present Perfect", "Future Simple", "Past Continuous"],
            "answer": "Present Perfect"
        },
        {
            "q": "Elige el verbo modal adecuado para expresar una obligación regulatoria estricta en auditoría:",
            "options": ["Can", "May", "Must", "Could"],
            "answer": "Must"
        },
        {
            "q": "¿Cuál de las siguientes palabras funciona para mostrar contraste técnico?",
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
                st.markdown("🌟 **¡Nivel Aprobado!** Estás listo para redactar reportes corporativos de alto nivel.")
            else:
                st.markdown("💡 Te sugerimos repasar las pestañas teóricas y volver a intentar el examen.")
            
            if st.button("🔄 Reiniciar Examen"):
                st.session_state.quiz_started = False
                st.session_state.score = 0
                st.session_state.quiz_step = 0
                st.rerun()
