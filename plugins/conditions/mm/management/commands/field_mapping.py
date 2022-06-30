FIELD_MAPPING = {
    ("datos demograficos.csv", "centro_procedencia"): (
        "MMDiagnosisDetails",
        "previous_hospital",
    ),
    ("datos demograficos.csv", "comentarios"): ("Demographics", "comments"),
    ("datos demograficos.csv", "c�digo de paciente"): (
        "Demographics",
        "hospital_number",
    ),
    ("datos demograficos.csv", "fecha_nacimiento"): ("Demographics", "date_of_birth"),
    ("datos demograficos.csv", "gmp_comentarios"): (
        "MMPastMedicalHistory",
        "gmp_comments",
    ),
    ("datos demograficos.csv", "gmp_fecha_diag"): (
        "MMPastMedicalHistory",
        "monoclonal_pathology_of_uncertain_meaning_date",
    ),
    ("datos demograficos.csv", "gmp_gmsi"): (
        "MMPastMedicalHistory",
        "monoclonal_pathology_of_uncertain_meaning",
    ),
    ("datos demograficos.csv", "gmp_mmasintomatico"): (
        "MMPastMedicalHistory",
        "asymtomatic_multiple_myeloma",
    ),
    ("datos demograficos.csv", "gmp_mmsintomatico"): (
        "MMPastMedicalHistory",
        "symtomatic_multiple_myeloma",
    ),
    ("datos demograficos.csv", "gmp_no"): (
        "MMPastMedicalHistory",
        "monoclonal_pathology",
    ),
    ("datos demograficos.csv", "gmp_plasmocitomaextramedular"): (
        "MMPastMedicalHistory",
        "external_pasmocytoma",
    ),
    ("datos demograficos.csv", "insu_ren_cron_prev"): (
        "MMPastMedicalHistory",
        "chronic_renal_insufficiency",
    ),
    ("datos demograficos.csv", "ircp_fecha_diag"): (
        "MMPastMedicalHistory",
        "chronic_renal_insufficiency_diagnosis_date",
    ),
    ("datos demograficos.csv", "neoplastia_previa"): (
        "MMPastMedicalHistory",
        "previous_neoplasm",
    ),
    ("datos demograficos.csv", "neoplastia_previa_describir"): (
        "MMPastMedicalHistory",
        "previous_neoplasm_details",
    ),
    ("datos demograficos.csv", "neoplastia_previa_fecha_diag"): (
        "MMPastMedicalHistory",
        "previous_neoplasm_date_of_diagnosis",
    ),
    ("datos demograficos.csv", "paciente_referido"): ("MMDiagnosisDetails", "referred"),
    ("datos demograficos.csv", "puntuacion_gah"): ("MMDiagnosisDetails", "gah_score"),
    ("datos demograficos.csv", "puntuacion_icc"): ("MMDiagnosisDetails", "icc_scale"),
    ("datos demograficos.csv", "puntuacion_imwg"): ("MMDiagnosisDetails", "imwg_scale"),
    ("datos demograficos.csv", "sexo"): ("Demographics", "sex"),
    ("datos enfermedad 1.csv", "albumina_1"): ("LabTest", "albumin"),
    ("datos enfermedad 1.csv", "anemia_pres_clinica_1"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 1.csv", "beta_2_microglobulina_1"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 1.csv", "calcio_1"): ("LabTest", "calcium"),
    ("datos enfermedad 1.csv", "celulas_plasmat_medula_1"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 1.csv", "celulasplasmaticascirculantes_1"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 1.csv", "cociente_kappa_lambda_1"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 1.csv", "comentarios_pres_clinica_1"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 1.csv", "creatininaserica_1"): ("LabTest", "creatinine"),
    ("datos enfermedad 1.csv", "cuant_cadena_ligera_kappa_1"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 1.csv", "cuant_cadena_ligera_lambda_1"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 1.csv", "cuant_monoclonal_serico_1"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 1.csv", "cuant_monoclonal_urinario_1"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 1.csv", "describir_serieosea_1"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 1.csv", "diagnostico_1"): ("MMDiagnosisDetails", "diagnosis"),
    ("datos enfermedad 1.csv", "dialisis_1"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 1.csv", "dolores_oseos_pres_clinica_1"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 1.csv", "ecog_1"): ("MMDiagnosisDetails", "ecog"),
    ("datos enfermedad 1.csv", "estado_iss_diagnostico_1"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 1.csv", "estado_riss_diagnostico_1"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_comentarios_estudio_1"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 1.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_1",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_del17p_1"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_del1p_1"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_gan1q_1"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_normal_1"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_otros_1"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_t1114_1"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_t1416_1"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_t414_1"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 1.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_1",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 1.csv", "estudio_citogenetico_estudio_t414_noefectuado_1"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 1.csv", "fecha_diagnostico_1"): (
        "MMDiagnosisDetails",
        "diagnosis_date",
    ),
    ("datos enfermedad 1.csv", "fecha_formular_filtrado_glomerular_1"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 1.csv", "fecha_primera_visita_centro_1"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 1.csv", "fiebre_pres_clinica_1"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 1.csv", "filtradoglomerular_1"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 1.csv", "formulafiltradodescribir_1"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 1.csv", "formulafiltradoglomerular_1"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 1.csv", "fosfatasa_alcalina_1"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 1.csv", "freelite_cuant_1"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 1.csv", "heavylite_cuant_1"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 1.csv", "hemoglobina_1"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 1.csv", "hipercalcemia_pres_clinica_1"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 1.csv", "insuficiencia_renal_pres_clinica_1"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 1.csv", "ldh_1"): ("LabTest", "ldh"),
    ("datos enfermedad 1.csv", "ldhtype_1"): ("LabTest", "ldh_type"),
    ("datos enfermedad 1.csv", "leucocitos_1"): ("LabTest", "leucocytes"),
    ("datos enfermedad 1.csv", "microorg_pc_foco_1"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 1.csv", "microorganismo_pres_clinica_1"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 1.csv", "otras_pruebas_imagen_describir_otros_1"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 1.csv", "otras_pruebas_imagen_otros_1"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 1.csv", "pcr_1"): ("LabTest", "pcr"),
    ("datos enfermedad 1.csv", "peso_diagnostico_1"): ("MMDiagnosisDetails", "weight"),
    ("datos enfermedad 1.csv", "pet_1"): ("Imaging", "pet_scan"),
    ("datos enfermedad 1.csv", "pet_describir_1"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 1.csv", "plaquetas_1"): ("LabTest", "platelets"),
    ("datos enfermedad 1.csv", "plasmocitomas_extramedulares_1"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 1.csv", "probnp_1"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 1.csv", "proteinastotales_1"): ("LabTest", "total_proteins"),
    ("datos enfermedad 1.csv", "proteinuria_1"): ("LabTest", "proteinuria"),
    ("datos enfermedad 1.csv", "proteinuria_g24_1"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 1.csv", "registro_epidemiologico_diag_1"): (
        "MMDiagnosisDetails",
        "epidemiological_register",
    ),
    ("datos enfermedad 1.csv", "resonancia_1"): ("Imaging", "resonance"),
    ("datos enfermedad 1.csv", "resonancia_describir_1"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 1.csv", "serie_osea_prueba_imagen_1"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 1.csv", "subclasificacion_1"): (
        "MMDiagnosisDetails",
        "subclassification",
    ),
    ("datos enfermedad 1.csv", "tac_1"): ("Imaging", "ct_scan"),
    ("datos enfermedad 1.csv", "tac_describir_1"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 1.csv", "talla_diagnostico_1"): ("MMDiagnosisDetails", "height"),
    ("datos enfermedad 1.csv", "tipo_cadena_ligera_1"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 1.csv", "tipo_cadena_pesada_1"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 1.csv", "tipo_cadena_pesada_otros_1"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 1.csv", "tipo_infeccion_pres_clinica_1"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 1.csv", "troponina_1"): ("LabTest", "troponine"),
    ("datos enfermedad 2.csv", "albumina_2"): ("LabTest", "albumin"),
    ("datos enfermedad 2.csv", "anemia_pres_clinica_2"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 2.csv", "beta_2_microglobulina_2"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 2.csv", "calcio_2"): ("LabTest", "calcium"),
    ("datos enfermedad 2.csv", "celulas_plasmat_medula_2"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 2.csv", "celulasplasmaticascirculantes_2"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 2.csv", "cociente_kappa_lambda_2"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 2.csv", "comentarios_pres_clinica_2"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 2.csv", "creatininaserica_2"): ("LabTest", "creatinine"),
    ("datos enfermedad 2.csv", "cuant_cadena_ligera_kappa_2"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 2.csv", "cuant_cadena_ligera_lambda_2"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 2.csv", "cuant_monoclonal_serico_2"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 2.csv", "cuant_monoclonal_urinario_2"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 2.csv", "describir_serieosea_2"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 2.csv", "dialisis_2"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 2.csv", "dolores_oseos_pres_clinica_2"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 2.csv", "estado_iss_diagnostico_2"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 2.csv", "estado_riss_diagnostico_2"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_comentarios_estudio_2"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 2.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_2",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_del17p_2"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_del1p_2"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_gan1q_2"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_normal_2"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_otros_2"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_t1114_2"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_t1416_2"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_t414_2"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 2.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_2",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 2.csv", "estudio_citogenetico_estudio_t414_noefectuado_2"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 2.csv", "fecha_formular_filtrado_glomerular_2"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 2.csv", "fecha_primera_visita_centro_2"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 2.csv", "fiebre_pres_clinica_2"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 2.csv", "filtradoglomerular_2"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 2.csv", "formulafiltradodescribir_2"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 2.csv", "formulafiltradoglomerular_2"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 2.csv", "fosfatasa_alcalina_2"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 2.csv", "freelite_cuant_2"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 2.csv", "heavylite_cuant_2"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 2.csv", "hemoglobina_2"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 2.csv", "hipercalcemia_pres_clinica_2"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 2.csv", "insuficiencia_renal_pres_clinica_2"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 2.csv", "ldh_2"): ("LabTest", "ldh"),
    ("datos enfermedad 2.csv", "ldhtype_2"): ("LabTest", "ldh_type"),
    ("datos enfermedad 2.csv", "leucocitos_2"): ("LabTest", "leucocytes"),
    ("datos enfermedad 2.csv", "microorg_pc_foco_2"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 2.csv", "microorganismo_pres_clinica_2"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 2.csv", "otras_pruebas_imagen_describir_otros_2"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 2.csv", "otras_pruebas_imagen_otros_2"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 2.csv", "pcr_2"): ("LabTest", "pcr"),
    ("datos enfermedad 2.csv", "pet_2"): ("Imaging", "pet_scan"),
    ("datos enfermedad 2.csv", "pet_describir_2"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 2.csv", "plaquetas_2"): ("LabTest", "platelets"),
    ("datos enfermedad 2.csv", "plasmocitomas_extramedulares_2"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 2.csv", "probnp_2"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 2.csv", "proteinastotales_2"): ("LabTest", "total_proteins"),
    ("datos enfermedad 2.csv", "proteinuria_2"): ("LabTest", "proteinuria"),
    ("datos enfermedad 2.csv", "proteinuria_g24_2"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 2.csv", "resonancia_2"): ("Imaging", "resonance"),
    ("datos enfermedad 2.csv", "resonancia_describir_2"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 2.csv", "serie_osea_prueba_imagen_2"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 2.csv", "tac_2"): ("Imaging", "ct_scan"),
    ("datos enfermedad 2.csv", "tac_describir_2"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 2.csv", "tipo_cadena_ligera_2"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 2.csv", "tipo_cadena_pesada_2"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 2.csv", "tipo_cadena_pesada_otros_2"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 2.csv", "tipo_infeccion_pres_clinica_2"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 2.csv", "troponina_2"): ("LabTest", "troponine"),
    ("datos enfermedad 3.csv", "albumina_3"): ("LabTest", "albumin"),
    ("datos enfermedad 3.csv", "anemia_pres_clinica_3"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 3.csv", "beta_2_microglobulina_3"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 3.csv", "calcio_3"): ("LabTest", "calcium"),
    ("datos enfermedad 3.csv", "celulas_plasmat_medula_3"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 3.csv", "celulasplasmaticascirculantes_3"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 3.csv", "cociente_kappa_lambda_3"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 3.csv", "comentarios_pres_clinica_3"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 3.csv", "creatininaserica_3"): ("LabTest", "creatinine"),
    ("datos enfermedad 3.csv", "cuant_cadena_ligera_kappa_3"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 3.csv", "cuant_cadena_ligera_lambda_3"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 3.csv", "cuant_monoclonal_serico_3"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 3.csv", "cuant_monoclonal_urinario_3"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 3.csv", "describir_serieosea_3"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 3.csv", "dialisis_3"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 3.csv", "dolores_oseos_pres_clinica_3"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 3.csv", "estado_iss_diagnostico_3"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 3.csv", "estado_riss_diagnostico_3"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_comentarios_estudio_3"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 3.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_3",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_del17p_3"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_del1p_3"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_gan1q_3"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_normal_3"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_otros_3"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_t1114_3"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_t1416_3"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_t414_3"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 3.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_3",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 3.csv", "estudio_citogenetico_estudio_t414_noefectuado_3"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 3.csv", "fecha_formular_filtrado_glomerular_3"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 3.csv", "fecha_primera_visita_centro_3"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 3.csv", "fiebre_pres_clinica_3"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 3.csv", "filtradoglomerular_3"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 3.csv", "formulafiltradodescribir_3"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 3.csv", "formulafiltradoglomerular_3"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 3.csv", "fosfatasa_alcalina_3"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 3.csv", "freelite_cuant_3"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 3.csv", "heavylite_cuant_3"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 3.csv", "hemoglobina_3"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 3.csv", "hipercalcemia_pres_clinica_3"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 3.csv", "insuficiencia_renal_pres_clinica_3"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 3.csv", "ldh_3"): ("LabTest", "ldh"),
    ("datos enfermedad 3.csv", "ldhtype_3"): ("LabTest", "ldh_type"),
    ("datos enfermedad 3.csv", "leucocitos_3"): ("LabTest", "leucocytes"),
    ("datos enfermedad 3.csv", "microorg_pc_foco_3"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 3.csv", "microorganismo_pres_clinica_3"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 3.csv", "otras_pruebas_imagen_describir_otros_3"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 3.csv", "otras_pruebas_imagen_otros_3"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 3.csv", "pcr_3"): ("LabTest", "pcr"),
    ("datos enfermedad 3.csv", "pet_3"): ("Imaging", "pet_scan"),
    ("datos enfermedad 3.csv", "pet_describir_3"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 3.csv", "plaquetas_3"): ("LabTest", "platelets"),
    ("datos enfermedad 3.csv", "plasmocitomas_extramedulares_3"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 3.csv", "probnp_3"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 3.csv", "proteinastotales_3"): ("LabTest", "total_proteins"),
    ("datos enfermedad 3.csv", "proteinuria_3"): ("LabTest", "proteinuria"),
    ("datos enfermedad 3.csv", "proteinuria_g24_3"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 3.csv", "resonancia_3"): ("Imaging", "resonance"),
    ("datos enfermedad 3.csv", "resonancia_describir_3"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 3.csv", "serie_osea_prueba_imagen_3"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 3.csv", "tac_3"): ("Imaging", "ct_scan"),
    ("datos enfermedad 3.csv", "tac_describir_3"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 3.csv", "tipo_cadena_ligera_3"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 3.csv", "tipo_cadena_pesada_3"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 3.csv", "tipo_cadena_pesada_otros_3"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 3.csv", "tipo_infeccion_pres_clinica_3"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 3.csv", "troponina_3"): ("LabTest", "troponine"),
    ("datos enfermedad 4.csv", "albumina_4"): ("LabTest", "albumin"),
    ("datos enfermedad 4.csv", "anemia_pres_clinica_4"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 4.csv", "beta_2_microglobulina_4"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 4.csv", "calcio_4"): ("LabTest", "calcium"),
    ("datos enfermedad 4.csv", "celulas_plasmat_medula_4"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 4.csv", "celulasplasmaticascirculantes_4"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 4.csv", "cociente_kappa_lambda_4"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 4.csv", "comentarios_pres_clinica_4"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 4.csv", "creatininaserica_4"): ("LabTest", "creatinine"),
    ("datos enfermedad 4.csv", "cuant_cadena_ligera_kappa_4"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 4.csv", "cuant_cadena_ligera_lambda_4"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 4.csv", "cuant_monoclonal_serico_4"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 4.csv", "cuant_monoclonal_urinario_4"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 4.csv", "describir_serieosea_4"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 4.csv", "dialisis_4"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 4.csv", "dolores_oseos_pres_clinica_4"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 4.csv", "estado_iss_diagnostico_4"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 4.csv", "estado_riss_diagnostico_4"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_comentarios_estudio_4"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 4.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_4",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_del17p_4"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_del1p_4"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_gan1q_4"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_normal_4"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_otros_4"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_t1114_4"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_t1416_4"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_t414_4"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 4.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_4",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 4.csv", "estudio_citogenetico_estudio_t414_noefectuado_4"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 4.csv", "fecha_formular_filtrado_glomerular_4"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 4.csv", "fecha_primera_visita_centro_4"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 4.csv", "fiebre_pres_clinica_4"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 4.csv", "filtradoglomerular_4"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 4.csv", "formulafiltradodescribir_4"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 4.csv", "formulafiltradoglomerular_4"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 4.csv", "fosfatasa_alcalina_4"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 4.csv", "freelite_cuant_4"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 4.csv", "heavylite_cuant_4"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 4.csv", "hemoglobina_4"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 4.csv", "hipercalcemia_pres_clinica_4"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 4.csv", "insuficiencia_renal_pres_clinica_4"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 4.csv", "ldh_4"): ("LabTest", "ldh"),
    ("datos enfermedad 4.csv", "ldhtype_4"): ("LabTest", "ldh_type"),
    ("datos enfermedad 4.csv", "leucocitos_4"): ("LabTest", "leucocytes"),
    ("datos enfermedad 4.csv", "microorg_pc_foco_4"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 4.csv", "microorganismo_pres_clinica_4"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 4.csv", "otras_pruebas_imagen_describir_otros_4"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 4.csv", "otras_pruebas_imagen_otros_4"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 4.csv", "pcr_4"): ("LabTest", "pcr"),
    ("datos enfermedad 4.csv", "pet_4"): ("Imaging", "pet_scan"),
    ("datos enfermedad 4.csv", "pet_describir_4"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 4.csv", "plaquetas_4"): ("LabTest", "platelets"),
    ("datos enfermedad 4.csv", "plasmocitomas_extramedulares_4"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 4.csv", "probnp_4"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 4.csv", "proteinastotales_4"): ("LabTest", "total_proteins"),
    ("datos enfermedad 4.csv", "proteinuria_4"): ("LabTest", "proteinuria"),
    ("datos enfermedad 4.csv", "proteinuria_g24_4"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 4.csv", "resonancia_describir_4"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 4.csv", "serie_osea_prueba_imagen_4"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 4.csv", "tac_4"): ("Imaging", "ct_scan"),
    ("datos enfermedad 4.csv", "tac_describir_4"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 4.csv", "tipo_cadena_ligera_4"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 4.csv", "tipo_cadena_pesada_4"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 4.csv", "tipo_cadena_pesada_otros_4"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 4.csv", "tipo_infeccion_pres_clinica_4"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 4.csv", "troponina_4"): ("LabTest", "troponine"),
    ("datos enfermedad 5.csv", "albumina_5"): ("LabTest", "albumin"),
    ("datos enfermedad 5.csv", "anemia_pres_clinica_5"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 5.csv", "beta_2_microglobulina_5"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 5.csv", "calcio_5"): ("LabTest", "calcium"),
    ("datos enfermedad 5.csv", "celulas_plasmat_medula_5"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 5.csv", "celulasplasmaticascirculantes_5"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 5.csv", "cociente_kappa_lambda_5"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 5.csv", "comentarios_pres_clinica_5"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 5.csv", "creatininaserica_5"): ("LabTest", "creatinine"),
    ("datos enfermedad 5.csv", "cuant_cadena_ligera_kappa_5"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 5.csv", "cuant_cadena_ligera_lambda_5"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 5.csv", "cuant_monoclonal_serico_5"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 5.csv", "cuant_monoclonal_urinario_5"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 5.csv", "describir_serieosea_5"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 5.csv", "dialisis_5"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 5.csv", "dolores_oseos_pres_clinica_5"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 5.csv", "estado_iss_diagnostico_5"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 5.csv", "estado_riss_diagnostico_5"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_comentarios_estudio_5"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 5.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_5",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_del17p_5"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_del1p_5"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_gan1q_5"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_normal_5"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_otros_5"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_t1114_5"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_t1416_5"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_t414_5"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 5.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_5",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 5.csv", "estudio_citogenetico_estudio_t414_noefectuado_5"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 5.csv", "fecha_formular_filtrado_glomerular_5"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 5.csv", "fecha_primera_visita_centro_5"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 5.csv", "fiebre_pres_clinica_5"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 5.csv", "filtradoglomerular_5"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 5.csv", "formulafiltradodescribir_5"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 5.csv", "formulafiltradoglomerular_5"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 5.csv", "fosfatasa_alcalina_5"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 5.csv", "freelite_cuant_5"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 5.csv", "heavylite_cuant_5"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 5.csv", "hemoglobina_5"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 5.csv", "hipercalcemia_pres_clinica_5"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 5.csv", "insuficiencia_renal_pres_clinica_5"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 5.csv", "ldh_5"): ("LabTest", "ldh"),
    ("datos enfermedad 5.csv", "ldhtype_5"): ("LabTest", "ldh_type"),
    ("datos enfermedad 5.csv", "leucocitos_5"): ("LabTest", "leucocytes"),
    ("datos enfermedad 5.csv", "microorg_pc_foco_5"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 5.csv", "microorganismo_pres_clinica_5"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 5.csv", "otras_pruebas_imagen_describir_otros_5"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 5.csv", "otras_pruebas_imagen_otros_5"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 5.csv", "pcr_5"): ("LabTest", "pcr"),
    ("datos enfermedad 5.csv", "pet_5"): ("Imaging", "pet_scan"),
    ("datos enfermedad 5.csv", "pet_describir_5"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 5.csv", "plaquetas_5"): ("LabTest", "platelets"),
    ("datos enfermedad 5.csv", "plasmocitomas_extramedulares_5"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 5.csv", "probnp_5"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 5.csv", "proteinastotales_5"): ("LabTest", "total_proteins"),
    ("datos enfermedad 5.csv", "proteinuria_5"): ("LabTest", "proteinuria"),
    ("datos enfermedad 5.csv", "proteinuria_g24_5"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 5.csv", "resonancia_5"): ("Imaging", "resonance"),
    ("datos enfermedad 5.csv", "resonancia_describir_5"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 5.csv", "serie_osea_prueba_imagen_5"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 5.csv", "tac_5"): ("Imaging", "ct_scan"),
    ("datos enfermedad 5.csv", "tac_describir_5"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 5.csv", "tipo_cadena_ligera_5"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 5.csv", "tipo_cadena_pesada_5"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 5.csv", "tipo_cadena_pesada_otros_5"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 5.csv", "tipo_infeccion_pres_clinica_5"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 5.csv", "troponina_5"): ("LabTest", "troponine"),
    ("datos enfermedad 6.csv", "albumina_6"): ("LabTest", "albumin"),
    ("datos enfermedad 6.csv", "anemia_pres_clinica_6"): (
        "ClinicalPresentation",
        "anemia",
    ),
    ("datos enfermedad 6.csv", "beta_2_microglobulina_6"): (
        "LabTest",
        "beta_2_microglobulin",
    ),
    ("datos enfermedad 6.csv", "calcio_6"): ("LabTest", "calcium"),
    ("datos enfermedad 6.csv", "celulas_plasmat_medula_6"): (
        "MProteinMesurements",
        "plasma_cells_in_bone_marrow",
    ),
    ("datos enfermedad 6.csv", "celulasplasmaticascirculantes_6"): (
        "LabTest",
        "circulating_plasma_cells",
    ),
    ("datos enfermedad 6.csv", "cociente_kappa_lambda_6"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("datos enfermedad 6.csv", "comentarios_pres_clinica_6"): (
        "ClinicalPresentation",
        "details",
    ),
    ("datos enfermedad 6.csv", "creatininaserica_6"): ("LabTest", "creatinine"),
    ("datos enfermedad 6.csv", "cuant_cadena_ligera_kappa_6"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("datos enfermedad 6.csv", "cuant_cadena_ligera_lambda_6"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("datos enfermedad 6.csv", "cuant_monoclonal_serico_6"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("datos enfermedad 6.csv", "cuant_monoclonal_urinario_6"): (
        "MProteinMesurements",
        "urinary_monoclonal_count",
    ),
    ("datos enfermedad 6.csv", "describir_serieosea_6"): (
        "Imaging",
        "bone_series_description",
    ),
    ("datos enfermedad 6.csv", "dialisis_6"): ("ClinicalPresentation", "dialysis"),
    ("datos enfermedad 6.csv", "dolores_oseos_pres_clinica_6"): (
        "ClinicalPresentation",
        "bone_pain",
    ),
    ("datos enfermedad 6.csv", "estado_iss_diagnostico_6"): (
        "ClinicalPresentation",
        "iss",
    ),
    ("datos enfermedad 6.csv", "estado_riss_diagnostico_6"): (
        "ClinicalPresentation",
        "riss",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_comentarios_estudio_6"): (
        "Cytogenetics",
        "details",
    ),
    (
        "datos enfermedad 6.csv",
        "estudio_citogenetico_estudio_alteracionescromosoma1_6",
    ): ("Cytogenetics", "chromosome_alterations"),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_del17p_6"): (
        "Cytogenetics",
        "del_17p",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_del1p_6"): (
        "Cytogenetics",
        "del1p",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_gan1q_6"): (
        "Cytogenetics",
        "gan1q",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_normal_6"): (
        "Cytogenetics",
        "normal_study",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_otros_6"): (
        "Cytogenetics",
        "other_study",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_t1114_6"): (
        "Cytogenetics",
        "t11_14",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_t1416_6"): (
        "Cytogenetics",
        "t4_14_16",
    ),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_t414_6"): (
        "Cytogenetics",
        "t4_14",
    ),
    (
        "datos enfermedad 6.csv",
        "estudio_citogenetico_estudio_t414_cariotipohiperploide_6",
    ): ("Cytogenetics", "t4_14_haploid_karyotype"),
    ("datos enfermedad 6.csv", "estudio_citogenetico_estudio_t414_noefectuado_6"): (
        "Cytogenetics",
        "t4_14_not_effected",
    ),
    ("datos enfermedad 6.csv", "fecha_formular_filtrado_glomerular_6"): (
        "LabTest",
        "glomerular_filtration_formula_date",
    ),
    ("datos enfermedad 6.csv", "fecha_primera_visita_centro_6"): (
        "MMDiagnosisDetails",
        "date_of_first_centre_visit",
    ),
    ("datos enfermedad 6.csv", "fiebre_pres_clinica_6"): (
        "ClinicalPresentation",
        "fever",
    ),
    ("datos enfermedad 6.csv", "filtradoglomerular_6"): (
        "LabTest",
        "glomerular_filtration",
    ),
    ("datos enfermedad 6.csv", "formulafiltradodescribir_6"): (
        "LabTest",
        "filter_formula_description",
    ),
    ("datos enfermedad 6.csv", "formulafiltradoglomerular_6"): (
        "LabTest",
        "glomerular_filtration_formula",
    ),
    ("datos enfermedad 6.csv", "fosfatasa_alcalina_6"): (
        "LabTest",
        "alkaline_phosphatase",
    ),
    ("datos enfermedad 6.csv", "freelite_cuant_6"): (
        "MProteinMesurements",
        "freelite_count",
    ),
    ("datos enfermedad 6.csv", "heavylite_cuant_6"): (
        "MProteinMesurements",
        "heavylite_count",
    ),
    ("datos enfermedad 6.csv", "hemoglobina_6"): ("LabTest", "hemoglobin"),
    ("datos enfermedad 6.csv", "hipercalcemia_pres_clinica_6"): (
        "ClinicalPresentation",
        "hypercalcemia",
    ),
    ("datos enfermedad 6.csv", "insuficiencia_renal_pres_clinica_6"): (
        "ClinicalPresentation",
        "renal_failure",
    ),
    ("datos enfermedad 6.csv", "ldh_6"): ("LabTest", "ldh"),
    ("datos enfermedad 6.csv", "ldhtype_6"): ("LabTest", "ldh_type"),
    ("datos enfermedad 6.csv", "leucocitos_6"): ("LabTest", "leucocytes"),
    ("datos enfermedad 6.csv", "microorg_pc_foco_6"): (
        "ClinicalPresentation",
        "microorganism_source",
    ),
    ("datos enfermedad 6.csv", "microorganismo_pres_clinica_6"): (
        "ClinicalPresentation",
        "microorganism",
    ),
    ("datos enfermedad 6.csv", "otras_pruebas_imagen_describir_otros_6"): (
        "Imaging",
        "other_imaging_test_description",
    ),
    ("datos enfermedad 6.csv", "otras_pruebas_imagen_otros_6"): (
        "Imaging",
        "other_imaging_test",
    ),
    ("datos enfermedad 6.csv", "pcr_6"): ("LabTest", "pcr"),
    ("datos enfermedad 6.csv", "pet_6"): ("Imaging", "pet_scan"),
    ("datos enfermedad 6.csv", "pet_describir_6"): ("Imaging", "pet_scan_description"),
    ("datos enfermedad 6.csv", "plaquetas_6"): ("LabTest", "platelets"),
    ("datos enfermedad 6.csv", "plasmocitomas_extramedulares_6"): (
        "ClinicalPresentation",
        "extramedullary_plasmacytomas",
    ),
    ("datos enfermedad 6.csv", "probnp_6"): ("LabTest", "nt_pro_bnp"),
    ("datos enfermedad 6.csv", "proteinastotales_6"): ("LabTest", "total_proteins"),
    ("datos enfermedad 6.csv", "proteinuria_6"): ("LabTest", "proteinuria"),
    ("datos enfermedad 6.csv", "proteinuria_g24_6"): ("LabTest", "proteinuria_g24"),
    ("datos enfermedad 6.csv", "resonancia_6"): ("Imaging", "resonance"),
    ("datos enfermedad 6.csv", "resonancia_describir_6"): (
        "Imaging",
        "resonance_description",
    ),
    ("datos enfermedad 6.csv", "serie_osea_prueba_imagen_6"): (
        "Imaging",
        "bone_series_test_image",
    ),
    ("datos enfermedad 6.csv", "tac_6"): ("Imaging", "ct_scan"),
    ("datos enfermedad 6.csv", "tac_describir_6"): ("Imaging", "ct_scan_description"),
    ("datos enfermedad 6.csv", "tipo_cadena_ligera_6"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("datos enfermedad 6.csv", "tipo_cadena_pesada_6"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("datos enfermedad 6.csv", "tipo_cadena_pesada_otros_6"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("datos enfermedad 6.csv", "tipo_infeccion_pres_clinica_6"): (
        "ClinicalPresentation",
        "infection_type",
    ),
    ("datos enfermedad 6.csv", "troponina_6"): ("LabTest", "troponine"),
    ("situacion actual.csv", "causa_muerte"): ("MMPatientStatus", "cause_of_death"),
    ("situacion actual.csv", "causa_muerte_otros"): (
        "MMPatientStatus",
        "cause_of_death_other",
    ),
    ("situacion actual.csv", "comentarios_discontinacion"): (
        "MMPatientStatus",
        "comments",
    ),
<<<<<<< HEAD
    ("tratamiento 1.csv", "acondicionamiento_alotph_1"): ("SCT", "alotph_conditioning"),
=======
>>>>>>> zaragosa-heroku
    ("tratamiento 1.csv", "acondicionamiento_atsp_1"): ("SCT", "atsp_conditioning"),
    ("tratamiento 1.csv", "candidato_transplante_1"): (
        "MMStemCellTransplantEligibility",
        "eligible_for_stem_cell_transplant",
    ),
    ("tratamiento 1.csv", "comentarios_mantenimiento_1"): ("MMRegimen", "comments"),
    ("tratamiento 1.csv", "esquema_consolidacion_1"): ("MMRegimen", "regimen"),
    ("tratamiento 1.csv", "esquema_consolidacion_otros_1"): (
        "MMRegimen",
        "regimen_details",
    ),
    ("tratamiento 1.csv", "esquema_induccion_1"): ("MMRegimen", "regimen"),
    ("tratamiento 1.csv", "esquema_induccion_describir_1"): ("MMRegimen", "comments"),
    ("tratamiento 1.csv", "esquema_mantenimiento_1"): ("MMRegimen", "regimen"),
    ("tratamiento 1.csv", "esquema_mantenimiento_describir_1"): (
        "MMRegimen",
        "regimen_details",
    ),
    ("tratamiento 1.csv", "estatus_trasplante_tandem_atsp_1"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 1.csv", "fecha_progresion_induccion_1"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 1.csv", "fiebre_comentarios_induccion_1"): ("Comorbidity", "details"),
    ("tratamiento 1.csv", "fiebre_induccion_1"): ("Comorbidity", "condition"),
    ("tratamiento 1.csv", "fuente_alopth_1"): ("SCT", "alotph_source"),
    ("tratamiento 1.csv", "hemorragias_comentarios_induccion_1"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 1.csv", "hemorragias_induccion_1"): ("Comorbidity", "condition"),
    ("tratamiento 1.csv", "indicar_bifosfonato_induccion_1"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 1.csv", "induccion_motivo_discontinuacion_1"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 1.csv", "induccion_motivo_discontinuacion_describir_1"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 1.csv", "insuficiencia_renal_comentarios_induccion_1"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 1.csv", "insuficiencia_renal_induccion_1"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 1.csv", "mantenimiento_progresion_fecha_1"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 1.csv", "manteniniemto_motivo_discontinuacion_1"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 1.csv", "manteniniemto_motivo_discontinuacion_describir_1"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_alotph_1"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_alotph_fecha_1"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_atsp_1"): ("MMResponse", "negative_mrd"),
    ("tratamiento 1.csv", "negativizacion_emr_atsp_fecha_1"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_consolidacion_1"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_consolidacion_fecha_1"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_induccion_1"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_induccion_fecha_1"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_mantenimiento_1"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 1.csv", "negativizacion_emr_mantenimiento_fecha_1"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 1.csv", "neuropatia_comentarios_induccion_1"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 1.csv", "neuropatia_induccion_1"): ("Comorbidity", "condition"),
    ("tratamiento 1.csv", "numero_ciclos_1"): ("MMRegimen", "nbCycles"),
    ("tratamiento 1.csv", "numero_ciclos_enfermedad_osea_induccion_1"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 1.csv", "numero_ciclos_induccion_1"): ("MMRegimen", "nbCycles"),
    ("tratamiento 1.csv", "otras_toxicidades_comentarios_induccion_1"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 1.csv", "otras_toxicidades_especificar_induccion_1"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 1.csv", "otras_toxicidades_induccion_1"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 1.csv", "radioterapia_induccion_fecha_fin_1"): (
        "RadiotherapyInduction",
        "end_date",
    ),
    ("tratamiento 1.csv", "radioterapia_induccion_fecha_inicio_1"): (
        "RadiotherapyInduction",
        "start_date",
    ),
    ("tratamiento 1.csv", "resp_despues_trasplante_atsp_fecha_1"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 1.csv", "respuesta_despues_consolidacion_1"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 1.csv", "respuesta_despues_consolidacion_fecha_1"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 1.csv", "respuesta_despues_induccion_1"): ("MMResponse", "response"),
    ("tratamiento 1.csv", "respuesta_despues_induccion_fecha_1"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 1.csv", "respuesta_despues_mantenimiento_1"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 1.csv", "respuesta_despues_mantenimiento_fecha_1"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 1.csv", "respuesta_despues_trasplante_alotph_1"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 1.csv", "respuesta_despues_trasplante_atsp_1"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 1.csv", "tecnica_emr2_1"): ("MMResponse", "mrd_technique"),
    ("tratamiento 1.csv", "tecnica_emr_alotph_1"): ("MMResponse", "mrd_technique"),
    ("tratamiento 1.csv", "tecnica_emr_atsp_1"): ("MMResponse", "mrd_technique"),
    ("tratamiento 1.csv", "tecnica_emr_consolidacion_1"): (
        "MMResponse",
        "mrd_technique",
    ),
    ("tratamiento 1.csv", "tecnica_emr_induccion_1"): ("MMResponse", "mrd_technique"),
    ("tratamiento 1.csv", "tipo_infeccion_comentarios_induccion_1"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 1.csv", "tipo_infeccion_documentada_foco_induccion_1"): (
        "Comorbidity",
        "infection_source",
    ),
    ("tratamiento 1.csv", "tipo_infeccion_documentada_microorganismo_induccion_1"): (
        "Comorbidity",
        "type_of_microorganism_infection",
    ),
    ("tratamiento 1.csv", "tipo_infeccion_induccion_1"): ("Comorbidity", "condition"),
    ("tratamiento 1.csv", "tipo_trasplante_alotph_1"): (
        "SCT",
        "type_of_alotph_transplant",
    ),
    (
        "tratamiento 1.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_1",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 1.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_1"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 1.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_1",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 1.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_1"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 1.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_1",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 1.csv", "trasplante_alogenico_alotph_fecha_1"): ("SCT", "sct_date"),
    ("tratamiento 1.csv", "trasplante_autologo_atsp_fecha_1"): ("SCT", "sct_date"),
    ("tratamiento 1.csv", "trasplante_numero_de_celulas_infundias_1"): (
        "SCT",
        "number_of_cells_infused",
    ),
    ("tratamiento 1.csv", "tratamiento_consolidacion_fecha_fin_1"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 1.csv", "tratamiento_consolidacion_fecha_inicio_1"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 1.csv", "tratamiento_enfermedad_osea_fecha_fin_induccion_1"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 1.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_1"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 1.csv", "tratamiento_induccion_fecha_fin_1"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 1.csv", "tratamiento_induccion_fecha_inicio_1"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 1.csv", "tratamiento_mantenimiento_fecha_fin_1"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 1.csv", "tratamiento_mantenimiento_fecha_inicio_1"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 1.csv", "tratamiento_mantenimiento_numero_ciclos_1"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 1.csv", "vertebroplastia_cifoplastia_comentarios_induccion_1"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 1.csv", "vertebroplastia_cifoplastia_fecha_induccion_1"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
<<<<<<< HEAD
    ("tratamiento 2.csv", "acondicionamiento_alotph_2"): ("SCT", "alotph_conditioning"),
=======
>>>>>>> zaragosa-heroku
    ("tratamiento 2.csv", "acondicionamiento_atsp_2"): ("SCT", "atsp_conditioning"),
    ("tratamiento 2.csv", "candidato_transplante_2"): (
        "MMStemCellTransplantEligibility",
        "eligible_for_stem_cell_transplant",
    ),
    ("tratamiento 2.csv", "cociente_kappa_lambda_2"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("tratamiento 2.csv", "comentarios_mantenimiento_2"): ("MMRegimen", "comments"),
    ("tratamiento 2.csv", "cuant_cadena_ligera_kappa_2"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("tratamiento 2.csv", "cuant_cadena_ligera_lambda_2"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("tratamiento 2.csv", "cuant_monoclonal_serico_2"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("tratamiento 2.csv", "esquema_consolidacion_2"): ("MMRegimen", "regimen"),
    ("tratamiento 2.csv", "esquema_consolidacion_otros_2"): (
        "MMRegimen",
        "regimen_details",
    ),
    ("tratamiento 2.csv", "esquema_induccion_2"): ("MMRegimen", "regimen"),
    ("tratamiento 2.csv", "esquema_induccion_describir_2"): ("MMRegimen", "comments"),
    ("tratamiento 2.csv", "esquema_mantenimiento_2"): ("MMRegimen", "regimen"),
    ("tratamiento 2.csv", "esquema_mantenimiento_describir_2"): (
        "MMRegimen",
        "comments",
    ),
    ("tratamiento 2.csv", "esquema_tratamiento_2"): ("MMRegimen", "regimen"),
    ("tratamiento 2.csv", "esquema_tratamiento_otros_2"): ("MMRegimen", "regimen"),
    ("tratamiento 2.csv", "estatus_trasplante_tandem_atsp_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "fecha_progresion_induccion_2"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 2.csv", "fiebre_comentarios_induccion_2"): ("Comorbidity", "details"),
    ("tratamiento 2.csv", "fiebre_comentarios_toxicidades_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "fiebre_induccion_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "fiebre_toxicidades_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "fuente_alopth_2"): ("SCT", "alotph_source"),
    ("tratamiento 2.csv", "hemorragias_comentarios_induccion_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "hemorragias_comentarios_toxicidades_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "hemorragias_induccion_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "hemorragias_toxicidades_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "indicar_bifosfonato_induccion_2"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 2.csv", "induccion_motivo_discontinuacion_2"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 2.csv", "induccion_motivo_discontinuacion_describir_2"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 2.csv", "insuficiencia_renal_comentarios_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "insuficiencia_renal_induccion_2"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 2.csv", "insuficiencia_renal_toxicidades_2"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 2.csv", "mantenimiento_progresion_fecha_2"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 2.csv", "manteniniemto_motivo_discontinuacion_2"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 2.csv", "manteniniemto_motivo_discontinuacion_describir_2"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 2.csv", "motivo_inicio_tratamiento_2"): ("MMRegimen", "start_reason"),
    ("tratamiento 2.csv", "negativizacion_emr_alotph_2"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_alotph_fecha_2"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_atsp_2"): ("MMResponse", "negative_mrd"),
    ("tratamiento 2.csv", "negativizacion_emr_atsp_fecha_2"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_consolidacion_2"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_consolidacion_fecha_2"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_induccion_2"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_induccion_fecha_2"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_mantenimiento_2"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 2.csv", "negativizacion_emr_mantenimiento_fecha_2"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 2.csv", "neuropatia_comentarios_induccion_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "neuropatia_comentarios_toxicidades_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "neuropatia_induccion_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "neuropatia_toxicidades_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "numero_ciclos_2"): ("MMRegimen", "nbCycles"),
    ("tratamiento 2.csv", "numero_ciclos_enfermedad_osea_induccion_2"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 2.csv", "numero_ciclos_induccion_2"): ("MMRegimen", "nbCycles"),
    ("tratamiento 2.csv", "otras_toxicidades_comentarios_induccion_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "otras_toxicidades_comentarios_toxicidades_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "otras_toxicidades_especificar_induccion_2"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 2.csv", "otras_toxicidades_especificar_toxicidades_2"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 2.csv", "otras_toxicidades_induccion_2"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 2.csv", "otras_toxicidades_toxicidades_2"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 2.csv", "radioterapia_induccion_fecha_fin_2"): (
        "RadiotherapyInduction",
        "end_date",
    ),
    ("tratamiento 2.csv", "radioterapia_induccion_fecha_inicio_2"): (
        "RadiotherapyInduction",
        "start_date",
    ),
    ("tratamiento 2.csv", "recaida_motivo_discontinuacion_2"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 2.csv", "recaida_motivo_discontinuacion_describir_2"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 2.csv", "resp_despues_trasplante_atsp_fecha_2"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 2.csv", "respuesta_despues_consolidacion_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "respuesta_despues_consolidacion_fecha_2"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 2.csv", "respuesta_despues_induccion_2"): ("MMResponse", "response"),
    ("tratamiento 2.csv", "respuesta_despues_induccion_fecha_2"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 2.csv", "respuesta_despues_mantenimiento_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "respuesta_despues_mantenimiento_fecha_2"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 2.csv", "respuesta_despues_trasplante_alotph_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "respuesta_despues_trasplante_atsp_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "tecnica_emr2_2"): ("MMResponse", "mrd_technique"),
    ("tratamiento 2.csv", "tipo_cadena_ligera_2"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("tratamiento 2.csv", "tipo_cadena_pesada_2"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("tratamiento 2.csv", "tipo_cadena_pesada_otros_2"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("tratamiento 2.csv", "tipo_infeccion_comentarios_induccion_2"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 2.csv", "tipo_infeccion_documentada_foco_induccion_2"): (
        "Comorbidity",
        "infection_source",
    ),
    ("tratamiento 2.csv", "tipo_infeccion_documentada_microorganismo_induccion_2"): (
        "Comorbidity",
        "type_of_microorganism_infection",
    ),
    ("tratamiento 2.csv", "tipo_infeccion_induccion_2"): ("Comorbidity", "condition"),
    ("tratamiento 2.csv", "tipo_trasplante_alotph_2"): (
        "SCT",
        "type_of_alotph_transplant",
    ),
    (
        "tratamiento 2.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_2",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 2.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_2"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 2.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_2",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 2.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_2"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 2.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_2",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 2.csv", "trasplante_alogenico_alotph_fecha_2"): ("SCT", "sct_date"),
    ("tratamiento 2.csv", "trasplante_autologo_atsp_fecha_2"): ("SCT", "sct_date"),
    ("tratamiento 2.csv", "trasplante_numero_de_celulas_infundias_2"): (
        "SCT",
        "number_of_cells_infused",
    ),
    ("tratamiento 2.csv", "trasplante_tandem_atsp_2"): ("SCT", "tandem_astp"),
    ("tratamiento 2.csv", "tratamiento_comentarios_2"): ("MMRegimen", "comments"),
    ("tratamiento 2.csv", "tratamiento_consolidacion_fecha_fin_2"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 2.csv", "tratamiento_consolidacion_fecha_inicio_2"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 2.csv", "tratamiento_enfermedad_osea_fecha_ifin_induccion_2"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 2.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_2"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 2.csv", "tratamiento_induccion_fecha_fin_2"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 2.csv", "tratamiento_induccion_fecha_inicio_2"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 2.csv", "tratamiento_mantenimiento_fecha_fin_2"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 2.csv", "tratamiento_mantenimiento_fecha_inicio_2"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 2.csv", "tratamiento_mantenimiento_numero_ciclos_2"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_fecha_fin_2"): ("MMRegimen", "end_date"),
    ("tratamiento 2.csv", "tratamiento_recaida_fecha_inicio_2"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_negativizacion_emr_2"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_numero_ciclos__2"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_progresion_fecha_2"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_respuesta_2"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 2.csv", "tratamiento_recaida_respuesta_fecha_2"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 2.csv", "vertebroplastia_cifoplastia_comentarios_induccion_2"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 2.csv", "vertebroplastia_cifoplastia_fecha_induccion_2"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
    ("tratamiento 3.csv", "cociente_kappa_lambda_3"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("tratamiento 3.csv", "comentarios_mantenimiento_3"): ("MMRegimen", "comments"),
    ("tratamiento 3.csv", "cuant_cadena_ligera_kappa_3"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("tratamiento 3.csv", "cuant_cadena_ligera_lambda_3"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("tratamiento 3.csv", "cuant_monoclonal_serico_3"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("tratamiento 3.csv", "esquema_mantenimiento_3"): ("MMRegimen", "regimen"),
    ("tratamiento 3.csv", "esquema_mantenimiento_describir_3"): (
        "MMRegimen",
        "comments",
    ),
    ("tratamiento 3.csv", "esquema_tratamiento_3"): ("MMRegimen", "regimen"),
    ("tratamiento 3.csv", "esquema_tratamiento_otros_3"): ("MMRegimen", "regimen"),
    ("tratamiento 3.csv", "fiebre_comentarios_toxicidades_3"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 3.csv", "fiebre_toxicidades_3"): ("Comorbidity", "condition"),
    ("tratamiento 3.csv", "hemorragias_comentarios_toxicidades_3"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 3.csv", "hemorragias_toxicidades_3"): ("Comorbidity", "condition"),
    ("tratamiento 3.csv", "indicar_bifosfonato_induccion_3"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 3.csv", "insuficiencia_renal_comentarios_3"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 3.csv", "insuficiencia_renal_toxicidades_3"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 3.csv", "mantenimiento_progresion_fecha_3"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 3.csv", "manteniniemto_motivo_discontinuacion_3"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 3.csv", "manteniniemto_motivo_discontinuacion_describir_3"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 3.csv", "motivo_inicio_tratamiento_3"): ("MMRegimen", "start_reason"),
    ("tratamiento 3.csv", "negativizacion_emr_mantenimiento_3"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 3.csv", "negativizacion_emr_mantenimiento_fecha_3"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 3.csv", "neuropatia_comentarios_toxicidades_3"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 3.csv", "neuropatia_toxicidades_3"): ("Comorbidity", "condition"),
    ("tratamiento 3.csv", "numero_ciclos_enfermedad_osea_induccion_3"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 3.csv", "otras_toxicidades_comentarios_toxicidades_3"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 3.csv", "otras_toxicidades_especificar_toxicidades_3"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 3.csv", "otras_toxicidades_toxicidades_3"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 3.csv", "recaida_motivo_discontinuacion_3"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 3.csv", "recaida_motivo_discontinuacion_describir_3"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 3.csv", "respuesta_despues_mantenimiento_3"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 3.csv", "respuesta_despues_mantenimiento_fecha_3"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 3.csv", "tecnica_emr2_3"): ("MMResponse", "mrd_technique"),
    ("tratamiento 3.csv", "tipo_cadena_ligera_3"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("tratamiento 3.csv", "tipo_cadena_pesada_3"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("tratamiento 3.csv", "tipo_cadena_pesada_otros_3"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    (
        "tratamiento 3.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_3",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 3.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_3"): (
        "BoneDisease",
        "treatment_type",
    ),
    ("tratamiento 3.csv", "tipo_tratamiento_enfermedad_osea_describir_induccion_3"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 3.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_3",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 3.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_3"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 3.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_3",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 3.csv", "tratamiento_comentarios_3"): ("MMRegimen", "comments"),
    ("tratamiento 3.csv", "tratamiento_enfermedad_osea_fecha_ifin_induccion_3"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 3.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_3"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 3.csv", "tratamiento_mantenimiento_fecha_fin_3"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 3.csv", "tratamiento_mantenimiento_fecha_inicio_3"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 3.csv", "tratamiento_mantenimiento_numero_ciclos_3"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_fecha_fin_3"): ("MMRegimen", "end_date"),
    ("tratamiento 3.csv", "tratamiento_recaida_fecha_inicio_3"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_negativizacion_emr_3"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_numero_ciclos_3"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_progresion_fecha_3"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_respuesta_3"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 3.csv", "tratamiento_recaida_respuesta_fecha_3"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 3.csv", "vertebroplastia_cifoplastia_comentarios_induccion_3"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 3.csv", "vertebroplastia_cifoplastia_fecha_induccion_3"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
    ("tratamiento 4.csv", "cociente_kappa_lambda_4"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("tratamiento 4.csv", "comentarios_mantenimiento_4"): ("MMRegimen", "comments"),
    ("tratamiento 4.csv", "cuant_cadena_ligera_kappa_4"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("tratamiento 4.csv", "cuant_cadena_ligera_lambda_4"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("tratamiento 4.csv", "cuant_monoclonal_serico_4"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("tratamiento 4.csv", "esquema_mantenimiento_4"): ("MMRegimen", "regimen"),
    ("tratamiento 4.csv", "esquema_mantenimiento_describir_4"): (
        "MMRegimen",
        "comments",
    ),
    ("tratamiento 4.csv", "esquema_tratamiento_4"): ("MMRegimen", "regimen"),
    ("tratamiento 4.csv", "esquema_tratamiento_otros_4"): ("MMRegimen", "regimen"),
    ("tratamiento 4.csv", "fiebre_comentarios_toxicidades_4"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "fiebre_toxicidades_4"): ("Comorbidity", "condition"),
    ("tratamiento 4.csv", "hemorragias_comentarios_toxicidades_4"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "hemorragias_toxicidades_4"): ("Comorbidity", "condition"),
    ("tratamiento 4.csv", "indicar_bifosfonato_induccion_4"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 4.csv", "insuficiencia_renal_comentarios_4"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "insuficiencia_renal_toxicidades_4"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 4.csv", "mantenimiento_progresion_fecha_4"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 4.csv", "manteniniemto_motivo_discontinuacion_4"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 4.csv", "manteniniemto_motivo_discontinuacion_describir_4"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 4.csv", "motivo_inicio_tratamiento_4"): ("MMRegimen", "start_reason"),
    ("tratamiento 4.csv", "negativizacion_emr_mantenimiento_4"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 4.csv", "negativizacion_emr_mantenimiento_fecha_4"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 4.csv", "neuropatia_comentarios_toxicidades_4"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "neuropatia_toxicidades_4"): ("Comorbidity", "condition"),
    ("tratamiento 4.csv", "numero_ciclos_enfermedad_osea_induccion_4"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_comentarios_toxicidades_4"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_comentarios_toxicidades_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_especificar_toxicidades_4"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_especificar_toxicidades_5"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_toxicidades_4"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 4.csv", "otras_toxicidades_toxicidades_5"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 4.csv", "recaida_motivo_discontinuacion_4"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 4.csv", "recaida_motivo_discontinuacion_describir_4"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 4.csv", "respuesta_despues_mantenimiento_4"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 4.csv", "respuesta_despues_mantenimiento_fecha_4"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 4.csv", "tipo_cadena_ligera_4"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("tratamiento 4.csv", "tipo_cadena_pesada_4"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("tratamiento 4.csv", "tipo_cadena_pesada_otros_4"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("tratamiento 4.csv", "tipo_infeccion_documentada_foco_induccion_4"): (
        "Comorbidity",
        "infection_source",
    ),
    ("tratamiento 4.csv", "tipo_infeccion_documentada_microorganismo_induccion_4"): (
        "Comorbidity",
        "type_of_microorganism_infection",
    ),
    (
        "tratamiento 4.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_4",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 4.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_4"): (
        "BoneDisease",
        "treatment_type",
    ),
    ("tratamiento 4.csv", "tipo_tratamiento_enfermedad_osea_describir_induccion_4"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 4.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_4",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 4.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_4"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 4.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_4",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 4.csv", "tratamiento_comentarios_4"): ("MMRegimen", "comments"),
    ("tratamiento 4.csv", "tratamiento_enfermedad_osea_fecha_ifin_induccion_4"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 4.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_4"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 4.csv", "tratamiento_mantenimiento_fecha_fin_4"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 4.csv", "tratamiento_mantenimiento_fecha_inicio_4"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 4.csv", "tratamiento_mantenimiento_numero_ciclos_4"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_fecha_fin_4"): ("MMRegimen", "end_date"),
    ("tratamiento 4.csv", "tratamiento_recaida_fecha_inicio_4"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_negativizacion_emr_4"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_numero_ciclos_4"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_progresion_fecha_4"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_respuesta_4"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 4.csv", "tratamiento_recaida_respuesta_fecha_4"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 4.csv", "vertebroplastia_cifoplastia_comentarios_induccion_4"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 4.csv", "vertebroplastia_cifoplastia_fecha_induccion_4"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
    ("tratamiento 5.csv", "cociente_kappa_lambda_5"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("tratamiento 5.csv", "comentarios_mantenimiento_5"): ("MMRegimen", "comments"),
    ("tratamiento 5.csv", "cuant_cadena_ligera_kappa_5"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("tratamiento 5.csv", "cuant_cadena_ligera_lambda_5"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("tratamiento 5.csv", "cuant_monoclonal_serico_5"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("tratamiento 5.csv", "esquema_mantenimiento_5"): ("MMRegimen", "regimen"),
    ("tratamiento 5.csv", "esquema_mantenimiento_describir_5"): (
        "MMRegimen",
        "comments",
    ),
    ("tratamiento 5.csv", "esquema_tratamiento_5"): ("MMRegimen", "regimen"),
    ("tratamiento 5.csv", "esquema_tratamiento_otros_5"): ("MMRegimen", "regimen"),
    ("tratamiento 5.csv", "fiebre_comentarios_toxicidades_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 5.csv", "fiebre_toxicidades_5"): ("Comorbidity", "condition"),
    ("tratamiento 5.csv", "hemorragias_comentarios_toxicidades_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 5.csv", "hemorragias_toxicidades_5"): ("Comorbidity", "condition"),
    ("tratamiento 5.csv", "indicar_bifosfonato_induccion_5"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 5.csv", "insuficiencia_renal_comentarios_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 5.csv", "insuficiencia_renal_toxicidades_5"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 5.csv", "mantenimiento_progresion_fecha_5"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 5.csv", "manteniniemto_motivo_discontinuacion_5"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 5.csv", "manteniniemto_motivo_discontinuacion_describir_5"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 5.csv", "motivo_inicio_tratamiento_5"): ("MMRegimen", "start_reason"),
    ("tratamiento 5.csv", "negativizacion_emr_mantenimiento_5"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 5.csv", "negativizacion_emr_mantenimiento_fecha_5"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 5.csv", "neuropatia_comentarios_toxicidades_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 5.csv", "neuropatia_toxicidades_5"): ("Comorbidity", "condition"),
    ("tratamiento 5.csv", "numero_ciclos_enfermedad_osea_induccion_5"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 5.csv", "otras_toxicidades_comentarios_toxicidades_5"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 5.csv", "recaida_motivo_discontinuacion_5"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 5.csv", "recaida_motivo_discontinuacion_describir_5"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 5.csv", "respuesta_despues_mantenimiento_5"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 5.csv", "respuesta_despues_mantenimiento_fecha_5"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 5.csv", "tecnica_emr2_5"): ("MMResponse", "mrd_technique"),
    ("tratamiento 5.csv", "tipo_cadena_ligera_5"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("tratamiento 5.csv", "tipo_cadena_pesada_5"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("tratamiento 5.csv", "tipo_cadena_pesada_otros_5"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("tratamiento 5.csv", "tipo_infeccion_documentada_foco_induccion_5"): (
        "Comorbidity",
        "infection_source",
    ),
    ("tratamiento 5.csv", "tipo_infeccion_documentada_microorganismo_induccion_5"): (
        "Comorbidity",
        "type_of_microorganism_infection",
    ),
    (
        "tratamiento 5.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_5",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 5.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_5"): (
        "BoneDisease",
        "treatment_type",
    ),
    ("tratamiento 5.csv", "tipo_tratamiento_enfermedad_osea_describir_induccion_5"): (
        "BoneDisease",
        "treatment_details",
    ),
    (
        "tratamiento 5.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_5",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 5.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_5"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 5.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_5",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 5.csv", "tratamiento_comentarios_5"): ("MMRegimen", "comments"),
    ("tratamiento 5.csv", "tratamiento_enfermedad_osea_fecha_ifin_induccion_5"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 5.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_5"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 5.csv", "tratamiento_mantenimiento_fecha_fin_5"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 5.csv", "tratamiento_mantenimiento_fecha_inicio_5"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 5.csv", "tratamiento_mantenimiento_numero_ciclos_5"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_fecha_fin_5"): ("MMRegimen", "end_date"),
    ("tratamiento 5.csv", "tratamiento_recaida_fecha_inicio_5"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_negativizacion_emr_5"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_numero_ciclos_5"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_progresion_fecha_5"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_respuesta_5"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 5.csv", "tratamiento_recaida_respuesta_fecha_5"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 5.csv", "vertebroplastia_cifoplastia_comentarios_induccion_5"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 5.csv", "vertebroplastia_cifoplastia_fecha_induccion_5"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
    ("tratamiento 6.csv", "cociente_kappa_lambda_6"): (
        "MProteinMesurements",
        "kappa_lambda_ratio",
    ),
    ("tratamiento 6.csv", "comentarios_mantenimiento_6"): ("MMRegimen", "comments"),
    ("tratamiento 6.csv", "cuant_cadena_ligera_kappa_6"): (
        "MProteinMesurements",
        "kappa_light_chain_count",
    ),
    ("tratamiento 6.csv", "cuant_cadena_ligera_lambda_6"): (
        "MProteinMesurements",
        "lambda_light_chain_count",
    ),
    ("tratamiento 6.csv", "cuant_monoclonal_serico_6"): (
        "MProteinMesurements",
        "serum_amount",
    ),
    ("tratamiento 6.csv", "esquema_mantenimiento_6"): ("MMRegimen", "regimen"),
    ("tratamiento 6.csv", "esquema_mantenimiento_describir_6"): (
        "MMRegimen",
        "comments",
    ),
    ("tratamiento 6.csv", "esquema_tratamiento_6"): ("MMRegimen", "regimen"),
    ("tratamiento 6.csv", "esquema_tratamiento_otros_6"): ("MMRegimen", "regimen"),
    ("tratamiento 6.csv", "fiebre_comentarios_toxicidades_6"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 6.csv", "fiebre_toxicidades_6"): ("Comorbidity", "condition"),
    ("tratamiento 6.csv", "hemorragias_comentarios_toxicidades_6"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 6.csv", "hemorragias_toxicidades_6"): ("Comorbidity", "condition"),
    ("tratamiento 6.csv", "indicar_bifosfonato_induccion_6"): (
        "BoneDisease",
        "bisphosphonate_treatment",
    ),
    ("tratamiento 6.csv", "insuficiencia_renal_comentarios_6"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 6.csv", "insuficiencia_renal_toxicidades_6"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 6.csv", "mantenimiento_progresion_fecha_6"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 6.csv", "manteniniemto_motivo_discontinuacion_6"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 6.csv", "manteniniemto_motivo_discontinuacion_describir_6"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 6.csv", "motivo_inicio_tratamiento_6"): ("MMRegimen", "start_reason"),
    ("tratamiento 6.csv", "negativizacion_emr_mantenimiento_6"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 6.csv", "negativizacion_emr_mantenimiento_fecha_6"): (
        "MMResponse",
        "negative_mrd_date",
    ),
    ("tratamiento 6.csv", "neuropatia_comentarios_toxicidades_6"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 6.csv", "neuropatia_toxicidades_6"): ("Comorbidity", "condition"),
    ("tratamiento 6.csv", "numero_ciclos_enfermedad_osea_induccion_6"): (
        "BoneDisease",
        "nb_cycles",
    ),
    ("tratamiento 6.csv", "otras_toxicidades_comentarios_toxicidades_6"): (
        "Comorbidity",
        "details",
    ),
    ("tratamiento 6.csv", "otras_toxicidades_especificar_toxicidades_6"): (
        "Comorbidity",
        "other_condition_name",
    ),
    ("tratamiento 6.csv", "otras_toxicidades_toxicidades_6"): (
        "Comorbidity",
        "condition",
    ),
    ("tratamiento 6.csv", "recaida_motivo_discontinuacion_6"): (
        "MMRegimen",
        "stop_reason",
    ),
    ("tratamiento 6.csv", "recaida_motivo_discontinuacion_describir_6"): (
        "MMRegimen",
        "stop_reason_details",
    ),
    ("tratamiento 6.csv", "respuesta_despues_mantenimiento_6"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 6.csv", "respuesta_despues_mantenimiento_fecha_6"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 6.csv", "tipo_cadena_ligera_6"): (
        "MProteinMesurements",
        "light_chain_type",
    ),
    ("tratamiento 6.csv", "tipo_cadena_pesada_6"): (
        "MProteinMesurements",
        "heavy_chain_type",
    ),
    ("tratamiento 6.csv", "tipo_cadena_pesada_otros_6"): (
        "MProteinMesurements",
        "heavy_chain_type_other",
    ),
    ("tratamiento 6.csv", "tipo_infeccion_documentada_foco_induccion_6"): (
        "Comorbidity",
        "infection_source",
    ),
    ("tratamiento 6.csv", "tipo_infeccion_documentada_microorganismo_induccion_6"): (
        "Comorbidity",
        "type_of_microorganism_infection",
    ),
    (
        "tratamiento 6.csv",
        "tipo_tratamiento_enfermedad_osea_bisfosfonatos_induccion_6",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 6.csv", "tipo_tratamiento_enfermedad_osea_denosumab_induccion_6"): (
        "BoneDisease",
        "treatment_type",
    ),
    ("tratamiento 6.csv", "tipo_tratamiento_enfermedad_osea_describir_induccion_6"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 6.csv",
        "tipo_tratamiento_enfermedad_osea_nodisponible_induccion_6",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 6.csv", "tipo_tratamiento_enfermedad_osea_otros_induccion_6"): (
        "BoneDisease",
        "treatment_type",
    ),
    (
        "tratamiento 6.csv",
        "tipo_tratamiento_enfermedad_osea_vertebroplastia_induccion_6",
    ): ("BoneDisease", "treatment_type"),
    ("tratamiento 6.csv", "tratamiento_comentarios_6"): ("MMRegimen", "comments"),
    ("tratamiento 6.csv", "tratamiento_enfermedad_osea_fecha_ifin_induccion_6"): (
        "BoneDisease",
        "end_date",
    ),
    ("tratamiento 6.csv", "tratamiento_enfermedad_osea_fecha_inicio_induccion_6"): (
        "BoneDisease",
        "start_date",
    ),
    ("tratamiento 6.csv", "tratamiento_mantenimiento_fecha_fin_6"): (
        "MMRegimen",
        "end_date",
    ),
    ("tratamiento 6.csv", "tratamiento_mantenimiento_fecha_inicio_6"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 6.csv", "tratamiento_mantenimiento_numero_ciclos_6"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_fecha_fin_6"): ("MMRegimen", "end_date"),
    ("tratamiento 6.csv", "tratamiento_recaida_fecha_inicio_6"): (
        "MMRegimen",
        "start_date",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_negativizacion_emr_6"): (
        "MMResponse",
        "negative_mrd",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_numero_ciclos_6"): (
        "MMRegimen",
        "nbCycles",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_progresion_fecha_6"): (
        "MMResponse",
        "progression_date",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_respuesta_6"): (
        "MMResponse",
        "response",
    ),
    ("tratamiento 6.csv", "tratamiento_recaida_respuesta_fecha_6"): (
        "MMResponse",
        "response_date",
    ),
    ("tratamiento 6.csv", "vertebroplastia_cifoplastia_comentarios_induccion_6"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_description",
    ),
    ("tratamiento 6.csv", "vertebroplastia_cifoplastia_fecha_induccion_6"): (
        "BoneDisease",
        "vertebroplasty_kyphoplasty_date",
    ),
}
