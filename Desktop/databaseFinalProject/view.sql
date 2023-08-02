select avg(value_integer)
from customer_has_property_integer
where property_integer_idproperty_integer = (select idproperty_integer from property_integer where property_integercol_name="age");

create view customerfullids as select idcustomer,idcustomer_string from customercustomerfullids;

select * from customerfullids