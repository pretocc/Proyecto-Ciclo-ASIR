-- Procedimiento para insertar los datos de red de los pcs en la tabla network_info
CREATE OR REPLACE PROCEDURE public.add_network_info(
	p_host character,
	p_mac character,
	p_ip character,
	p_model character,
	INOUT p_msg_error character)
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO network_info(host, mac, ip, model) 
	VALUES (P_host, P_mac, P_ip, P_model)
		ON CONFLICT (mac)
	DO
		UPDATE SET host = P_host, ip = P_ip, model = P_model;
	 
EXCEPTION WHEN OTHERS THEN
        P_msg_error := SQLERRM;	
END;
$BODY$;