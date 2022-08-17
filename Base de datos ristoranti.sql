create database ristoranti;

create table cliente(
dni int(8) not null primary key,
nombre varchar(20) not null ,
apellido varchar(20) not null,
telefono int(10) not null);

create table reserva(
dni int(8) not null,
id_reserva int(4) not null primary key,
dia date not null,
hora time not null,
cantidad_comensales int(2) not null,
foreign key (dni) references cliente (dni) 
);

