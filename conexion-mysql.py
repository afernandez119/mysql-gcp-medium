###0. Librerías

import pandas as pd
import sqlalchemy

#!pip install mysql-connector #Eliminar comentario en caso de no tener instalada esta librería. No es necesario importarla


###1. Conexión a BBDD¶

db_username = 'externo' #Usuario externo que hemos creado
db_password = 'Password_123456' #Contraseña del usuario externo
db_ip = '35.230.152.204' #IP externa de la instancia
db_name = 'noticias'

s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)

engine = sqlalchemy.create_engine(s)

print(engine.table_names())


###2. Inserción de datos en la BBDD

#Creamos unos datos dummy para incorporar a la tabla 'noticias_financieras'

news = {"titulo":['Santander se dispara el 6%',
                  'El mapa de la nueva Unicaja-Liberbank'],
        "texto":['El banco toma el relevo de Telefónica en un rally con ciertos paralelismos con el logrado ayer por la teleco. Acelera su salida de mínimos en Bolsa, y también cuenta con el respaldo de las firmas de inversión. Barclays destaca que "hay valoraciones difíciles de ignorar" en la banca, y elige a Santander como uno de sus tres bancos europeos favoritos, con un espectacular potencial alcista.',
                 'El \'matrimonio\' entre Unicaja y Liberbank daría lugar a un banco con 1.633 oficinas repartidas por toda la península. El mayor número de sucursales se localiza en Andalucía, donde Unicaja tiene su sede.']    
}

#Convertimos a un DF de pandas
news_df = pd.DataFrame(news)
news_df

###2.1. Inserción de noticias en la tabla noticias_financieras

#Hacemos uso de la función ".to_sql" de pandas:
news_df.to_sql(con=engine, name='noticias_financieras', if_exists='append',index=False)


###2.2. Consulta a la tabla noticias_financieras

#Ejecutamos la consulta a la BBDD. ATENCIÓN: no se debería utilizar fetchall puesto que nos traerá todos los datos de la tabla

engine.execute('SELECT * FROM noticias_financieras').fetchall()

#Si queremos convertir la consulta a un DF de pandas:

news_df2 = pd.read_sql('SELECT * FROM noticias_financieras LIMIT 10', engine)
news_df2


