import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(page_title="Curso: English for Accountants", layout="wide")

# Estructura de navegación tipo "Learning Path"
if "unit" not in st.session_state:
    st.session_state.unit = "Introducción"

st.sidebar.title("📚 Curso Bilingüe")
st.sidebar.markdown("---")
units = ["Introducción", "Unidad 1: Vocabulario Financiero", "Unidad 2: Auditoría y Normas", "Unidad 3: Reportes Corporativos"]
st.session_state.unit = st.sidebar.radio("Selecciona tu progreso:", units)

# Módulo de contenido dinámico
def show_unit(unit_name):
    st.header(unit_name)
    
    if unit_name == "Introducción":
        st.write("Bienvenido al curso de Inglés Técnico para Contadores.")
        st.info("Objetivo: Dominar el 60% del vocabulario crítico para auditorías.")
        
    elif unit_name == "Unidad 1: Vocabulario Financiero":
        st.subheader("Clase: Financial Statements Basics")
        st.markdown("""
        * **Income Statement**: Estado de Resultados.
        * **Balance Sheet**: Balance General.
        * **Cash Flow**: Flujo de Efectivo.
        * **To reconcile**: Conciliar.
        """)
        if st.checkbox("Marcar Unidad 1 como completada"):
            st.success("¡Unidad 1 completada!")

    elif unit_name == "Unidad 2: Auditoría y Normas":
        st.subheader("Clase: Internal Controls & Compliance")
        st.write("Verbos esenciales: *To comply*, *To disclose*, *To audit*.")
        # Aquí insertaremos ejercicios tipo "fill-in-the-blanks" más adelante
        
    elif unit_name == "Unidad 3: Reportes Corporativos":
        st.subheader("Clase: Formal Reporting")
        st.write("Estructura de conectores para informes: *Furthermore*, *Consequently*, *Nevertheless*.")

# Ejecución
show_unit(st.session_state.unit)

# Footer de progreso persistente
st.sidebar.markdown("---")
st.sidebar.progress(33) # Esto se calculará dinámicamente según el progreso
