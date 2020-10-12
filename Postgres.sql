-- Table: public.Users

-- DROP TABLE public."Users";

CREATE TABLE public."Users"
(
    id integer NOT NULL,
    brukernavn character varying(30) COLLATE pg_catalog."default",
    epost character varying(254) COLLATE pg_catalog."default",
    passord character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT "Users_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public."Users"
    OWNER to postgres;