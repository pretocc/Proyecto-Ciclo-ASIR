-- Procedimiento para insertar los servicios de los pcs en la tabla hosts
CREATE OR REPLACE PROCEDURE public.add_services(
	p_host character,
	p_name character,
	p_state character,
	INOUT p_msg_error character)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO services(host, name, state) 
	VALUES (P_host, P_name, P_state);
	 
EXCEPTION WHEN OTHERS THEN
        P_msg_error := SQLERRM;	
END;
$BODY$;