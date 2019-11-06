# -*- coding: utf-8 -*-
def setup_wiimote():
    
    import cwiid
    import time
  
    print('Press 1+2 on your Wiimote now...')
    
    wm = cwiid.Wiimote() # cria uma istância do objeto wiimote
    
    time.sleep(1)
    
    wm.rpt_mode = cwiid.RPT_IR # define o modo de aquisição de dados para o sensor 
    
    return wm
