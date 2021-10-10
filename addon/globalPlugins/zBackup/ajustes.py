# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

import addonHandler
import globalVars
import os
import sys
import wx

# For translation
addonHandler.initTranslation()

# Bandera ventana principal del complemento. Para saber si esta abierta.
IS_WinON = False
# Nuevos id para botones de dialogo
ID_TRUE = wx.NewIdRef() # para botón aceptar
ID_FALSE = wx.NewIdRef() # para botón cancelar
# Variable unidad de sistema
unidadSistema = os.environ['SYSTEMDRIVE']
# Variable para la ubicación de Drive Snapshot y url para descargar
dirPath = os.path.join(os.path.dirname(__file__), "Snapshot")
if os.path.exists(os.environ['PROGRAMFILES(X86)']): # 64 Bits
	dirSnapshot = os.path.join(os.path.dirname(__file__), "Snapshot", "snapshot64.exe")
	urlSnapshot = "http://www.drivesnapshot.de/download/snapshot64.exe"
else: # 32 Bits
	dirSnapshot = os.path.join(os.path.dirname(__file__), "Snapshot", "snapshot.exe")
	urlSnapshot = "http://www.drivesnapshot.de/download/snapshot.exe"
# Variable fichero log error
ficheroLog =os.path.join(globalVars.appArgs.configPath, "zBackupLog_error.txt")
# Variable tamaño ficheros copia seguridad y diccionario
sizeFicheros = 2
dictLenght = {
	0:500,
	1:1000,
	2:1500,
	3:2000,
	4:2500,
	5:5000,
	6:10000,
}
