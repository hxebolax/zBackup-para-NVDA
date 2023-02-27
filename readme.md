# Manual de zBackup para NVDA.

zBackup nos permitirá hacer copias de seguridad de la partición que contenga el sistema operativo.

Esto significa que el disco o partición que contenga la instalación de Windows se podrá guardar para poder ser restaurada.

zBackup puede hacer las copias de seguridad en caliente sin necesidad de detener aplicaciones o dejar de hacer lo que estemos haciendo.

[Este complemento se basa en la aplicación Drive Snapshot.](http://www.drivesnapshot.de/en/index.htm)

zBackup viene a simplificar las acciones comunes y necesarias para que podamos hacer una copia de seguridad y restaurarla sin necesidad de ayuda ni de herramientas externas, como WinPE.

Además de hacer copias de seguridad, podremos restaurar dichas copias, montarlas como unidades virtuales, y todo ello de manera accesible.

zBackup se basa en Drive Snapshot, por lo que usa una aplicación externa a NVDA. Dicha aplicación pesa menos de 500 KB y será descargada de la página oficial cuando iniciemos el complemento por primera vez. En cada actualización del complemento de zBackup, la aplicación será descargada de su página para tener siempre la última versión.

Drive SnapShot no es una aplicación gratuita y tiene sus limitaciones. La aplicación se puede usar durante 30 días en su totalidad, pero pasado ese tiempo lo único que no dejará es seguir haciendo copias de seguridad, aunque sí restaurarlas y montarlas.

En la página de la aplicación podremos comprar Drive SnapShot por 39 euros en su licencia más básica, suficiente para uso personal.

Si se compra la licencia, hay que tener en cuenta que debemos tenerla a mano y bien guardada, ya que cada vez que actualicemos zBackup, al descargarse una versión actualizada de la aplicación, tendremos que registrarla para tener tiempo ilimitado.

## *** Información muy importante ***

zBackup ha sido probado en distintos entornos y situaciones con excelentes resultados. Sin embargo, en el mundo de la informática todo puede pasar, y puede haber fallos, por lo que es un complemento sólo aconsejable a personas con conocimientos suficientes para poder salir de una mala restauración del sistema. Esto supone saber arrancar desde otro medio para poder recuperar la información, instalar el sistema operativo y, en definitiva, poder volver a tener Windows si algo saliera mal.

Al usar el complemento, el usuario es el único responsable de los resultados, excluyendo al autor de la aplicación y del complemento de cualquier problema que se pudiera producir en cuanto a una mala restauración, copia de seguridad defectuosa, pérdida de datos parcial o completa, y en definitiva, el resultado final del uso de dicho paquete.

## *** Advertencia para un buen uso ***

zBackup incorpora protecciones para evitar cometer errores, como restaurar desde la misma partición de Windows, utilizar símbolos no permitidos en los nombres de las copias, protección para la falta de espacio, etc. Sin embargo, se deben tener en cuenta varias consideraciones.

Las copias de seguridad sólo podrán restaurarse desde una partición o disco diferente a la de Windows. Las copias igualmente pueden ser restauradas desde medios externos, pero tendremos que tener en consideración la velocidad de lectura de dichos medios. Un medio lento puede causar problemas al restaurar, por lo que se recomienda usar discos externos SSD o algún método de almacenamiento USB de alta velocidad tipo C.

Debemos tener en cuenta que si hacemos una copia de seguridad en modo no seguro de la BIOS, podremos restaurar dicha copia mientras estemos en ese modo. Si cambiamos a modo seguro, la copia hecha en modo no seguro ya no se podrá restaurar. Cada copia tiene que ser restaurada con el hardware correspondiente y la configuración de hardware correspondiente.

Igualmente, es recomendable no usar zBackup para hacer copias de seguridad de discos protegidos con BitLocker.

zBackup a sido probado en Windows 10 y 11, pero es válido en Windows 7 y 8 según la documentación de la aplicación.

Se recomienda que el directorio donde guardemos las copias de seguridad no contenga espacios.

zBackup no podrá ser usado desde copias portables de NVDA.

## Interfaz de zBackup

zBackup pretende tener pocas opciones y ser clara, por lo que en todo momento nos dará mensajes de información de lo que va a hacer y pasos a seguir.

Desde la pantalla principal podremos hacer la copia de seguridad.

Para lanzar la pantalla principal es necesario añadir un gesto en NVDA / Preferencias / Gestos de entrada / Categoría zBackup.

Una vez abierta, caeremos en un cuadro de sólo lectura que contendrá el directorio donde guardaremos la copia de seguridad. Si tabulamos, caeremos en el botón "Seleccionar directorio", el cuál nos permitirá seleccionar dicho directorio.

Las copias de seguridad se guardarán en subcarpetas dentro de este directorio. Es recomendable que esta carpeta no tenga espacios.

Si tabulamos de nuevo caeremos en un cuadro de edición llamado "Nombre para la copia de seguridad". En este cuadro pondremos el nombre identificativo de nuestra copia de seguridad.

En este cuadro no se permiten espacios ni caracteres no permitidos por Windows en carpetas y archivos. Dichos caracteres son los siguientes, comprendidos entre las comillas triples:

"""\ / : * ? » < > |"""

Este nombre identificativo servirá para nombrar la subcarpeta y los distintos archivos de la copia de seguridad.

Si volvemos a tabular, caeremos en un cuadro combinado donde podremos elegir el tamaño de cada archivo de la copia de seguridad. Podremos seleccionar de 500 mb a 10 GB.

Esto significa que al hacer la copia de seguridad, los archivos resultantes tendrán ese tamaño. Para poner un ejemplo: si nuestra partición de Windows tiene un tamaño de 60 GB aproximadamente, la copia resultante tendrá un tamaño total de unos 20 a 30 GB. Si elegimos que los archivos resultantes sean de 10 GB, creará aproximadamente 3 archivos.

Si tabulamos otra vez, caeremos en el botón "Iniciar la copia de seguridad". Si todos los datos están bien rellenados y se cumplen las condiciones de espacio y de ubicación, nos dará la posibilidad de iniciar la copia de seguridad, indicando que va a hacer en todo momento.

Si volvemos a tabular, caeremos en el botón "Menú". Si lo pulsamos, se desplegará un menú contextual con las siguientes opciones:

* Restaurar copia de seguridad: Con esta opción, podremos restaurar una copia de seguridad. Se nos irá orientando con mensajes. Es importante tener en cuenta que, una vez llegado al punto de elegir la imagen a restaurar y aceptarla, el proceso ya no tiene vuelta atrás y se restaurará el sistema.

* Montar disco virtual de una copia de seguridad: Con esta opción, tendremos la posibilidad de elegir una unidad libre de nuestro ordenador y montar virtualmente una copia. Esto va bien por si tenemos algo específico que queramos recuperar de una copia y no deseamos restaurar por completo.

* Desmontar unidades virtuales: Esta opción desmontará todas las unidades virtuales que hayamos montado con zBackup. No es posible elegir una a una. Esta opción se ejecutará satisfactoriamente aunque no tengamos ninguna montada.

* Ejecutar la aplicación Drive Snapshot: Con esta opción, lanzaremos Drive Snapshot y podremos usar la aplicación en su modo de interfaz gráfica. También podremos registrarla con el serial, en caso de haber adquirido una licencia.

Todos los controles tienen atajos de teclado, los cuáles se informan según recorremos la interfaz.

## Otros

Al hacer una copia de seguridad, es necesario que el disco o partición de destino tenga el tamaño de la partición del sistema. Si la partición de sistema tiene 60 GB, es necesario tener libre 60 GB en la de destino, aunque luego la copia ocupe la mitad o menos. Esto es por seguridad.

Es recomendable tener un medio de arranque por si algo saliera mal. Se recomienda un WinPE y Drive Snapshot en dicho medio. De esa manera, podríamos recuperar desde la copia de seguridad el sistema.

zBackup a sido probado en Windows sin modificar. No se garantiza un buen funcionamiento en ciertas versiones de Windows modificadas que circulan por Internet.

Vuelvo a advertir que zBackup no sea usado si no se tienen los conocimientos para poder salir de una mala restauración.

## Problemas encontrados

El complemento ha sido probado en varios ordenadores con distinto hardware y configuración, además de en máquinas virtuales.

Cuando arranca para restaurar, podemos tener como algo orientativo que los ventiladores del ordenador se ponen a trabajar y se paran cuando termina la restauración. Igualmente, si tenemos auriculares enchufados, con los chasquidos en los auriculares podemos detectar los reinicios.

En modo seguro, a veces, una vez restaurada la copia de seguridad, el sistema no arranca y se queda en el logo del fabricante.

En esos casos, es conveniente esperar unos minutos y apagar el ordenador.

La próxima vez que iniciemos, Windows nos preguntará si queremos hacer una comprobación del disco o empezará dicha comprobación por sí mismo, dando como resultado una pantalla inaccesible que nos dice que probemos otra opción para recuperar o que apaguemos el ordenador.

Si pulsamos Intro, se apagará. La próxima vez que arranquemos el ordenador, se iniciará en Windows.

Esto es la protección del modo seguro, que hila muy fino, pero en realidad la restauración se hizo correctamente.

Igualmente, a veces arranca en Windows, y cuando ya iniciamos la sesión aparece una notificación indicando que tenemos que reiniciar para reparar los errores. Si reiniciamos y esperamos unos segundos volveremos a Windows, ya sin ningún problema.

Durante las pruebas, esto a sucedido alguna vez, siendo una minoría de veces. No obstante, puede suceder, por lo que se debe saber que se hace. Sigue vigente el aviso de tener otro medio de recuperación por si acaso, y entender que hay cientos de máquinas, configuraciones y puede que lo que funcione en una, no lo haga en otra.

Hoy en día, solemos tener en nuestros móviles una aplicación de reconocimiento OCR. Es muy recomendable hacer uso de ella para saber qué está sucediendo en las pantallas no accesibles.

Tal y como se recordó anteriormente, el autor de la aplicación y del complemento quedan exentos de toda responsabilidad por cualquier problema ocasionado por el complemento o el programa.