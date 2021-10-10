# Manual de zBackup para NVDA.

zBackup nos permitirá hacer copias de seguridad de la partición que contenga el sistema operativo.

Esto significa que el disco o partición que contenga la instalación de Windows se podrá guardar para poder ser restaurada.

zBackup puede hacer las copias de seguridad en caliente sin necesidad de detener aplicaciones o dejar de hacer lo que estemos haciendo.

Este complemento se basa en la aplicación Drive Snapshot:

http://www.drivesnapshot.de/en/index.htm

zBackup viene a simplificar las acciones comunes y necesarias para que podamos hacer una copia de seguridad y podamos restaurarla sin necesidad de ayuda ni de herramientas externas como WinPE.

Además de poder hacer copias de seguridad podremos restaurar dichas copias, podremos montar dichas copias como unidades virtuales y todo de manera accesible.

zBackup se basa en Drive SnapShot  por lo que usa una aplicación externa a NVDA dicha aplicación pesa menos de 500 KB y será descargada de la pagina oficial cuando iniciemos el complemento por primera vez. Decir que en cada actualización del complemento de zBackup la aplicación será descargada de su página para tener siempre la última versión.

Decir que Drive SnapShot no es una aplicación gratuita y tiene sus limitaciones.

Drive SnapShot nos permitirá usar la aplicación durante 30 días aproximadamente en su totalidad pero pasado ese tiempo lo único que no dejara es seguir haciendo copias de seguridad, si restaurarlas y montarlas.

En la página de la aplicación podremos comprar Drive SnapShot por 39€ en su licencia más básica suficiente para uso personal.

Si se compra la licencia hay que tener en cuenta que tenemos que tener amano y bien guardada dicha licencia ya que como he comentado cada vez que actualicemos zBackup al descargarse una versión actualizada de la aplicación tendremos que registrarla para tener tiempo ilimitado.

## *** Información muy importante ***

zBackup a sido probado en distintos entornos, situaciones y a sido exitoso su comportamiento.

Pero en el mundo de la informática todo puede pasar y algo puede fallar por lo que es un complemento solo aconsejado a personas con conocimientos suficientes para poder salir de una mala restauración del sistema, esto supone saber arrancar desde otro medio para poder recuperar la información, saber instalar el sistema operativo, en definitiva si algo saliera mal el poder volver a tener Windows.

Al usar el complemento automáticamente el usuario es el único responsable de los resultados excluyendo al autor de la aplicación y del complemento de cualquier problema que se pudiera producir en cuanto a una mala restauración, mala copia de seguridad, perdida de datos parcial o completa, en definitiva el usuario es el único responsable del resultado final del uso de dicho paquete.

##*** Advertencia para un buen uso ***

zBackup trae ya protecciones para evitar cometer errores como restaurar desde la misma partición de Windows, utilizar símbolos no permitidos en los nombres de las copias, protección para la falta de espacio, etc. Pero hay que tener unas consideraciones a tener en cuenta.

Las copias de seguridad solo serán posible restaurarlas desde una partición o disco diferente a la de Windows. Las copias igualmente pueden ser restauradas desde medios externos pero tendremos que tener en consideración la velocidad de lectura de dichos medios. Un medio lento puede causar problemas al restaurar por lo que se recomiendan discos externos SSD o algún método de almacenamiento usb pero de alta velocidad enchufados a TIPO C.

Bien tenemos que tener en cuenta que si hacemos una copia de seguridad en modo no seguro de la BIOS podremos restaurar dicha copia mientras estemos en ese modo. Si cambiamos a modo seguro la copia echa en modo no seguro ya no se podrá restaurar, esto sucede al revés cada copia tiene que ser restaurada con el hardware correspondiente y la configuración de hardware correspondiente.

Igualmente es recomendable no usar zBackups para hacer copias de seguridad de discos protegidos con BitLocker.

zBackup a sido probado en Windows 10 y 11 pero es válido para Windows 7 y 8 según documentación de la aplicación.

Se recomienda que el directorio donde guardemos las copias de seguridad no contengan espacios.

zBackup no podrá ser usado desde copias portables de NVDA.

# Interface de zBackup

zBackup pretende tener pocas opciones y ser clara por lo que en todo momento nos dará mensajes de información de lo que va hacer y pasos a seguir.

En la pantalla principal es donde podremos hacer la copia de seguridad.

Para lanzar la pantalla principal es necesario añadir un gesto en NVDA / Preferencias / Gestos de entrada... y buscar zBackup y añadir una combinación de teclas.

Una vez abierta caeremos en un cuadro de solo lectura el cual contendrá el directorio donde guardaremos la copia de seguridad, si tabulamos caeremos en el botón Seleccionar directorio el cual nos permitirá seleccionar dicho directorio.

En esta carpeta se guardaran en subdirectorios las copias de seguridad, es recomendable que esta carpeta no tenga espacios.

Si tabulamos de nuevo caeremos en un cuadro de escritura llamado Nombre para la copia de seguridad, en este cuadro pondremos el nombre identificativo de nuestra copia de seguridad.

En este cuadro no se permiten ni espacios ni caracteres no permitidos por Windows en carpetas y archivos, dichos caracteres son los siguientes comprendidos entre las comillas triples:

“””\ / : * ? " < > |”””

Bien este nombre identificativo creara un directorio dentro del directorio destino de la copia con el nombre que elijamos y dentro de este directorio los archivos de la copia tendrán también este nombre.

Si volvemos a tabular caeremos en un cuadro combinado donde podremos elegir el tamaño de cada archivo de la copia de seguridad, podremos elegir entre 500 mb a 10 GB.

Esto significa que al hacer la copia de seguridad los archivos resultantes tendrán ese tamaño. Para poner un ejemplo si nuestra partición de Windows tiene un tamaño de 60 GB aproximadamente la copia resultante tendrá un tamaño total de unos 20 a 30 GB. Si elegimos que los archivos resultantes sean de 10 GB creara aproximadamente 3 archivos.

Si tabulamos caeremos en el botón Iniciar la copia de seguridad si todos los datos están bien rellenados y se cumplen las condiciones de espacio y de ubicación nos dará la posibilidad de iniciar la copia de seguridad indicando que va hacer en todo momento.

Si volvemos a tabular caeremos en el botón Menú el cual si lo pulsamos se nos desplegara un menú contextual con las siguientes opciones:

* Restaurar copia de seguridad: Con esta opción podremos restaurar una copia de seguridad y nos ira orientando con mensajes, tener en cuenta que una vez llegado al punto de elegir la imagen a restaurar una vez elegida y aceptada el proceso ya no tiene vuelta atrás y se restaurara el sistema.

* Montar disco virtual de una copia de seguridad: Con esta opción tendremos posibilidad de elegir una unidad libre de nuestro ordenador y montar virtualmente una copia, esto va bien por si tenemos algo especifico que queramos recuperar de una copia y no deseamos restaurar por completo.

* Desmontar unidades virtuales: Esta opción desmontara todas las unidades virtuales que hayamos montado con zBackup cuando digo todas es que si tenemos 3 montadas se desmontaran todas no es posible elegir una a una. Esta opción se ejecutara satisfactoriamente aunque no tengamos ninguna montada ya que hará la comprobación aun sin tener ninguna montada.

* Ejecutar la aplicación Drive Snapshot: Con esta opción lanzaremos Drive Snapshot y podremos usar la aplicación en su manera interface también podremos registrar con el serial la aplicación.

Decir que todo tiene atajos de teclado los cuales se informan conforme recorremos la interface.

## Otros

Al hacer una copia de seguridad es necesario en la partición o disco destino tener el tamaño de la partición de sistema, si la partición de sistema tiene 60 GB es necesario tener libre 60 GB en la de destino aunque luego la copia ocupe la mitad o menos esto es por seguridad.

Es recomendable tener un medio de arranque por si algo saliera mal, se recomienda un WinPE y Drive Snapshot en dicho medio, de esa manera podríamos recuperar desde la copia de seguridad el sistema.

zBackup a sido probado en Windows sin modificar por lo que en Windows modificados de esos que hay por la red no garantizo su funcionamiento.

Vuelvo a advertir que zBackup no sea usado si no se tienen los conocimientos para salir de una mala restauración.

## Problemas encontrados

E probado el complemento en varios ordenadores y con distinto hardware y configuración además de en máquinas virtuales.

Decir que cuando arranca para restaurar podemos tener como algo orientativo que los ventiladores del ordenador se ponen a trabajar y se paran cuando termina la restauración, igualmente si tenemos auriculares enchufados con los chasquidos en los auriculares podemos detectar los reinicios.

E detectado que en modo seguro a veces una vez restaurada la copia de seguridad no arranca y se queda en el logo del fabricante.

Bien en esos casos es conveniente esperar unos minutos y apagar el ordenador.

La próxima vez que iniciemos nos preguntara si queremos hacer una comprobación del disco o directamente a veces empezara dicha comprobación dando como resultado una pantalla inaccesible la cual nos dice que probemos otra opción para recuperar o que apaguemos el ordenador.

Bien si damos a intro se apagara y la próxima vez que iniciemos el ordenador ya se iniciara en Windows.

Esto es la protección del modo seguro que hila muy fino pero realmente la restauración se hizo correctamente.

Igualmente a veces arranca en Windows y cuando ya iniciamos la sesión nos sale una notificación con que tenemos que reiniciar para reparar los errores, si reiniciamos y esperamos unos segundos volveremos a Windows ya sin ningún problema.

Como digo esto me a sucedido alguna vez siendo una minoría de veces pero puede suceder por lo que no hay que tener miedo pero si saber que se hace. No obstante sigue vigente el aviso de tener otro medio de recuperación por si acaso y tener en cuenta que hay cientos de máquinas, configuraciones y puede que lo que si funcione en una en otra no.

Hoy en día solemos tener en nuestros móviles una aplicación de reconocimiento OCR, es muy recomendable hacer uso de ella para saber en las pantallas no accesibles que está sucediendo.

Por lo que es responsabilidad de cada uno usar o no el complemento.

Repito que el autor de la aplicación y del complemento quedan exentos de cualquier problema ocasionado por el complemento.
