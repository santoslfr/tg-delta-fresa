function [q] = rastreamento_pontos(q_temp,p1,p2,p3,p4,f)

% garante a ordem em que cada ponto do plano da imagem adquirida pelo sensor é representado

% pkg load statistics deve ser carragada no main

q = zeros(size(q_temp));

q1 = [p1,f]; %pixel
q2 = [p2,f]; %pixel
q3 = [p3,f]; %pixel
q4 = [p4,f]; %pixel

q_temp2 = [ q1;
            q2;
            q3;
            q4];

n = size(q_temp,1);

dist = zeros(n,n);

for i=1:n
for j=1:n

dist(i,j)= pdist([q_temp(i,:);q_temp2(j,:)],"euclidean");

end
end

for i=1:n

[min_v , min_j] = min(dist(i,:));

q(i,:) = q_temp2(min_j,:);

end
