with tabs[5]:
    st.header("🎯 Quiz: Auditoría y Finanzas B3+")
    
    # Módulo de Repaso Pre-Quiz
    with st.expander("📖 Repaso rápido antes del examen"):
        st.markdown("""
        * **Present Perfect**: Se usa en auditoría para describir acciones que tienen un efecto en el presente (ej. 'We have found a discrepancy').
        * **Linking Words**: 'Consequently' indica una consecuencia directa, mientras que 'Nevertheless' introduce una concesión o contraste.
        * **Modals**: 'Must' es mandatorio en normas contables (IFRS/GAAP).
        """)
    
    # Base de conocimientos del Quiz
    quiz_data = [
        {
            "q": "El cliente ha presentado estados financieros con errores. ¿Qué oración es más precisa para un informe?",
            "options": [
                "Management has presented inaccurate financial statements.", 
                "Management had presented inaccurate financial statements.", 
                "Management presents inaccurate financial statements.", 
                "Management will present inaccurate financial statements."
            ],
            "answer": "Management has presented inaccurate financial statements.",
            "explanation": "El *Present Perfect* es ideal aquí porque el error tiene un impacto actual en la auditoría."
        },
        {
            "q": "Complete la oración: 'The internal controls were weak; ________, we decided to perform more substantive tests.'",
            "options": ["Therefore", "However", "In spite of", "And"],
            "answer": "Therefore",
            "explanation": "Se requiere un conector de consecuencia (Cause & Effect) debido a la relación lógica."
        }
    ]
    
    # Lógica del Quiz
    if not st.session_state.quiz_started:
        if st.button("🚀 Comenzar Quiz de Auditoría"):
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
                    st.success("¡Correcto!")
                    st.session_state.score += 50
                else:
                    st.error(f"Incorrecto. La respuesta correcta era: {current_q['answer']}")
                
                st.info(f"**¿Por qué?** {current_q['explanation']}")
                
                if st.button("Siguiente pregunta"):
                    st.session_state.quiz_step += 1
                    st.rerun()
        else:
            st.write(f"### Tu puntaje final: {st.session_state.score}/100")
            if st.session_state.score == 100:
                st.balloons()
            if st.button("Reiniciar"):
                st.session_state.quiz_started = False
                st.rerun()
