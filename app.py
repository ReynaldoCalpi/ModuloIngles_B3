import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="B3+ Accounting English", layout="wide")

# Inicialización de estado
if 'progreso' not in st.session_state:
    st.session_state.progreso = 0

# Título y Bienvenida
st.title("💼 B3+ English for Accountants & Auditors")
st.markdown("Plataforma interactiva basada en el curso de Inglés Técnico Contable.")

# Definición de las unidades de aprendizaje
tabs = st.tabs([
    "📍 1. Vocabulario Esencial", 
    "📊 2. Estados Financieros", 
    "🔍 3. Auditoría y Compliance", 
    "📝 4. Ejercicios & Quiz"
])

# Unidad 1: Vocabulario
with tabs[0]:
    st.header("Módulo 1: Vocabulario Esencial")
    voc_data = {
        "Término": ["Assets", "Liabilities", "Equity", "Revenue", "Accrual Accounting"],
        "Definición": ["Activos", "Pasivos", "Patrimonio", "Ingresos", "Contabilidad por devengo"]
    }
    st.table(pd.DataFrame(voc_data))

# Unidad 2: Estados Financieros
with tabs[1]:
    st.header("Módulo 2: Estados Financieros")
    st.markdown("""
    * **Balance Sheet (Statement of Financial Position)**: La foto financiera a una fecha.
    * **Income Statement (Profit & Loss)**: El desempeño durante un periodo.
    * **Cash Flow Statement**: Movimiento de efectivo.
    """)

# Unidad 3: Auditoría
with tabs[2]:
    st.header("Módulo 3: Auditoría y Normas")
    st.write("Verbos clave: *To disclose* (revelar), *To reconcile* (conciliar), *To comply* (cumplir).")

# Unidad 4: Quiz interactivo
with tabs[3]:
    st.header("Módulo 4: Evaluación de Dominio")
    pregunta = st.radio("¿Qué significa 'Liabilities'?", ["Activos", "Patrimonio", "Pasivos"])
    if st.button("Enviar respuesta"):
        if pregunta == "Pasivos":
            st.success("Correcto: Pasivos/Obligaciones.")
            st.session_state.progreso += 25
        else:
            st.error("Incorrecto, intenta de nuevo.")

# Sidebar de progreso
st.sidebar.title("Tu Progreso")
st.sidebar.progress(st.session_state.progreso)
