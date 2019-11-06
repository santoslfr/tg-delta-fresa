# -*- coding: utf-8 -*-
#import time

def ler_mouse(ser):
    
    #leitura = str()
    #resposta = str()
    #dados = str()
    
    ser.flushInput()
    
    ser.write(b'l')
    
#    time.sleep(0.003)
#    
#    while ser.in_waiting == 0: # envia a requisição de leitura até obter uma resposta
#    
#        ser.write(b'l') # requisição de leitura de dados dos mouses
    
    leitura = ser.read()
    
    resposta = leitura
    
    #while ser.in_waiting != 0: #leitura != b'\r': # le a resposta até o caracter de final de menssagem : '\r'
    while leitura != b'\r': # le a resposta até o caracter de final de menssagem : '\r'
        
        leitura = ser.read()
    
        resposta += leitura
    
    dados = resposta.split(b';')
    
    # formato dados:
    
    # [delta_xa;delta_ya;botões_a;delta_xb;delta_yb;botões_b;delta_xc;delta_yc;botões_c;'\r']
    
    dados_mouse = {'mouse_a':[float(dados[0]),float(dados[1]),int(dados[2])],
                   'mouse_b':[float(dados[3]),float(dados[4]),int(dados[5])],
                   'mouse_c':[float(dados[6]),float(dados[7]),int(dados[8])]}
    
    return dados_mouse
    #return resposta