-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- object: operador | type: ROLE --
-- DROP ROLE IF EXISTS operador;
CREATE ROLE operador WITH 
	INHERIT
	LOGIN
	ENCRYPTED PASSWORD '********';
-- ddl-end --
COMMENT ON ROLE operador IS E'Usuario para la inserción de los datos en la base de datos workstations';
-- ddl-end --


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: workstations | type: DATABASE --
-- -- DROP DATABASE IF EXISTS workstations;
-- CREATE DATABASE workstations
-- 	ENCODING = 'UTF8'
-- 	LC_COLLATE = 'es_ES.UTF-8'
-- 	LC_CTYPE = 'es_ES.UTF-8'
-- 	TABLESPACE = pg_default
-- 	OWNER = operador;
-- -- ddl-end --
-- COMMENT ON DATABASE workstations IS E'Datos recopilados de las estaciones de trabajo de nuestra red local.\nTambién contiene datos sobre las intervenciones realizadas es los mismos.';
-- -- ddl-end --
-- 

-- object: public.infocpu | type: TABLE --
-- DROP TABLE IF EXISTS public.infocpu CASCADE;
CREATE TABLE public.infocpu (
	host character(15) NOT NULL,
	cpu character(50),
	so character(50),
	memory smallint,
	disk smallint,
	free_disk smallint,
	sn character(50),
	model character(50),
	notes text,
	date_info date DEFAULT Now(),
	host_hosts character(15),
	CONSTRAINT infocpu_pk PRIMARY KEY (host)

);
-- ddl-end --
ALTER TABLE public.infocpu OWNER TO operador;
-- ddl-end --

-- object: public.network_info | type: TABLE --
-- DROP TABLE IF EXISTS public.network_info CASCADE;
CREATE TABLE public.network_info (
	host character(15) NOT NULL,
	mac character(17) NOT NULL,
	ip character(15),
	model character(50),
	date_info date DEFAULT Now(),
	host_hosts character(15),
	CONSTRAINT network_info_pk PRIMARY KEY (mac)

);
-- ddl-end --
ALTER TABLE public.network_info OWNER TO operador;
-- ddl-end --

-- object: public.intervention | type: TABLE --
-- DROP TABLE IF EXISTS public.intervention CASCADE;
CREATE TABLE public.intervention (
	id serial NOT NULL,
	host character(15) NOT NULL,
	description text,
	interv_date date DEFAULT Now(),
	solution text,
	technician character(25),
	host_hosts character(15),
	CONSTRAINT intervention_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.intervention OWNER TO operador;
-- ddl-end --

-- object: public.hosts | type: TABLE --
-- DROP TABLE IF EXISTS public.hosts CASCADE;
CREATE TABLE public.hosts (
	host character(15) NOT NULL,
	ip character(40),
	CONSTRAINT nombres_pk PRIMARY KEY (host)

);
-- ddl-end --
ALTER TABLE public.hosts OWNER TO operador;
-- ddl-end --

-- object: public.services | type: TABLE --
-- DROP TABLE IF EXISTS public.services CASCADE;
CREATE TABLE public.services (
	id serial NOT NULL,
	host character(1) NOT NULL,
	name character(100),
	state character(10),
	date_info date DEFAULT Now(),
	host_hosts character(15),
	CONSTRAINT services_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.services OWNER TO operador;
-- ddl-end --

-- object: public.software | type: TABLE --
-- DROP TABLE IF EXISTS public.software CASCADE;
CREATE TABLE public.software (
	host character(15),
	id serial NOT NULL,
	name character(100),
	version character(20),
	editor character(50),
	host_hosts character(15),
	CONSTRAINT software_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.software OWNER TO operador;
-- ddl-end --

-- object: hosts_fk | type: CONSTRAINT --
-- ALTER TABLE public.network_info DROP CONSTRAINT IF EXISTS hosts_fk CASCADE;
ALTER TABLE public.network_info ADD CONSTRAINT hosts_fk FOREIGN KEY (host_hosts)
REFERENCES public.hosts (host) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: hosts_fk | type: CONSTRAINT --
-- ALTER TABLE public.services DROP CONSTRAINT IF EXISTS hosts_fk CASCADE;
ALTER TABLE public.services ADD CONSTRAINT hosts_fk FOREIGN KEY (host_hosts)
REFERENCES public.hosts (host) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: hosts_fk | type: CONSTRAINT --
-- ALTER TABLE public.intervention DROP CONSTRAINT IF EXISTS hosts_fk CASCADE;
ALTER TABLE public.intervention ADD CONSTRAINT hosts_fk FOREIGN KEY (host_hosts)
REFERENCES public.hosts (host) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: hosts_fk | type: CONSTRAINT --
-- ALTER TABLE public.software DROP CONSTRAINT IF EXISTS hosts_fk CASCADE;
ALTER TABLE public.software ADD CONSTRAINT hosts_fk FOREIGN KEY (host_hosts)
REFERENCES public.hosts (host) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: hosts_fk | type: CONSTRAINT --
-- ALTER TABLE public.infocpu DROP CONSTRAINT IF EXISTS hosts_fk CASCADE;
ALTER TABLE public.infocpu ADD CONSTRAINT hosts_fk FOREIGN KEY (host_hosts)
REFERENCES public.hosts (host) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: infocpu_uq | type: CONSTRAINT --
-- ALTER TABLE public.infocpu DROP CONSTRAINT IF EXISTS infocpu_uq CASCADE;
ALTER TABLE public.infocpu ADD CONSTRAINT infocpu_uq UNIQUE (host_hosts);
-- ddl-end --


