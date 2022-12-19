CREATE PROCEDURE 'getcustomersbycountry'(IN c VARCHAR(45))
   BEGIN
     select CustomerID, CustomerName, Address, City
     from customers
     where Country="c";

     set @c = "Turkey"
   END
