# DB-HSE-Project
In order to make this thing work, you have to use postgresql server called studhubcreation - its creation is listed below - and a number of extensions for python that
are listed in requirements.txt.

To make sure that it works properly, run:

$ cd bdproject

$ python manage.py makemigrations

$ python manage.py migrate

If there was no failure messages, run:
$ python manage.py runserver

And you're good to go.


The creation of studhubcreation:
CREATE DATABASE studHubCreation;

Open up the query tool in studHubCreation and paste. Make sure that you have the proper password instead of '***':

-- FUNCTION: public.studhubstart()

-- DROP FUNCTION public.studhubstart();

CREATE OR REPLACE FUNCTION public.studhubstart(
	)
    RETURNS void
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
	begin
	
		-- create extension dblink;
		PERFORM dblink_connect('studhub', 'dbname=studHubCreation port=5432 host=localhost user=postgres password=***');
		PERFORM dblink_exec('studhub', 'create database studHub;');
		PERFORM dblink_disconnect('studhub');
		
	end;
	
$BODY$;

ALTER FUNCTION public.studhubstart()
    OWNER TO postgres;
    
create extension dblink;
select studhubstart();
