#!/bin/bash

echo 1- Se elimina cualquier tabla con el el nombre sgpdb de la base de datos

sudo -u postgres dropdb sgpdb

echo 2- Creacion de la base de datos

sudo -u postgres createdb sgpdb

echo 3- La base de datos se ha creado con exito
