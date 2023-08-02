select distinct
table1.zip, table1.pop, table2.lat,table2.long,table2.name
from table1 join table2 on table1.zip = table2.table1_zip
