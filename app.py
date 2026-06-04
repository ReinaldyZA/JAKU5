            # ── Model Klasifikasi ──
            st.markdown(
                "<div style='margin-top:18px;'></div>"
                "<div class='sim-section-label'>Model Klasifikasi</div>",
                unsafe_allow_html=True,
            )
            model_label = st.selectbox(
                "Model Klasifikasi",
                ["XGBoost (Rekomendasi)", "Random Forest", "SVM"],
                label_visibility="collapsed",
                help="XGBoost direkomendasikan karena akurasi tertinggi pada data uji.",
                key="sim_model_label",
            )
            model_choice_map = {
                "XGBoost (Rekomendasi)": "xgboost",
                "Random Forest": "random_forest",
                "SVM": "svm",
            }
            st.session_state["sim_model_choice"] = model_choice_map[model_label]
