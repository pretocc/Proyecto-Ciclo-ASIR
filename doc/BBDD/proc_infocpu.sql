-- Procedimiento para insertar los datos de sistema de los pcs en la tabla infocpu
CREATE OR REPLACE PROCEDURE public.add_infocpu(
	p_host character,
	p_cpu character,
	p_so character,
	p_memory smallint,
	p_disk smallint,
	p_free_disk smallint,
	p_sn character,
	p_model character,
	INOUT p_msg_error character)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO infocpu(host, cpu, so, memory, disk, free_disk, sn, model) 
	VALUES (P_host, P_cpu, P_so, P_memory, P_disk, P_free_disk, P_sn, P_model)
		ON CONFLICT (host)
	DO
		UPDATE SET cpu = P_cpu, so = P_so, memory = P_memory, disk = P_disk,
		free_disk = P_free_disk, sn = P_sn, model = P_model, date_info = NOW();
	 
EXCEPTION WHEN OTHERS THEN
        P_msg_error := SQLERRM;	
END;
$BODY$;