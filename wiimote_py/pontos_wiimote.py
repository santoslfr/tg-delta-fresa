# -*- coding: utf-8 -*-
def pontos_wiimote(wm,cop):
    
    import numpy as np
    posicao = wm.state['ir_src'] # lê os dados do sensor ir na lista state
    
    # formato do lista :
    
    # [{'pos': (x1, y1), 'size': s1}, {'pos': (x2, y2), 'size': s2}
    #, {'pos': (x3, y3), 'size': s3}, {'pos': (x4, y4), 'size': s4}]
    
    # a lista é formada por quatro elementos, cada elemento é um dicionário com dois componentes
    # o primeniro 'pos' é um par ordenado com as coordenadas da "bolha" ir no plano da imagem
    # o segundo, size , dá o tamanho (em pixels ?) da "bolha"
    
    
    # Se algum dado não está disponivel ele é definido como "None"
    
    # [{'pos': (x1, y1), 'size': s1}, {'pos': (x2, y2), 'size': s2}
    #, {'pos': (x3, y3), 'size': s3}, None]
    
    # sempre são necessários os quatro pontos para uso na determinação com a técnica P4P

    
    if None in posicao:
        
        pontos = 0
    
    else:
            
        pontos = np.array([[posicao[0]['pos'][0] - cop[0] , posicao[0]['pos'][1] - cop[1] ],
                           [posicao[1]['pos'][0] - cop[0] , posicao[1]['pos'][1] - cop[1] ],
                           [posicao[2]['pos'][0] - cop[0] , posicao[2]['pos'][1] - cop[1] ],
                           [posicao[3]['pos'][0] - cop[0] , posicao[3]['pos'][1] - cop[1] ]])
    
    return pontos
    
  # b = [{'pos': (475, 281), 'size': 1}, {'pos': (560, 663), 'size': 1}, {'pos': (723, 134), 'size': 3}, None]

# =============================================================================
# dados = {'led': 1, 'ir_src': [{'pos': (475, 281), 'size': 1}, {'pos': (560, 663), 'size': 1}, {'pos': (723, 134), 'size': 3}, None], 'rpt_mode': 8, 'ext_type': 0, 'rumble': 0, 'error': 0, 'battery': 99}
#
# posicao = dados['ir_src']
#
#
# p1 = posicao[0]
# (x1,y1) = p1['pos']
#
#
# p2 = posicao[1]
# (x2,y2) = p2['pos']
#
#
# p3 = posicao[2]
# (x3,y3) = p3['pos']