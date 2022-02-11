# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import globalVars
import config
import gui
import ui
from scriptHandler import script
import winsound
from threading import Thread
import wx
import os
import sys
import shutil
import subprocess
import urllib.request
import socket
import time
from . import ajustes
from . import utilidades

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		if globalVars.appArgs.secure: return

	# Translators: Description for name in input gesture window
	@script(gesture=None, description= _("Mostrar ventana principal"), category= "zBackup")
	def script_Run(self, gesture):
		if config.isInstalledCopy():
			if ajustes.IS_WinON == False:
				if os.path.isfile(ajustes.dirSnapshot):
					self.mainThread = HiloComplemento(1)
					self.mainThread.start()
				else:
					self.mainThread = HiloComplemento(2)
					self.mainThread.start()
			else:
				# Translators: Message informing that a copy of the plug-in has already been opened
				ui.message(_("Ya hay una instancia de zBackup para NVDA abierta."))
		else:
			# Translators: Message informing that it is not possible to run on a portable copy of NVDA
			ui.message(_("No se puede ejecutar zBackup en una copia portable de NVDA."))

class HiloComplemento(Thread):
	def __init__(self, opcion):
		super(HiloComplemento, self).__init__()

		self.opcion = opcion
		self.daemon = True

	def run(self):
		def lanzaApp():
			self.windowsApp = VentanaPrincipal(gui.mainFrame)
			gui.mainFrame.prePopup()
			self.windowsApp.Show()

		def lanzaDescargaInicio():
			ajustes.IS_WinON = True
			# Translators: Message to inform about snapshot information and that it is to be downloaded
			xguiMsg = \
_("""No se encontró Drive Snapshot.

Es necesario descargar la aplicación para poder usar el complemento.

La aplicación es portable y se guardara en el directorio del complemento:

{}

Su peso es inferior a 500KB.

Le recuerdo que la aplicación es de evaluación por 30 días, es recomendable ver la ayuda del complemento.

¿Desea descargar la aplicación ahora para poder usar el complemento?""").format(ajustes.dirSnapshot)
			msg = wx.MessageDialog(None, xguiMsg, 
				# Translators: Title of the dialog box that will ask about snapshot downloading
				_("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				dlg = DescargaDialogoInicio()
				result = dlg.ShowModal()
				if result == ajustes.ID_TRUE:
					dlg.Destroy()
					ajustes.IS_WinON = False
					wx.CallAfter(lanzaApp)
				else:
					dlg.Destroy()
					ajustes.IS_WinON = False
			else:
				msg.Destroy()
				ajustes.IS_WinON = False
				return

		if self.opcion == 1:
			wx.CallAfter(lanzaApp)
		if self.opcion == 2:
			wx.CallAfter(lanzaDescargaInicio)

class DescargaDialogoInicio(wx.Dialog):
	def __init__(self):

		WIDTH = 550
		HEIGHT = 400

		# Translators: Snapshot download window title
		super(DescargaDialogoInicio, self).__init__(None, -1, title=_("Descargando Drive Snapshot..."), size = (WIDTH, HEIGHT))

		self.CenterOnScreen()

		self.Panel = wx.Panel(self)

		self.progressBar=wx.Gauge(self.Panel, wx.ID_ANY, range=100, style = wx.GA_HORIZONTAL)
		self.textorefresco = wx.TextCtrl(self.Panel, wx.ID_ANY, style =wx.TE_MULTILINE|wx.TE_READONLY)
		self.textorefresco.Bind(wx.EVT_CONTEXT_MENU, self.skip)

		# Translators: Accept button name
		self.AceptarTRUE = wx.Button(self.Panel, ajustes.ID_TRUE, _("&Aceptar"))
		self.Bind(wx.EVT_BUTTON, self.onAceptarTRUE, id=self.AceptarTRUE.GetId())
		self.AceptarTRUE.Disable()

		# Translators: Name of close button
		self.AceptarFALSE = wx.Button(self.Panel, ajustes.ID_FALSE, _("&Cerrar"))
		self.Bind(wx.EVT_BUTTON, self.onAceptarFALSE, id=self.AceptarFALSE.GetId())
		self.AceptarFALSE.Disable()

		self.Bind(wx.EVT_CLOSE, self.onNull)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer_botones = wx.BoxSizer(wx.HORIZONTAL)

		sizer.Add(self.progressBar, 0, wx.EXPAND)
		sizer.Add(self.textorefresco, 1, wx.EXPAND)

		sizer_botones.Add(self.AceptarTRUE, 2, wx.CENTER)
		sizer_botones.Add(self.AceptarFALSE, 2, wx.CENTER)

		sizer.Add(sizer_botones, 0, wx.EXPAND)

		self.Panel.SetSizer(sizer)

		self.textorefresco.SetFocus()
		HiloDescarga(self)

	def skip(self, event):
		return

	def onNull(self, event):
		pass

	def next(self, event):
		self.progressBar.SetValue(event)

	def TextoRefresco(self, event):
		self.textorefresco.Clear()
		self.textorefresco.AppendText(event)

	def done(self, event):
		winsound.MessageBeep(0)
		self.AceptarTRUE.Enable()
		self.textorefresco.Clear()
		self.textorefresco.AppendText(event)
		self.textorefresco.SetInsertionPoint(0) 
		self.AceptarTRUE.SetFocus()

	def error(self, event):
		winsound.MessageBeep(16)
		self.AceptarFALSE.Enable()
		self.textorefresco.Clear()
		self.textorefresco.AppendText(event)
		self.textorefresco.SetInsertionPoint(0) 
		self.AceptarFALSE.SetFocus()

	def onAceptarTRUE(self, event):
		if self.IsModal():
			self.EndModal(event.EventObject.Id)
		else:
			self.Close()

	def onAceptarFALSE(self, event):
		if self.IsModal():
			self.EndModal(event.EventObject.Id)
		else:
			self.Close()

class HiloDescarga(Thread):
	def __init__(self, frame):
		super(HiloDescarga, self).__init__()

		self.frame = frame
		self.url = ajustes.urlSnapshot

		self.dirPath=ajustes.dirPath
		if os.path.exists(self.dirPath) == False:
			os.mkdir(self.dirPath)
		self.tiempo = 30

		self.daemon = True
		self.start()

	def __call__(self, block_num, block_size, total_size):
		readsofar = block_num * block_size
		if total_size > 0:
			percent = readsofar * 1e2 / total_size
			wx.CallAfter(self.frame.next, percent)
			time.sleep(1 / 995)
			wx.CallAfter(self.frame.TextoRefresco, _("Espere por favor...\n") + _("Descargando: %s") % utilidades.humanbytes(readsofar))
			if readsofar >= total_size: # Si queremos hacer algo cuando la descarga termina.
				pass
		else: # Si la descarga es solo el tamaño
			wx.CallAfter(self.frame.TextoRefresco, _("Espere por favor...\n") + _("Descargando: %s") % utilidades.humanbytes(readsofar))

	def run(self):
		try:
			socket.setdefaulttimeout(self.tiempo) # Dara error si pasan 30 seg sin internet
			try:
				req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
				obj = urllib.request.urlopen(req).geturl()
				urllib.request.urlretrieve(obj, ajustes.dirSnapshot, reporthook=self.__call__)
			except Exception as e:
				urllib.request.urlretrieve(self.url, ajustes.dirSnapshot, reporthook=self.__call__)

			wx.CallAfter(self.frame.done, _("La descarga se completó.\n") + _("Ya puede cerrar esta ventana."))
		except Exception as e:
			wx.CallAfter(self.frame.error, _("Algo salió mal.\n") + _("Compruebe que tiene conexión a internet y vuelva a intentarlo.\n") + _("Ya puede cerrar esta ventana."))

			try:
				shutil.rmtree(ajustes.dirPath, ignore_errors=True)
			except:
				pass

class VentanaPrincipal(wx.Dialog):
	def __init__(self, parent):

		WIDTH = 550
		HEIGHT = 300

		super(VentanaPrincipal, self).__init__(parent, -1, size = (WIDTH, HEIGHT))

		ajustes.IS_WinON = True
		self.SetTitle(_("zBackup para NVDA"))

		self.directorioDestino = ""

		self.panel_1 = wx.Panel(self, wx.ID_ANY)

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("&Directorio destino:"))
		sizer_1.Add(label_1, 0, wx.EXPAND, 0)

		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

		self.txtDirectorio = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_NO_VSCROLL)
		sizer_2.Add(self.txtDirectorio, 0, wx.EXPAND, 0)
		self.directorioBTN = wx.Button(self.panel_1, wx.ID_ANY, _("&Seleccionar directorio"))
		sizer_2.Add(self.directorioBTN, 1, wx.ALL |wx.ALIGN_CENTER_VERTICAL, 0)

		label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, _("&Nombre para la copia de seguridad"))
		sizer_1.Add(label_2, 0, wx.EXPAND, 0)

		self.txtNombre = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
		sizer_1.Add(self.txtNombre, 0, wx.EXPAND, 0)

		label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Seleccione el &tamaño para los archivos de la copia:"))
		sizer_1.Add(label_3, 0, wx.EXPAND, 0)

		self.listLenght = ["500 MB", "1 GB", "1.5 GB", "2 GB", "2.5 GB", "5 GB", "10 GB"]
		self.choice = wx.Choice(self.panel_1, 2, choices=self.listLenght)
		self.choice.SetSelection(ajustes.sizeFicheros)
		sizer_1.Add(self.choice, 0, wx.EXPAND, 0)

		sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

		self.copiaBTN = wx.Button(self.panel_1, wx.ID_ANY, _("&Iniciar la copia de seguridad"))
		sizer_3.Add(self.copiaBTN, 2, wx.EXPAND / wx.CENTER, 0)

		self.menuBTN = wx.Button(self.panel_1, wx.ID_ANY, _("&Menú"))
		sizer_3.Add(self.menuBTN, 2, wx.CENTER, 0)

		self.panel_1.SetSizer(sizer_1)

		self.Layout()

		self.CenterOnScreen()
		self.cargaEventos()

	def cargaEventos(self):
		self.txtDirectorio.Bind(wx.EVT_CONTEXT_MENU, self.skip)
		self.txtNombre.Bind(wx.EVT_CONTEXT_MENU, self.skip)
		self.directorioBTN.Bind(wx.EVT_BUTTON, self.onSeleccionarDirectorio)
		self.choice.Bind(wx.EVT_CHOICE, self.onChoice)
		self.copiaBTN.Bind(wx.EVT_BUTTON, self.onIniciaCopia)
		self.menuBTN.Bind(wx.EVT_BUTTON,self.menuBoton)

		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyEscape)
		self.Bind(wx.EVT_CLOSE, self.onSalir)

	def skip(self, event):
		return

	def onChoice(self, event):
		ajustes.sizeFicheros = event.GetSelection()

	def menuBoton(self, event):
		self.menu = wx.Menu()
		item1 = self.menu.Append(1, _("&Restaurar copia de seguridad"))
		self.menu.Bind(wx.EVT_MENU, self.onMenuAcciones)
		item2 = self.menu.Append(2, _("&Montar disco virtual de una copia de seguridad"))
		self.menu.Bind(wx.EVT_MENU, self.onMenuAcciones)
		item3 = self.menu.Append(3, _("&Desmontar unidades virtuales"))
		self.menu.Bind(wx.EVT_MENU, self.onMenuAcciones)
		item4 = self.menu.Append(4, _("&Ejecutar la aplicación Drive Snapshot"))
		self.menu.Bind(wx.EVT_MENU, self.onMenuAcciones)
		self.menuBTN.PopupMenu(self.menu)

	def onMenuAcciones(self, event):
		menuID = event.GetId()
		if menuID == 1:
			msg = \
_("""*** ADVERTENCIA ***

A continuación se le va a pedir que elija un archivo *.sna que pertenece a una copia de seguridad.

Cuando lo seleccione se le pedirá permisos de administrador, el ordenador se reiniciara y se restaurara la copia de seguridad.

Después de pedirle permisos de Administrador quedara una ventana de consola la cual cuando presionemos cualquier tecla se reiniciara y dará comienzo la copia de seguridad.

Es conveniente que tenga todas las aplicaciones cerradas o cuando Windows se lo solicite le diga finalizar todo.

Tenga en cuenta que el proceso no puede cancelarse y si acepta debe mantener el ordenador con batería suficiente, mejor enchufado a la corriente eléctrica y esperar a que Windows se reinicie ya con la copia restaurada.

Es conveniente tener en la pantalla de inicio de Windows activado el lector de pantalla para que nos avise que inicio.

La acción que transcurre entre el reinicio siguiente y el inicio de Windows no es accesible, pero no tiene que interactuar para nada con el ordenador.

Si lo desea y tiene alguna aplicación móvil de OCR puede ir mirando de capturar alguna información que le indique el porcentaje de la restauración, sobre la esquina inferior derecha suele aparecer el porcentaje que lleva restaurado.

Le recuerdo que el autor del complemento queda exento de cualquier problema que pueda causar una mala restauración.

¿Desea continuar?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				wildcard = _("Archivo copia de seguridad (*.sna)|*.sna")
				dlgF = wx.FileDialog(None, message=_("Seleccione un archivo de copia de seguridad"), defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
				if dlgF.ShowModal() == wx.ID_OK:
					copiaFichero = dlgF.GetPath()
					dlgF.Destroy()
					if  ajustes.unidadSistema == copiaFichero[:2]:
						msg = \
_("""No puede restaurar una copia de seguridad desde la partición de sistema.

Mueva la copia de seguridad a otra partición o un medio externo.""")
						gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
						return
					else:
						HiloRestauracion(copiaFichero)
						self.Destroy()
						gui.mainFrame.postPopup()
				else:
					dlgF.Destroy()

			else:
				msg.Destroy()

		if menuID == 2:
			dlg = DialogoMontar()
			result = dlg.ShowModal()
			if result == ajustes.ID_TRUE:
				dlg.Destroy()
				datos = [dlg.unidadSeleccionada, dlg.ficheroSeleccion]
				HiloMontar(datos)
				self.Destroy()
				gui.mainFrame.postPopup()
			else:
				dlg.Destroy()

		if menuID == 3:
			msg = \
_("""Se va a proceder a desmontar todas las unidades virtuales.

Se le pedirá permisos de Administrador para realizar la acción.

¿Desea continuar?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				HiloDesmontar()
				self.Destroy()
				gui.mainFrame.postPopup()
			else:
				msg.Destroy()

		if menuID == 4:
			os.startfile(os.path.realpath(ajustes.dirSnapshot))

	def onSeleccionarDirectorio(self, event):
		dlg = wx.DirDialog(self, _("Seleccione un directorio:"),
			style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			if  ajustes.unidadSistema == dlg.GetPath()[:2]:
				msg = \
_("""No puede guardar la copia de seguridad en la ubicación que eligió.

{}

La copia de seguridad tiene que guardarse en una ubicación distinta a la partición de sistema ya sea otra partición u otro disco.""").format(dlg.GetPath())
				gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
				self.txtDirectorio.Clear()
				self.directorioDestino = ""
			else:
				total_src, used_src, free_src = shutil.disk_usage(ajustes.unidadSistema + "\\")
				total_dest, used_dst, free_dst = shutil.disk_usage(dlg.GetPath()[:3])
				if free_dst < used_src:
					msg = \
_("""La ubicación que eligió no tiene espacio suficiente para guardar la copia de seguridad.

{}

La comprobación del tamaño se hace del total de la partición de sistema.

Al hacer la copia de seguridad luego se comprime y queda la mitad aproximadamente, pero es necesario reservar el tamaño original para imprevistos de compresión.

* Tamaño partición sistema: {}
* Tamaño libre destino: {}

Por favor elija otra ubicación con más espacio o si tiene copias de seguridad antiguas borre alguna.""").format(dlg.GetPath(), utilidades.humanbytes(used_src), utilidades.humanbytes(free_dst))
					gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
					self.txtDirectorio.Clear()
					self.directorioDestino = ""
				else:
					self.txtDirectorio.SetValue(dlg.GetPath())
					self.directorioDestino =dlg.GetPath()
		dlg.Destroy()

	def onIniciaCopia(self, event):
		if self.txtDirectorio.GetValue() == "":
			msg = \
_("""El campo del directorio está vacío.

Este campo es obligatorio ya que será donde se guarde la copia de seguridad.

Seleccione un directorio para poder continuar.""")
			gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
			self.directorioBTN.SetFocus()
		else:
			if self.txtNombre.GetValue() == "":
				msg = \
_("""El campo de nombre para la copia de seguridad  es obligatorio.

Dicho campo es necesario para crear el subdirectorio y la estructura de archivos en.

{}

Además este campo nos valdrá para identificar nuestra copia de seguridad.

Introduzca un nombre para poder continuar.""").format(self.txtDirectorio.GetValue())
				gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
				self.txtNombre.SetFocus()
			else:
				if any(c in ' \/:*?"<>|' for c in self.txtNombre.GetValue()):
					msg = \
_("""El nombre para la copia de seguridad contiene caracteres no permitidos.

Los siguientes caracteres no pueden ser usados, utilice una revisión virtual para verlos:

\ / : * ? " < > |

Además por seguridad en las restauraciones se a omitido el poder poner espacios por lo que le recomiendo los sustituya por guiones o guiones bajos.

Modifique el Nombre para la copia de seguridad para continuar.""")
					gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
					self.txtNombre.SetFocus()
				else:
					msg = \
_("""A continuación se le solicitara permisos de Administrador para poder hacer la copia de seguridad.

Una vez concedidos se abrirá una ventana con el progreso de la copia.

Cuando el proceso termine se cerrara la ventana y le saldrá información si la copia fue exitosa o no.

¿Desea empezar la copia de seguridad?""")
					msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
					ret = msg.ShowModal()
					if ret == wx.ID_YES:
						msg.Destroy()
						temporal = [self.directorioDestino, self.txtNombre.GetValue()]
						HiloCopia(temporal)
						self.Destroy()
						gui.mainFrame.postPopup()
					else:
						msg.Destroy()
						return

	def onKeyEscape(self, event):
		if event.GetUnicodeKey() == wx.WXK_ESCAPE:
			ajustes.IS_WinON = False
			self.Destroy()
			gui.mainFrame.postPopup()
		else:
			event.Skip()

	def onSalir(self, event):
		ajustes.IS_WinON = False
		self.Destroy()
		gui.mainFrame.postPopup()

class DialogoMontar(wx.Dialog):
	def __init__(self):

		WIDTH = 700
		HEIGHT = 350

		super(DialogoMontar, self).__init__(None, -1, size = (WIDTH, HEIGHT))

		self.SetTitle(_("Montar imagen de copia de seguridad como unidad virtual"))
		self.unidadSeleccionada = ""
		self.ficheroSeleccion = ""

		self.panel_1 = wx.Panel(self, wx.ID_ANY)

		sizer_1 = wx.BoxSizer(wx.VERTICAL)

		self.unidades = utilidades.unidadesLibres(":")
		label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Seleccione una &unidad de disco donde montar la imagen:"))
		sizer_1.Add(label_1, 0, wx.EXPAND, 0)
		self.choice = wx.Choice(self.panel_1, wx.ID_ANY, choices=["Elija unidad"]+self.unidades)
		self.choice.SetSelection(0)
		sizer_1.Add(self.choice, 0, wx.EXPAND, 0)

		label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, _("Seleccione un archivo &de copia de seguridad:"))
		sizer_1.Add(label_2, 0, wx.EXPAND, 0)

		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

		self.txtFichero = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_NO_VSCROLL)
		sizer_2.Add(self.txtFichero, 1, wx.EXPAND, 0)
		self.ficheroBTN = wx.Button(self.panel_1, wx.ID_ANY, _("&Seleccionar copia de seguridad"))
		sizer_2.Add(self.ficheroBTN, 0, wx.ALL |wx.ALIGN_CENTER_VERTICAL, 0)

		sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

		self.aceptarBTN = wx.Button(self.panel_1, 1, _("&Aceptar"))
		sizer_3.Add(self.aceptarBTN, 2, wx.CENTER, 0)

		self.cancelarBTN = wx.Button(self.panel_1, 2, _("&Cancelar"))
		sizer_3.Add(self.cancelarBTN, 2, wx.CENTER, 0)

		self.panel_1.SetSizer(sizer_1)

		self.Layout()
		self.CenterOnScreen()
		self.cargaEventos()

	def cargaEventos(self):
		self.choice.Bind(wx.EVT_CHOICE, self.onChoice)
		self.Bind(wx.EVT_BUTTON, self.onBotones)
		self.ficheroBTN.Bind(wx.EVT_BUTTON, self.onSeleccionarFichero)

		self.Bind(wx.EVT_CHAR_HOOK, self.on_keyVentanaDialogo)
		self.Bind(wx.EVT_CLOSE, self.onCerrar)

	def onChoice(self, event):
		choiceID = event.GetSelection()
		if choiceID == 0:
			self.unidadSeleccionada = ""
		else:
			self.unidadSeleccionada = self.unidades[event.GetSelection()-1]

	def onBotones(self, event):
		botonID = event.GetId()
		if botonID == 1:
			if self.choice.GetSelection() == 0:
				msg = \
_("""Tiene que seleccionar una unidad para poder continuar""")
				gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
				self.choice.SetFocus()
			else:
				if self.txtFichero.GetValue() == "":
					msg = \
_("""El campo del fichero de copia de seguridad está vacío.

Este campo es obligatorio ya que es necesario tener la ruta de una copia de seguridad para montar.

Seleccione un fichero para poder continuar.""")
					gui.messageBox(msg, _("Error"), wx.ICON_ERROR)
					self.ficheroBTN.SetFocus()
				else:
					if self.IsModal():
						self.EndModal(ajustes.ID_TRUE)
					else:
						self.Close()
		if botonID == 2:
			if self.IsModal():
				self.EndModal(ajustes.ID_FALSE)
			else:
				self.Close()

	def onSeleccionarFichero(self, event):
		wildcard = _("Archivo copia de seguridad (*.sna)|*.sna")
		dlgF = wx.FileDialog(None, message=_("Seleccione un archivo de copia de seguridad"), defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
		if dlgF.ShowModal() == wx.ID_OK:
			self.ficheroSeleccion = dlgF.GetPath()
			self.txtFichero.SetValue(os.path.basename(self.ficheroSeleccion))
			dlgF.Destroy()

	def on_keyVentanaDialogo(self, event):
		if event.GetKeyCode() == 27: # Pulsamos ESC y cerramos la ventana
			if self.IsModal():
				self.EndModal(ajustes.ID_FALSE)
			else:
				self.Close()
		else:
			event.Skip()

	def onCerrar(self, event):
		if self.IsModal():
			self.EndModal(ajustes.ID_FALSE)
		else:
			self.Close()

class HiloCopia(Thread):
	def __init__(self, opciones):
		super(HiloCopia, self).__init__()

		self.opciones = opciones
		self.daemon = True
		self.start()

	def run(self):
		cmd = '"{}" {} "{}" -L{} --CreateDir --LogFile:"{}" -Gx'.format(ajustes.dirSnapshot, ajustes.unidadSistema, os.path.join(self.opciones[0], self.opciones[1], self.opciones[1]), ajustes.dictLenght.get(ajustes.sizeFicheros), ajustes.ficheroLog)
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		cmdOutput = []
		with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='CP437', startupinfo=si, creationflags = 0x08000000, universal_newlines=True, shell = True) as proc:
			for line in proc.stdout:
				cmdOutput.append(line)
		if proc.returncode == 0:
			msg = \
_("""Se completo la copia de seguridad correctamente en la ubicación:

{}

Le aconsejo guarde correctamente dicho directorio por si necesitara restaurar.""").format(os.path.join(self.opciones[0], self.opciones[1]))
			gui.messageBox(msg,_("Información"), wx.ICON_INFORMATION)
		else:
			try:
				shutil.rmtree(os.path.join(self.opciones[0], self.opciones[1]), ignore_errors=True)
			except:
				pass

			winsound.MessageBeep(16)
			msg = \
_("""Algo salió mal. Al usar una aplicación externa no puedo dar más información del error.

Pero se guardo un log para que pueda revisarlo.

¿Desea ver el log de error?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				try:
					with open(ajustes.ficheroLog, 'r') as f:
						txt = "".join(line for line in f if not line.isspace())
					ui.browseableMessage(txt, _("Log de error"))
				except:
					ui.browseableMessage(''.join(str(e) for e in cmdOutput), _("Log de error"))
			else:
				msg.Destroy()

		ajustes.IS_WinON = False

		try:
			os.remove(ajustes.ficheroLog)
		except:
			pass

class HiloRestauracion(Thread):
	def __init__(self, opciones):
		super(HiloRestauracion, self).__init__()

		self.opciones = opciones
		self.daemon = True
		self.start()

	def run(self):
		cmd = '"{}" --autoreboot:any --Schedule {} "{}"'.format(ajustes.dirSnapshot, ajustes.unidadSistema, self.opciones)
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		cmdOutput = []
		with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='CP437', startupinfo=si, creationflags = 0x08000000, universal_newlines=True, shell = True) as proc:
			for line in proc.stdout:
				cmdOutput.append(line)
		if proc.returncode == 0:
			os.system("shutdown -t 0 -r -f")
		else:
			winsound.MessageBeep(16)
			msg = \
_("""Algo salió mal. Al usar una aplicación externa no puedo dar más información del error.

Pero se guardo un log para que pueda revisarlo.

¿Desea ver el log de error?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				ui.browseableMessage(''.join(str(e) for e in cmdOutput), _("Log de error"))
			else:
				msg.Destroy()

		ajustes.IS_WinON = False

class HiloMontar(Thread):
	def __init__(self, opciones):
		super(HiloMontar, self).__init__()

		self.opciones = opciones
		self.daemon = True
		self.start()

	def run(self):
		cmd = 'start {} "{}" {} -VQ'.format(ajustes.dirSnapshot, self.opciones[1], self.opciones[0])
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		cmdOutput = []
		with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='CP437', startupinfo=si, creationflags = 0x08000000, universal_newlines=True, shell = True) as proc:
			for line in proc.stdout:
				cmdOutput.append(line)
		if proc.returncode == 0:
			msg = \
_("""Se monto correctamente la imagen.

¿Desea abrir el explorador de archivos en la raíz de la unidad {}?""").format(self.opciones[0])
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				os.startfile(os.path.realpath(self.opciones[0]))
			else:
				msg.Destroy()

		else:
			winsound.MessageBeep(16)
			msg = \
_("""Algo salió mal. Al usar una aplicación externa no puedo dar más información del error.

Pero se guardo un log para que pueda revisarlo.

¿Desea ver el log de error?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				ui.browseableMessage(''.join(str(e) for e in cmdOutput), _("Log de error"))
			else:
				msg.Destroy()

		ajustes.IS_WinON = False

class HiloDesmontar(Thread):
	def __init__(self):
		super(HiloDesmontar, self).__init__()

		self.daemon = True
		self.start()

	def run(self):
		cmd = 'start {} -!unmount'.format(ajustes.dirSnapshot)
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		cmdOutput = []
		with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='CP437', startupinfo=si, creationflags = 0x08000000, universal_newlines=True, shell = True) as proc:
			for line in proc.stdout:
				cmdOutput.append(line)
		if proc.returncode == 0:
			msg = \
_("""Se desmontaron correctamente todas las imágenes.""")
			gui.messageBox(msg,_("Información"), wx.ICON_INFORMATION)
		else:
			winsound.MessageBeep(16)
			msg = \
_("""Algo salió mal. Al usar una aplicación externa no puedo dar más información del error.

Pero se guardo un log para que pueda revisarlo.

¿Desea ver el log de error?""")
			msg = wx.MessageDialog(None, msg, _("Pregunta"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			ret = msg.ShowModal()
			if ret == wx.ID_YES:
				msg.Destroy()
				ui.browseableMessage(''.join(str(e) for e in cmdOutput), _("Log de error"))
			else:
				msg.Destroy()

		ajustes.IS_WinON = False
