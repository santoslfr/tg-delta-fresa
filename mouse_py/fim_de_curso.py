# -*- coding: utf-8 -*-

def fim_de_curso(dados_mouse):
    
    sensor = [0,0,0]
    
    sensor[0]=(dados_mouse['mouse_a'][2] >> 2 ) & 0b00000001
    sensor[1]=(dados_mouse['mouse_b'][2] >> 2 ) & 0b00000001
    sensor[2]=(dados_mouse['mouse_c'][2] >> 2 ) & 0b00000001
    
    return sensor


