SELECT distinct
	 m.person_id AS Hospital_patient_ID,
	 m.measurement_date AS followup_date,
	 m2.value_as_number AS LDH,
	 m3.value_as_number AS MProtein_urine,
	 m4.value_as_number AS b2m,
	 m5.value_as_number AS albumin,
	 m6.value_as_number AS MProtein_serum
FROM omopcdm.measurement m
LEFT JOIN 
	(
		SELECT * FROM omopcdm.measurement m 
		WHERE m.measurement_concept_id = 3005783
	) m2 ON m2.measurement_date = m.measurement_date AND m2.person_id = m.person_id 
LEFT JOIN 
(
	SELECT * FROM omopcdm.measurement m
	WHERE m.measurement_concept_id = 3036416
) m3 ON m3.measurement_date = m.measurement_date AND m3.person_id = m.person_id
LEFT JOIN 
(
	SELECT * FROM omopcdm.measurement m
	WHERE m.measurement_concept_id = 4042560
) m4 ON m4.measurement_date = m.measurement_date AND m4.person_id = m.person_id 

LEFT JOIN 
(
	SELECT * FROM omopcdm.measurement m
	WHERE m.measurement_concept_id = 40483245
) m5 ON m5.measurement_date = m.measurement_date AND m5.person_id = m.person_id 
LEFT JOIN 
(
	SELECT * FROM omopcdm.measurement m
	WHERE m.measurement_concept_id = 2000000728
) m6 ON m6.measurement_date = m.measurement_date AND m6.person_id = m.person_id 
where m.measurement_concept_id IN (3005783,3036416,4042560,40483245,2000000728)
ORDER BY Hospital_patient_ID
