function [p1, p2, p3, p4] = aquisicao_imagem(cop,P_ref,f)

%% pontos informados pela camera
%
%p1_x = 803 ; %pixel
%p1_y = 420 ; %pixel
%p2_x = 822 ; %pixel
%p2_y = 302 ; %pixel
%p3_x = 215 ; %pixel
%p3_y = 347 ; %pixel
%p4_x = 191 ; %pixel
%p4_y = 266 ; %pixel
%
%% pontos no sistema de coordenadas do modelo câmera pinhole
%
%% 1024x768 : resolução da câmera
%
%%cop = (512,384)
%
%p1 = [p1_x - cop(1,1),p1_y - cop(1,2)];
%p2 = [p2_x - cop(1,1),p2_y - cop(1,2)];
%p3 = [p3_x - cop(1,1),p3_y - cop(1,2)];
%p4 = [p4_x - cop(1,1),p4_y - cop(1,2)];
%
%%p1 = [p1_x ,p1_y];
%%p2 = [p2_x ,p2_y];
%%p3 = [p3_x ,p3_y];
%%p4 = [p4_x ,p4_y];

Pim = zeros(size(P_ref));

for i =1:4

Pim(i,:) = [ ((-f*P_ref(i,1))/P_ref(i,3)) ((-f*P_ref(i,2))/P_ref(i,3)) f];

end

p1 = Pim(1,:);
p2 = Pim(2,:);
p3 = Pim(3,:);
p4 = Pim(4,:);