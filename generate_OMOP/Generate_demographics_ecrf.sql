select distinct
p.person_id as Hospital_patient_ID,
p.day_of_birth::text || '/' || p.month_of_birth::text || '/' || p.year_of_birth::text as dob,
case 
	when p.gender_concept_id=8507 then 'Male'
	when p.gender_concept_id=8532 then 'Female'
	else 'Unknown'
end as gender,
case 
	when d.death_date is not null then 'Dead'
	else 'Under treatment' 
	end as status,
d.death_date as date_of_death,
case 
	when m.value_as_concept_id =  4188540 then 'No'
	when m.value_as_concept_id =4188539 then 'Yes'
	when m.value_as_concept_id =45882933 then 'Unknown'
	else 'Unknown' end as del17p,
case 
	when m2.value_as_concept_id =  4188540 then 'No'
	when m2.value_as_concept_id =4188539 then 'Yes'
	when m2.value_as_concept_id =45882933 then 'Unknown'
	else 'Unknown' end as Del13,
case 
	when m3.value_as_concept_id =  4188540 then 'No'
	when m3.value_as_concept_id =4188539 then 'Yes'
	when m3.value_as_concept_id =45882933 then 'Unknown'
	else 'Unknown' end as "t(4;14)(p16;q32)",
case
	when m4.value_as_concept_id = 2000000719 then 'Stage II'
	when m4.value_as_concept_id = 2000000718 then 'Stage I'
	when m4.value_as_concept_id =   45877986 then 'Unknown'
	when m4.value_as_concept_id = 2000000720 then 'Stage III'
	end as "ISS Stage",
case
	when m5.value_as_concept_id = 2000000722 then 'Stage II'
	when m5.value_as_concept_id =   45877986 then 'Unknown'
	when m5.value_as_concept_id = 2000000723 then 'Stage III'
	when m5.value_as_concept_id = 2000000721 then 'Stage I'
	end as "Durie-Salmon Stage",
co.condition_start_date as date_of_diagnosis
from person p
left join omopcdm.condition_occurrence co on p.person_id = co.person_id
left join omopcdm.death d on d.person_id  = p.person_id
left join omopcdm.measurement m on m.person_id = p.person_id 
left join omopcdm.measurement m2 on m2.person_id =p.person_id 
left join omopcdm.measurement m3 on m3.person_id =p.person_id 
left join omopcdm.measurement m4 on m4.person_id =p.person_id 
left join omopcdm.measurement m5 on m5.person_id =p.person_id 
where co.condition_concept_id = 437233 
	and m.measurement_concept_id = 2000000016 
	and m2.measurement_concept_id = 2000000018 
	and m3.measurement_concept_id = 2000000020 
	and m4.measurement_concept_id = 2000000008	and m4.measurement_date = co.condition_start_date
	and m5.measurement_concept_id = 2000000009 and m5.measurement_date = co.condition_start_date
	
	