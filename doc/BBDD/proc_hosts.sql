-- Procedimiento para insertar los pcs en la tabla hosts
CREATE OR REPLACE PROCEDURE public.add_hosts(
	p_host character,
	p_ip character,
	INOUT p_msg_error character)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO hosts(host, ip) VALUES (P_host, P_ip)
	ON CONFLICT (host)
	DO
		UPDATE SET ip = P_ip;
	 
EXCEPTION WHEN OTHERS THEN
        P_msg_error := SQLERRM;	
END;
$BODY$;