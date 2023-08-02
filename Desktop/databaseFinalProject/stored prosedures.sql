DELIMITER //
create procedure mydb.spGetDetailsByCityName(IN zip_code INT)
BEGIN
  select *
  from city
  where zipcode = zip_code; 

end //
DELIMITER ;

call mydb.spGetDetailsByCityName(93225);

DELIMITER //
create procedure mydb.spGetAvgGbDownLoad(OUT avgGb INT)
BEGIN
  select avg(value_integer)
  INTO avgGb
  from customer_has_property_integer
  where property_integer_idproperty_integer = (select idproperty_integer from property_integer where property_integercol_name="Avg Monthly GB Download");
end //
DELIMITER ;

call mydb.spGetAvgGbDownLoad(@avgGb);
select @avgGb;


DELIMITER //
create procedure mydb.spNewTotalCharges(INOUT total_charge float, IN kdv float)
BEGIN
set total_charge = total_charge + kdv;
end //
DELIMITER ;

set @total_charge = 15.87;

call mydb.spNewTotalCharges(@total_charge,12);
select @total_charge;





