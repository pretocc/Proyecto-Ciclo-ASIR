-- Procedimiento para insertar el software de los pcs en la tabla software
CREATE OR REPLACE PROCEDURE public.add_software(
	p_host character,
	p_name character,
	p_version character,
	p_editor character,
	INOUT p_msg_error character)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO software(host, name, version, editor) 
	VALUES (P_host, P_name, P_version, P_editor);
	 
EXCEPTION WHEN OTHERS THEN
        P_msg_error := SQLERRM;	
END;
$BODY$;