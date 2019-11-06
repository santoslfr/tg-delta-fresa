function [R,T] = posicao_absoluta_v2(P,P_ref)

% A partir dos pontos P no sistema de coordenadas da camera e os pontos P_ref
% do modelo do marcador no sistema de coordenadas absoluto achar a matriz de rotação
% R e de translação T que leva o modelo P_ref a uma posição equivalente a P no
% sistema de coordenadas absoluto

P = P';
P_ref = P_ref';

n = size(P,2); % numero de pontos em P
n_ref = size(P_ref,2); % numero de pontos em P_ref

% Passos dos algoritimo

% 1 : calcular P_m , P_ref_m , Q_m e Q_ref_m

P_m = (1/n)*sum(P,2); % ponto médio
P_ref_m = (1/n_ref)*sum(P_ref,2); % ponto médio
Q_m = P - repmat(P_m,1,n);
Q_ref_m = P_ref - repmat(P_ref_m,1,n_ref);

% 2 : Calcular a matriz H (3x3) :

H = zeros(3,3,n);

Q_ref_m
Q_m

for i=1:n

H(:,:,i) = Q_ref_m(:,i)*Q_m(:,i)';

end

H

H = sum(H,3)

% 3 : Achar a SDV de H

% Cálculo do Singular Value Decomposition (SVD) de H

[U, S, V] = svd(H);

% 4 : Calcular X

X = V*(U');

% 5 : Calcular det(X);

dtm = det(X);

if (round(dtm) == 1)

R = X;

else if (round(dtm) == -1)

if (round(S(1,1)) == 0)

R = [ -1*X(:,1) X(:,2) X(:,3) ];

elseif (round(S(2,2)) == 0) 

R = [ X(:,1) -1*X(:,2) X(:,3) ];

else (round(S(3,3)) == 0)

R = [ X(:,1) X(:,2) -1*X(:,3) ];
end

end
end

P_m

R

P_ref_m

X

T = P_m - R*P_ref_m;

U

S

V

dtm
