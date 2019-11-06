function [l1,l2,a,b,d_externo,d_interno,d,alfa,mp,m1,m2,g,I_motor] = delta_parametros_prototipo

% parâmetros do robô

% dimensões

l1=0.057;%[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
l2=0.075;%[m] : comprimento do antebraço / distância entre a junta do cotovelo
a=0.080;%[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
b=0.070;%[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
d_externo = 0.013;%[m] : diametro da barra externa do link distal
d_interno = 0.013;%[m] : diametro da barra interna do link distal
d = 0.116;%[m] : distância entre as juntas rotulares j1 e j2
alfa = [ 0 ; 120*2*pi()/360 ; 240*2*pi()/360];%[rad] :ângulo entre os braços : 0º, 120º e 240°

% massa

mp=2.500; %[kg] : massa do end-effector
m1=0.650; %[kg] : massa do link proximal
m2=0.375; %[kg] : massa do link

% vetor gravidade

g = [0   ;% x
     0   ;% y
     -9.8];%z 

% motor

I_motor=1; % momento de inercia do motor

end
