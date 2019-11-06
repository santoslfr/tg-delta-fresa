function [pr] = fusao_sensores(delta_x_mi,delta_y_mi,x_ta,y_ta,theta_ta,theta_mi,r_mi)

% variação da posição e orientação do robô (u)

u = [delta_xr;
     delta_yr;
     delta_thetar];
     
% erro na variação da posição e orientação do robô : ruido do sistema (wt)

wt = [ wt_x;
       wt_y;
       wt_theta];

% A. Modelo do Sistema : dinamica do deslocamento da base 
% a partir das medições do mouse
       
% posição e orientação do robô : vetor de estado (Xt)

Xt = [ xt;
       yt;
       thetat];

% xt+1 = ft(xt,yt,thetat)

xt_1 = xt + (delta_xr + wt_x)*cos(thetat) - (delta_yr + wt_y)*sin(thetat);
yt_1 = yt + (delta_xr + wt_x)*sin(thetat) + (delta_yr + wt_y)*cos(thetat);
thetat_1 = thetat + delta_thetar + wt_theta;

% Q : matriz de covariância do ruido do sitema, wt.
% sigma_w: desvio padrão na variação dos valores medidos pelo sensor do mouse

sigma_t_wx = 0;
sigma_t_wy = 0;
sigma_t_wz = 0;

Qt = diag([ sigma_t_wx^2 sigma_t_wy^2 sigma_t_wz^2]);

% B. Modelo de observação (medição)
% Equação de observação da posição do centro do robô

% zt = Ht*Xt + vt

zt = [ xtc;
       ytc];

Ht = [ 1 0 0;
       0 1 0];
       
% vt : ruido na observação causado pelo erro de quantização da imagem e demais ruidos.
       
vt = [ vtx;
       vty];

% Rt : matriz de covariância do ruido na observação
% sigma_v : desvio padrão dos erros de observação da posição do centro do robô

sigma_t_vx = 0;
sigma_t_vy = 0;

Rt = diag([ sigma_t_vx^2 sigma_t_vy^2 ]);

% C. Integração com o uso do Filtro de Kalmam dos dois valores estimados

% A equação do modelo do sistema, xt+1 = ft(xt,yt,thetat), é uma linearização
% ao redor da medição, ut. Além disso, assumindo que o ruido do sistema ,wt,
% e o ruido da observação , vt, tem média zero, as matrizes de covariância
% Qt(wt) e Rt(vt) são ruido branco e não possuem correlação entre si.

% Algoritimo de estimação


