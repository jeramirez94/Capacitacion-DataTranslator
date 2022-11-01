--.schema

--.databases

SELECT  *
FROM    actor;

SELECT  first_name || ' ' || last_name as 'Actor_Name'
FROM    actor;

SELECT  actor_id, first_name, last_name
FROM    actor
WHERE   first_name = 'joe'

SELECT  actor_id, first_name, last_name
FROM    actor
WHERE   last_name like '%gen%'

SELECT  actor_id, first_name, last_name
FROM    actor
WHERE   last_name like '%LI%'
order by last_name asc, first_name asc

SELECT  country_id, country
FROM    country
WHERE   country in ('Afghanistan', 'Bangladesh', 'China')

--Enumera los apellidos de los actores, así como cuántos actores tienen ese apellido.
SELECT  last_name, count(1) as cantidad_de_actores
FROM    actor
GROUP   BY last_name

--Enumere los apellidos de los actores y el número de actores que tienen ese apellido, 
--pero sólo para los nombres que comparten al menos dos actores.
SELECT  last_name, count(1) as cantidad_de_actores
FROM    actor
GROUP   BY last_name
having count(1) > 1

--Utilice JOIN para mostrar los nombres y apellidos, así como la dirección, 
--de cada miembro del personal. Utilice las tablas staff y address:
SELECT  s.first_name, s.last_name, a.address
FROM    staff s 
INNER JOIN    address a
    ON  s.address_id = a.address_id

--Utilice JOIN para mostrar el importe total recaudado por cada miembro del personal 
--en agosto de 2005. Utilice las tablas personal y pago.
SELECT  s.first_name, s.last_name,  round(sum(amount),2) total
FROM    staff s
INNER JOIN    payment p
    on  s.staff_id = p.staff_id
WHERE   p.payment_date >= '2005-08-01'
    AND p.payment_date <= '2005-08-31'
group by s.first_name, s.last_name


--Enumere cada película y el número de actores que figuran en ella. 
--Utilice las tablas actor_película y película. Utilice la unión interna.
SELECT  f.title, count(1) as num_actors
FROM    film f
INNER JOIN  film_actor fa
    ON  f.film_id = fa.film_id
GROUP BY f.title;

--¿Cuántas copias de la película Jorobado Imposible existen en el sistema de inventario?
SELECT  f.title, count(1) as inventary_amount
FROM    film f
INNER JOIN inventory i
    ON  f.film_id = i.film_id
WHERE   title = 'HUNCHBACK IMPOSSIBLE';


--Utilizando las tablas payment y customer y el comando JOIN, 
--enumera el total pagado por cada cliente. Enumera los clientes alfabéticamente por su apellido
SELECT  c.last_name, c.first_name, sum(amount) total_payment
FROM    customer c
INNER JOIN payment p
    ON  c.customer_id = p.customer_id
GROUP   BY c.last_name, c.first_name
ORDER BY c.last_name

-- La música de Queen ha experimentado un improbable resurgimiento. Como consecuencia involuntaria, 
-- las películas que empiezan por la letra Q también han aumentado su popularidad. Utilice subconsultas 
-- para mostrar los títulos de las películas que empiezan por la letra Q y cuyo idioma es el inglés.
SELECT  f.title
FROM    film f
INNER JOIN  language l
    ON  f.language_id = l.language_id
WHERE   f.title like 'Q%'
    AND l.name = 'English'

--Utiliza las subconsultas para mostrar todos los actores que aparecen en la película Alone Trip.
SELECT  f.title, a.first_name || ' ' || a.last_name as 'Actor_Name'
FROM    film f
INNER JOIN  film_actor fa
    ON  f.film_id = fa.film_id
INNER   JOIN    actor a
    ON  fa.actor_id = a.actor_id
WHERE   f.title = 'ALONE TRIP'
GROUP BY 2;

--Desea realizar una campaña de marketing por correo electrónico en Canadá, 
--para lo cual necesitará los nombres y las direcciones de correo electrónico de todos los clientes canadienses. 
--Utilice uniones para recuperar esta información.
SELECT  cm.first_name || ' ' || cm.last_name, cm.email
FROM    customer cm
INNER   JOIN    address a
    ON  cm.address_id = a.address_id
INNER   JOIN    city ct
    ON  a.city_id = ct.city_id
INNER   JOIN    country cr
    ON  ct.country_id = cr.country_id
WHERE   cr.country = 'Canada'


--Las ventas han disminuido entre las familias jóvenes, y usted desea dirigirse a todas las películas familiares 
--para una promoción. Identifique todas las películas categorizadas como familiares.
SELECT  f.title, c.name
FROM    film f
JOIN    film_category fc
    ON  f.film_id = fc.film_id
JOIN    category c
    ON  fc.category_id = c.category_id
WHERE   c.name = 'Family'

--Muestre las películas más alquiladas en orden descendente.
SELECT  *
FROM    film
order   by rental_rate desc
LIMIT   10

--Escriba una consulta para mostrar el volumen de negocio, en dólares, de cada tienda.
SELECT  st.store_id, sum(r.amount) as dollares
FROM    payment r
JOIN    staff s
    ON  r.staff_id = s.staff_id
JOIN    store st
    ON  s.store_id = st.store_id
GROUP BY  s.store_id

--Escribir una consulta para mostrar para cada tienda su ID de tienda, ciudad y país.
SELECT  s.store_id, ct.city as city, cr.country
FROM    store s
INNER   JOIN    address a
    ON  s.address_id = a.address_id
INNER   JOIN    city ct
    ON  a.city_id = ct.city_id
INNER   JOIN    country cr
    ON  ct.country_id = cr.country_id

--Enumere los cinco géneros más importantes en ingresos brutos en orden descendente. 
--(Sugerencia: es posible que tenga que utilizar las siguientes tablas: categoría, film_category, 
--inventario, pago y alquiler).

SELECT  c.name, sum(pay.amount)
FROM    payment pay
JOIN    rental r
    ON  pay.rental_id = r.rental_id
JOIN    inventory i
    ON  r.inventory_id = i.inventory_id
JOIN    film f
    ON  i.film_id = f.film_id
JOIN    film_category fc
    ON  f.film_id = fc.film_id
JOIN    category c
    ON  fc.category_id = c.category_id
GROUP by c.name
ORDER BY 2 DESC
LIMIT 5