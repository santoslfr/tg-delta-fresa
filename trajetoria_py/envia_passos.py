# -*- coding: utf-8 -*-
import numpy as np

def envia_passos(passos,ser):
    
    #ser.write(b'a') # avisa o arduino que serão enviados passos
    resposta = 0
    i = 0
    
    l = np.zeros((np.size(passos,0),2))
    l = l.astype(int)
    passos = np.packbits(np.concatenate((l,passos),axis=1)) # completa a sequência com duas coluna nulas
          
    while(i <= (passos.size -1)):
                       
        #solicitacao = chr(ord(ser.read()))
               
        ser.write(b'a')
        
        if(passos[i] ==0 ):
            
            g='À' # B11000000
            g.encode('latin-1')            
            ser.write(g.encode('latin-1'))
        
        else:
        
            ser.write(chr(passos[i]).encode())
            
        i = i + 1
        
        while(resposta != b'e'):
            
            resposta = ser.read()
            print("aguardado")
        
        resposta = 0
    #resposta = ser.read()

    #g='À'
    #g.encode('latin-1')
    #bin(192).encode()
    #ser.write(g.encode('latin-1')) # avisa o arduino do fim de envio dos passos
    
    #ser.close()
    
def reset(passos,ser):
    
    ser.write(b'r') # inicializa o reset do robô para a posição inicial
    
    resposta = 0
    
    while(resposta != b'p'):
    
        resposta = ser.read()
        
#        if(resposta != b'p'):
#            
#            ser.write(b'p')
            
    print("enviar passos")
    
    envia_passos(passos,ser) # envia os passos para posicionar a fresa sobre a peça
    
    #ser.close()
