% Ler coordendas dos pontos da camera do wiimote
clear
close all
clc

pkg load statistics % para ter acesso a função de cáculo de distancia entre pontos


[f, d_ij, P_ref, cop] = parametros_base();
[p1, p2, p3, p4] = aquisicao_imagem(cop,P_ref,f);
[q_temp] = pareamento_pontos(p1,p2,p3,p4,f);
[q] = rastreamento_pontos(q_temp,p1,p2,p3,p4,f);
[c_tetha_ij] = cosseno_entre_raios(q);
[r_i] = distancia_ri(c_tetha_ij,d_ij);
[P] = mapeamento_2d_3d(q,r_i);
[R,T] = posicao_absoluta(P,P_ref);
[P_cent,P_abs] = inter_ret(R,T,P_ref)

hold on
scatter3(q(:,1),q(:,2),q(:,3),'r')
scatter3(P_ref(:,1),P_ref(:,2),P_ref(:,3),'g')
scatter3(P_abs(:,1),P_abs(:,2),P_abs(:,3),'b')

%scatter3(q(:,1),q(:,2),q(:,3))

%p1_x = 803 ; %pixel
%p1_y = 420 ; %pixel
%p2_x = 822 ; %pixel
%p2_y = 302 ; %pixel
%p3_x = 215 ; %pixel
%p3_y = 347 ; %pixel
%p4_x = 191 ; %pixel
%p4_y = 266 ; %pixel
%
%p1 = [p1_x ,p1_y];
%p2 = [p2_x ,p2_y];
%p3 = [p3_x ,p3_y];
%p4 = [p4_x ,p4_y];
%
%p = [p1;p2;p3;p4];
%plot(p(:,1),p(:,2))

%acosd(c_tetha_ij)