------------Tabale name: scarmart_employee_information---------
select * from scarmart_employee_information
-------------employee details for a person---------
create PROCEDURE each_person
	@person_id varchar(15)
as
begin
     select * from scarmart_employee_information
	 where employeed_id=@person_id
end

-----employees in a department---------
create PROCEDURE each_department_information
	@department varchar(15)
as
begin
     select top 10 * from scarmart_employee_information
	 where department=@department

end