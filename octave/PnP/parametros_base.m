function [f, d_ij, P_ref, cop] = parametros_base()

%Parâmetros intrínsecos

f=1280; %distância focal

%Parâmetros do marcador

% cordenadas dos leds

% distancia entre os leds 

%d12= 70; %[mm]
%d13= 42; %[mm]
%d24= 42; %[mm]
%d34= 70; %[mm]
%d14= 80; %[mm]
%d23= 80; %[mm]
%
%       % 1   2   3   4
%d_ij = [ 1   d12 d13 d14;  %1
%         d12 1   d23 d24;  %2
%         d13 d23 1   d34;  %3
%         d14 d24 d34 1   ]; %4
%        
%% coordenadas dos leds ( modelo de referência ) versores: (-1,1,1)
%
%l1_ref = [d12/2 , d13/2 , 3]; %[mm]
%l2_ref = [-d12/2, d24/2 , 3];
%l3_ref = [d34/2 , -d14/2, 3];
%l4_ref = [-d34/2, -d24/2, 24

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% pontos do marcador( sistema de coordenadas do robô ) : 4 pontos não coplanares [mm]

P_ref = [35  20 420; # [mm] distancia eixo z medida a partir da base do robô
        -35  20 390;
         35 -20 390;
        -35 -20 390];

% distancia entre os pontos do marcador

n=size(P_ref,1);

d_ij = zeros(n,n);

for i=1:n
for j=1:n

d_ij(i,j)= pdist([P_ref(i,:);P_ref(j,:)],"euclidean");

end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%P_ref = [ l1_ref;
%          l2_ref;
%          l3_ref;
%          l4_ref ];
%          
% center of projection : cop

cop = [512 384];
