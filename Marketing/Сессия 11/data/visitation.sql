-- Table: public.visitation

-- DROP TABLE IF EXISTS public.visitation;

CREATE TABLE IF NOT EXISTS public.visitation
(
    "User Id" text COLLATE pg_catalog."default",
    "Region" text COLLATE pg_catalog."default",
    "Device" text COLLATE pg_catalog."default",
    "Channel" text COLLATE pg_catalog."default",
    "Session Start" text COLLATE pg_catalog."default",
    "Session End" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.visitation
    OWNER to postgres;