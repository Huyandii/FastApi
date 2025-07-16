# API con MYSQL.

    1 - Crear un bbdd MySQL llama upgrade-shop: Y crear la siguiente tabla
                products
                    id
                    title
                    price
                    quantity
                    status

    2 - "fastapi[standard]"
        python-dotenv
        mysql-connector-python

    3 - pip list y creais el fichero requirements.txt


## ENTIDAD USUARIOS:

    - Crear una tabla users en la base de datos. llenarla con 10 registros x
      -id: int
      -name: str
      -surname: str
      -age: int
      -email: str
      -fecha_registro: date => default now()
      -status: int -> Boolean
      -password: str
      -rol: ENUM('admin', 'user')
    
    - Crear ficheros routes, models y controllers especifico para users x
    - Models modelo de user sin id y con id x
    - Routes GET users/id => optener los datos de un usuarios 
            - PUT users/id => actualizar un usuario
            - DEL users/id => borrar un usuario

        - TODO: CASA HACER LA RUTA PARA OBTENER TODOS LOS USUARIOS => GETALL
        - TODO: CASA HACER LA RUTA PARA REGISTRAR UN USUARIO. => REGISTER => POST