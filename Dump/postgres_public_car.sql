insert into public.car (identification_num, model, status, location, plate, company_id, color) values (1, 'CH11', 'used', '(123.0,43.0)', 'AN10200CS', 1, 'red');
insert into public.car (identification_num, model, status, location, plate, company_id, color) values (2, 'CH12', 'used', '(56.0,74.0)', 'AN10200CS', 1, 'red');
insert into public.car (identification_num, model, status, location, plate, company_id, color) values (3, 'Toyota', 'unused', '(197.0,31.0)', 'AF2001', 1, 'blue');
insert into public.car (identification_num, model, status, location, plate, company_id, color) values (4, 'Nissan', 'unused', '(65.0,87.0)', 'AC901', 1, 'black');
insert into public.car (identification_num, model, status, location, plate, company_id, color) values (5, 'Rav4', 'unused', '(77.0,87.0)', 'AK901', 1, 'orange');

insert into public.company (company_id, company_name) values (1, 'Aidar');

insert into public.customer (username, email, phone_number, location, full_name) values (1, 'larisa@mail.ru', 8777345621, '(231.0,129.0)', 'Cool Per');
insert into public.customer (username, email, phone_number, location, full_name) values (2, 'vitalii2@mail.ru', 8777345623, '(179.0,35.0)', 'Vitalii Pol');
insert into public.customer (username, email, phone_number, location, full_name) values (3, 'zakir@mail.ru', 8917914623, '(130.0,61.0)', 'Zakir Nur');
insert into public.customer (username, email, phone_number, location, full_name) values (4, 'artur@mail.ru', 8977201655, '(201.0,54.0)', 'Artur Akh');
insert into public.customer (username, email, phone_number, location, full_name) values (5, 'ilnur@mail.ru', 8777666623, '(801.0,555.0)', 'Ilnur Tel');

insert into public.history_of_charging (identification_num, uid, starting_ch, ending_ch, date) values (1, 2, '08:00:00', '08:50:00', '2018-11-25');
insert into public.history_of_charging (identification_num, uid, starting_ch, ending_ch, date) values (2, 3, '10:00:00', '10:10:00', '2018-11-26');
insert into public.history_of_charging (identification_num, uid, starting_ch, ending_ch, date) values (3, 3, '11:00:00', '11:30:00', '2018-11-24');

insert into public.history_of_providing (wid, pcompany_id, type_car_p) values (2, 1, 'dich1');
insert into public.history_of_providing (wid, pcompany_id, type_car_p) values (3, 2, 'dich2');

insert into public.history_of_repairing (identification_num, wid, price, car_parts, date) values (1, 2, 500, 'dich1', '2018-11-11');

insert into public.history_of_trip (trip_id, identification_num, username, starting_loc, client_loc, final_loc, date, starting_tr, ending_tr, price, location) values (1, 1, 1, '(3.0,10.0)', '(7.0,13.0)', '(2.0,4.0)', '2018-11-24', '09:00:00', '10:00:00', 200, 'Kazan');
insert into public.history_of_trip (trip_id, identification_num, username, starting_loc, client_loc, final_loc, date, starting_tr, ending_tr, price, location) values (2, 2, 2, '(1.0,5.0)', '(3.0,8.0)', '(8.0,9.0)', '2018-11-26', '17:00:00', '19:00:00', 300, 'Kazan');
insert into public.history_of_trip (trip_id, identification_num, username, starting_loc, client_loc, final_loc, date, starting_tr, ending_tr, price, location) values (3, 1, 2, '(6.0,3.0)', '(5.0,5.0)', '(10.0,6.0)', '2018-11-26', '15:00:00', '16:00:00', 500, 'Chelny');

insert into public.provider (pcompany_id, phone_num, address, name) values (1, 977722677, 'Kazan', 'YaSuperProvider');
insert into public.provider (pcompany_id, phone_num, address, name) values (2, 977722591, 'Elabuga', 'TopProvider');
insert into public.provider (pcompany_id, phone_num, address, name) values (3, 917228678, 'Chelny', 'Super777');
insert into public.provider (pcompany_id, phone_num, address, name) values (4, 965228888, 'Yekab', 'Prov21');
insert into public.provider (pcompany_id, phone_num, address, name) values (5, 917228666, 'Ilnov', 'Provider01');

insert into public.station (uid, location, price_of_charging, plug_formats, free_sockets, amount_of_sockets, company_id) values (1, '(25.0,25.0)', 100, 'all', 7, 7, 1);
insert into public.station (uid, location, price_of_charging, plug_formats, free_sockets, amount_of_sockets, company_id) values (2, '(25.0,75.0)', 200, 'all', 7, 7, 1);
insert into public.station (uid, location, price_of_charging, plug_formats, free_sockets, amount_of_sockets, company_id) values (3, '(75.0,25.0)', 100, 'all', 7, 7, 1);
insert into public.station (uid, location, price_of_charging, plug_formats, free_sockets, amount_of_sockets, company_id) values (4, '(75.0,75.0)', 200, 'all', 7, 7, 1);

insert into public.workshops (wid, location, available_car_p, available_time, company_id) values (1, '(26.0,26.0)', 'some1', '8-20', 1);
insert into public.workshops (wid, location, available_car_p, available_time, company_id) values (2, '(26.0,76.0)', 'some2', '6-20', 1);
insert into public.workshops (wid, location, available_car_p, available_time, company_id) values (3, '(76.0,26.0)', 'some3', '4-20', 1);
insert into public.workshops (wid, location, available_car_p, available_time, company_id) values (4, '(76.0,76.0)', 'some4', '3-20', 1);
