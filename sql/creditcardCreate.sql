-- Crea la tabla de usuarios
create table creditcard (
  card_number varchar( 20 ) NOT NULL PRIMARY KEY,
  owner_id text NOT NULL,
  owner_name text NOT NULL,
  bank_name text NOT NULL,
  due_date varchar(20) NOT NULL,
  franchise text NOT NULL,
  payment_day varchar(20) NOT NULL,
  monthly_fee varchar(40) NOT NULL,
  interest_rate varchar(20) NOT NULL
); 