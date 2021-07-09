-- Preguntas a responder
--1. ¿Cuántos Leads compro cada consumidor?
SELECT DISTINCT (comprador), count(*) FROM compradores GROUP BY comprador;

--2. ¿Cuántos leads creo cada productos?
SELECT DISTINCT (id_productor), count(*) FROM leads GROUP BY id_productor;

--3. ¿Cuánto tiempo promedio se tardo cada productor en producir un elemento?
SELECT 
id_productor,
((max(fecha_inicio)-min(fecha_inicio))/count(*))
FROM leads
GROUP BY
id_productor;
/*
SELECT
    id_productor,
    SUM(TIMESTAMPDIFF(SECOND,
                      fecha_inicio,
                      CASE WHEN endDate = '0000-00-00 00:00:00'
                           THEN CURRENT_TIMESTAMP ELSE endDate END)) AS timeTaken
FROM leads
GROUP BY id_productor;
*/
--4. ¿Cuánto tiempo le lleva a todo el sistema terminar de producir y consumir?


--5. ¿Cuánto tiempo tarde en terminar el sistema en un modelo de alternancia?


