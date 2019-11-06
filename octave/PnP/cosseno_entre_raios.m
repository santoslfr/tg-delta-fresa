function [c_tetha_ij] = cosseno_entre_raios(q)

% calcula o cosseno dos ângulos entre os raios que partem da origem do sistema de
% coordenadas da camera até os pontos do plano da imagem

% q : vetor linha com os pontos do plano da imagem : q1, q2, q3 ...

k=size(q,1); % tem que ser >=2 ( minimo de dois pontos )

% combinação entre pontos entre k, onde aij = aji
%a = factorial(k)/(factorial(2)*factorial(k-2)); % nmmero de ângulos

c_tetha_ij = zeros(k,k);

%for i = 1:k-1
%for j = i+1:k

for i = 1:k
for j = 1:k

c_tetha_ij(i,j) = dot(q(i,:),q(j,:))/(norm(q(i,:))*norm(q(j,:)));
c_tetha_ij(j,i) = c_tetha_ij(i,j);

%c_tetha_ij = [ 0          c_tetha_12 c_tetha_13 c_tetha_14;  %1
%               c_tetha_12 0          c_tetha_23 c_tetha_24;  %2
%               c_tetha_13 c_tetha_23 0          c_tetha_34;  %3
%               c_tetha_14 c_tetha_24 c_tetha_34 0         ]; %4        
end
end
