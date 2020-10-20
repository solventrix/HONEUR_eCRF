select
	tl.person_id as Hospital_patient_ID,
	tl.line_number as LOT,
	tl.drug_era_start_date as Start_date,
	tl.drug_era_end_date as end_date,
	c.concept_name as regimen,
	null as response,
	null as response_date,
	null as SCT_type,
	null as SCT_date
from omopcdm.treatment_line tl 
left join omopcdm.concept c on c.concept_id = tl.drug_concept_id 
union
select
	tl.person_id as Hospital_patient_ID,
	tl.line_number as LOT,
	null as Start_date,
	null as end_date,
	null as regimen,
	c.concept_name as response,
	o.observation_date as response_date,
	null as SCT_type,
	null as SCT_date
from omopcdm.treatment_line tl 
left join omopcdm.observation o on o.person_id = tl.person_id 
left join omopcdm.concept c on c.concept_id = o.observation_concept_id 
where observation_concept_id in (2000000608, 2000000601, 2000000602, 2000000610,2000000604,2000000609,2000000611,2000000603)
and o.observation_date > tl.drug_era_start_date -30 and o.observation_date <= tl.drug_era_end_date + 30 
union
select
	tl.person_id as Hospital_patient_ID,
	tl.line_number as LOT,
	null as Start_date,
	null as end_date,
	null as regimen,
	null as response,
	null as response_date,
	'Autologous' as SCT_type,
	po.procedure_date::text as SCT_date
from omopcdm.treatment_line tl 
left join omopcdm.procedure_occurrence po on po.person_id = tl.person_id 
where po.procedure_concept_id = 4144157
and po.procedure_date >= tl.line_start_date and po.procedure_date <= tl.line_end_date
order by Hospital_patient_ID, LOT, Start_date
