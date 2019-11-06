pkg load statistics

clear
close all
clc

f = 1280; % distancia focal
c = [ 0 0 0 ];
% pontos do marcador : 4 pontos não coplanares

Pm = [ 10  5  20;
      -10  10  20;
       10 -10  20;
      -10 -10 24];

% distancia entre os pontos do marcador

n=size(Pm,1);

d_ij = zeros(n,n);

for i=1:n
for j=1:n

d_ij(i,j)= pdist([Pm(i,:);Pm(j,:)],"euclidean");

end
end

rs = zeros(n,1);

for i=1:n

rs(i,1)= pdist([c;Pm(i,:)],"euclidean");

end

% pontos do marcador - sistema de referencia da camera

% PC = [ 3.4596   -4.9873   11.5560;
%        9.8314   12.6564   20.1058;
%       -8.8868   -8.5328   19.3016;
%       -4.4042    5.8636   33.0366];

PC = [ 3.4596  -4.9873  110.5560;
       9.8314  12.6564  200.1058;
      -8.8868  -8.5328  190.3016;
      -4.4042   5.8636  330.0366];


% pontos no plano da imagem

Pim = zeros(size(PC));

for i =1:4

Pim(i,:) = [ ((-f*PC(i,1))/PC(i,3)) ((-f*PC(i,2))/PC(i,3)) f];

end

[c_tetha_ij] = cosseno_entre_raios(Pim);
[r_i,j,erro] = distancia_ri(c_tetha_ij,d_ij);
[P] = mapeamento_2d_3d(Pim,r_i);
[R,T] = posicao_absoluta_v2(P,Pm);
[P_cent,P_abs] = inter_ret(R,T,Pm);
%
%figure(1)
%
%hold on
%scatter3(Pm(:,1),Pm(:,2),Pm(:,3),'r') % pontos do marcador - vermelho
%scatter3(Pim(:,1),Pim(:,2),Pim(:,3) ,'g') % pontos no plano da imagem - verde
%scatter3(P(:,1),P(:,2),P(:,3),'c') % pontos 3d sistema de camera - cyan
%scatter3(0,0,0,'b') % ponto focal - preto
%
%Pim_g = ((R')*(Pim'- repmat(T,1,size(Pim',2))))';
%P_g = ((R')*(P'- repmat(T,1,size(P',2))))';
%C = ((R')*([0;0;0] - T))';
%
%figure(2)
%
%hold on
%scatter3(Pm(:,1),Pm(:,2),Pm(:,3),'r') % pontos do marcador - vermelho
%scatter3(Pim_g(:,1),Pim_g(:,2),Pim_g(:,3) ,'g') % pontos no plano da imagem - verde
%scatter3(P_g(:,1),P_g(:,2),P_g(:,3),'c') % pontos 3d sistema de camera - cyan
%scatter3(C(:,1),C(:,2),C(:,3),'b') % ponto focal - preto


%scatter3(P_abs(:,1),P_abs(:,2),P_abs(:,3) ,'m') % ponto 3d - magenta
%scatter3(P_cent(1,1),P_cent(1,2),0,'k') % centro 3d