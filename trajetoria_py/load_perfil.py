# -*- coding: utf-8 -*-
import scipy.io as sio

arquivo = 'perfil.mat'

def load_perfil(arquivo):
    
    mat_contents = sio.loadmat(arquivo)
    perfil = mat_contents['pc']
    
    return perfil
