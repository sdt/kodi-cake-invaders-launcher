import os
import xbmcaddon

__addon__ = xbmcaddon.Addon()
program = __addon__.getSetting('cake_invaders_path')
os.execlp(program, program)
