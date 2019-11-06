function [P] = mapeamento_2d_3d(q,r_i)

% Recebe como parametros os pontos q e distancias r_i e retorna os pontos P

P = zeros(4,3);

for i = 1:4
for j = 1:3

P(i,j) = (q(i,j)/(( q(i,1)^2 + q(i,2)^2 + q(i,3)^2 )^(1/2)))*r_i(i,1);

end
end