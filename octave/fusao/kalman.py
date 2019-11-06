# -*- coding: utf-8 -*-
import numpy as np

def kalman(delta_xr,delta_yr,delta_thetar,x_ta,y_ta,theta_ta,xtc,ytc,thetac,P_ta):

    # algoritimo de estimação : Filtro de Kalman
    
    # pre : predição ( com base nas medições dos mouses )
    # at : atualização ( com base na medição da câmera )
    # ta : "tempo atual" da atualização anterior
    
    # Xt = ft(xt,yt,thetat) : vetor de estado da posição do robô
    # ut : variação da posição e orientação do robô detectada pelos mouses
    # Qt(wt) : matriz de covariância do ruido do sitema.
    # wt : ruido na variação da posição e orientação do robô : ruido da medição dos mouses
    # Pt : matriz de covariância do filtro de kalman.
    # Rt(vt) : matriz de covariância do ruido na observação
    # vt : ruido na observação causado pelo erro de quantização da imagem e demais ruidos : ruido na medição da câmera
    # zt : posição do centro do robô determinada pela câmera
    
    wt_x = 2 #[mm]
    wt_y = 2 #[mm]
    wt_theta = 1.7*10**-2 # [rad]
    
    wt = np.array([[wt_x],
                   [wt_y],
                   [wt_theta]])
    
    vtx = 2   #[mm]
    vty = 2   #[mm]
    vtt = 0.2 #[rad]
    
    vt = np.array([[vtx],
                   [vty],
                   [vtt]])

    # Rt = np.diag(np.array([ sigma_t_vx^2 , sigma_t_vy^2 , sigma_t_vt^2]))
    
    Rt = wt@(wt.transpose())
    
    # Qt = np.diag(np.array([ sigma_t_wx^2 , sigma_t_wy^2 , sigma_t_wz^2]))
    
    Qt = vt@(wt.transpose())
    
    Ht = np.array([[1 , 0 , 0],
                   [0 , 1 , 0],
                   [0 , 0 , 1]])
    
    zt = np.array([xtc,
                   ytc,
                   thetac])
           
    Ft = np.array([[1 , 0 , -delta_xr*np.sin(theta_ta) - delta_yr*np.cos(theta_ta)],
                   [0 , 1 ,  delta_xr*np.cos(theta_ta) - delta_yr*np.sin(theta_ta)],
                   [0 , 1 ,  0                                                    ]])
        
    Gt = np.array([[np.cos(theta_ta) ,-np.sin(theta_ta) , 0],
                   [np.sin(theta_ta) , np.cos(theta_ta) , 0],
                   [0             , 0                   , 1]])
           
    ###########################################################################
    
    # Predição ( usa os dados do mouse )
    
    # X_pre = ft(X_ta, ut, 0 )
    # P_pre = Ft*P_ta*(Ft)' + Gt*Qt*(Gt)'
    
    # Ganho de Kalman
    
    # Kt = P_pre*(Ht')*(Ht*P_pre*(Ht') + Rt)^-1;
    
    # Atualização ( usa os dados da câmera )
    
    # X_at = X_pre + Kt*(zt - Ht*X_pre);
    # P_at = P_pre - Kt*Ht*P_pre
    
    ###########################################################################
    
    # Predição ( usa os dados do mouse )
    
    x_pre = x_ta + delta_xr*np.cos(theta_ta) - delta_yr*np.sin(theta_ta)
    y_pre = y_ta + delta_xr*np.sin(theta_ta) + delta_yr*np.cos(theta_ta)
    theta_pre = theta_ta + delta_thetar
    
    X_pre =np.array([[x_pre],
                     [y_pre],
                     [theta_pre]])
               
    P_pre = Ft@P_ta@(Ft.transpose()) + Gt@Qt@(Gt.transpose())
    
    # Ganho de Kalman
    
    Kt = P_pre@(Ht.transpose())@(Ht@P_pre@(Ht.transpose()) + Rt)**-1
    
    # Atualização ( usa os dados da câmera )
    
    X_at = X_pre + Kt@(zt - Ht@X_pre)
    P_at = P_pre - Kt@Ht@P_pre
    
    x_at = X_at[0,0]
    y_at = X_at[1,0]
    theta_at = X_at[2,0]
    
    return x_at,y_at,theta_at,P_at