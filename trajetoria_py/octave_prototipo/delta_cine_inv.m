function [Phi1,Phi2,ri,l1i,l2i] = delta_cine_inv(p,l1,l2,a,b,alfa)

% parâmetros do robô

% dimensões

% l1 : comprimento do braço / distância entre a junta do ombro e do cotovelo
% l2 : comprimento do antebraço / distância entre a junta do cotovelo
% a  : distância entre a origem do sistema de coordenadas da base e a junta do ombro
% b  : distância entre a origem do sistema de coordenadas do end-effector e a junta do pulso
% d_externo : diametro da barra externa do link distal
% d_interno : diametro da barra interna do link distal
% d  : distância entre as juntas rotulares j1 e j2
% alfa : %ângulo entre os braços : 0º, 120º e 240°

% parâmetros cinemáticos

% p : posição do end-effector
% p_linha  : variação da posição (velocidade)
% p_2linha : variação da velocidade (aceleração)

% variaveis
% obs.: Variaveis com o prefixo "L_" estão no sistema de coordenadas local de cada braço

L_ai = [a;0;0];
L_bi = [b;0;0];
L_ri = zeros(3,3);
Phi=zeros(3,3);
L_l1i=zeros(3,3);
L_l2i=zeros(3,3);
ai=zeros(3,3);
bi=zeros(3,3); 
l1i=zeros(3,3);
l2i=zeros(3,3);
ri=zeros(3,3);

% Ângulos Phi

%             ______________
%                | |   ||
%               OO=O    O ---->Xi
%             // //     |\\ ) Phi1i
%           //  //      |  \\
%         O==O //       |   \\
%          \ O===O      v    O-----
%           \ \  \      Zi  /v\) Phi1i
%            \  \  \       /Phi\
%             O==\  \     /  2i
%                O===O---O
%            ________________
%              ||   | | Yi||
%              OO   O=O--> O
%             //    |||    \\
%           //    Zi|V|     \\
%          //       | |      \\
%         O==O     O==O----  O=O
%          \  \   /  /Phi3i/ /
%           \  \ /  /    / /
%            \  \  /   / /
%             O==O=O ==O

% Vetores dos braços

%          O    X   ai
%           o--->---> 
%           |       |\
%           |       | \ l1i
%         Z V       |  \
%           |      |    V
%           |      |    /
%           |     |    /
%         P |  ri |   /
%           |     |  / l2i
%           |    |  /
%           |    | /
%           |    VV
%           V---->
%               bi


% Análise da Posição : cinemática inversa ( dada a posição do end-effector determinar os ângulos Phi1i )

for i=1:3       

L_ri(:,i) = [ -1*a + b + p(1,1)*cos(alfa(i,1)) + p(2,1)*sin(alfa(i,1));
            -1*p(1,1)*sin(alfa(i,1)) + p(2,1)*cos(alfa(i,1))        ;
            p(3,1)                                                  ];      
      
end     

for i=1:1:3          

Phi(3,i) = acos((-1*p(1,1)*sin(alfa(i,1)) + p(2,1)*cos(alfa(i,1)))/l2);

Phi(2,i) = acos((L_ri(1,i)^2 + L_ri(2,i)^2 + L_ri(3,i)^2 - l1^2 - l2^2)/(2*l1*l2*sin(Phi(3,i))));

Phi(1,i) = atan(-1*((-1*l1*L_ri(3,i) -1*l2*sin(Phi(3,i))*cos(Phi(2,i))*L_ri(3,i) + l2*sin(Phi(3,i))*sin(Phi(2,i))*L_ri(1,i))...
           /(l1*L_ri(1,i) +  l2*sin(Phi(3,i))*sin(Phi(2,i))*L_ri(3,i) + l2*sin(Phi(3,i))*cos(Phi(2,i))*L_ri(1,i ))));             
end  

for i=1:3         

L_l1i(:,i) = [ l1*cos(Phi(1,i)) ;
               0                ;
               l1*sin(Phi(1,i)) ];
        
L_l2i(:,i) = [ l2*sin(Phi(3,i))*cos(Phi(1,i) + Phi(2,i));
               l2*cos(Phi(3,i))                         ;
               l2*sin(Phi(3,i))*sin(Phi(1,i) + Phi(2,i))];
             
end  

%conferido consistencia

% ri = l1i + l2i

if abs(L_ri - [L_l1i + L_l2i]) < 10^-6

% transformação do sistema de coordenadas local ( braços ) para o sistema de coorddenadas global

T0i = [ 1 , 0 , 0 ;
       -0 , 1 , 0 ;
        0 , 0 , 1 ];
        
T0i(:,:,2) = [ -0.50000 ,  0.86603 , 0.00000 ;
               -0.86603 , -0.50000 , 0.00000 ;
                0.00000 ,  0.00000 , 1.00000 ];

T0i(:,:,3) = [-0.50000 , -0.86603 ,  0.00000 ;
               0.86603 , -0.50000 ,  0.00000 ;
               0.00000 ,  0.00000 ,  1.00000 ];

inv_T0i =[ 1 , -0 ,  -0 ;
          -0 ,  1  , -0 ;
           0 ,  0  , 1  ];

inv_T0i(:,:,2) = [ -0.50000 , -0.86603 , -0.00000 ;
                    0.86603 , -0.50000 , -0.00000 ;
                    0.00000 ,  0.00000 ,  1.00000 ];

inv_T0i(:,:,3) = [ -0.50000 ,  0.86603 , -0.00000 ;
                   -0.86603 , -0.50000 , -0.00000 ;
                    0.00000 ,  0.00000 ,  1.00000 ];

for i=1:3

%T0i(:,:,i) = [ cos(alfa(i,1))    , sin(alfa(i,1)) , 0 ;
%               -1*sin(alfa(i,1)) , cos(alfa(i,1)) , 0 ;
%               0                 , 0              , 1 ];
%   
%inv_T0i(:,:,i) = inv(T0i(:,:,i));

ai(:,i) = inv_T0i(:,:,i)*L_ai;
bi(:,i) = inv_T0i(:,:,i)*L_bi;
l1i(:,i)= inv_T0i(:,:,i)*L_l1i(:,i);
l2i(:,i)= inv_T0i(:,:,i)*L_l2i(:,i);
ri(:,i)= inv_T0i(:,:,i)*L_ri(:,i);

end

Phi1 = Phi(1,:);
Phi2 = Phi(2,:);

else

Phi1 = NaN;
Phi2 = NaN;

end
