function [q_temp] = pareamento_pontos(p1,p2,p3,p4,f)

% ordena cada ponto do plano da imagem adquirida pelo sensor 

%Pontos no plano da imagem : 3d ( sistema de referencia da camera )

q1 = [p1,f]; %pixel [x_max, y_max, f]
q2 = [p2,f]; %pixel [x_min, y_max, f]
q3 = [p3,f]; %pixel [x_max, y_min, f]
q4 = [p4,f]; %pixel [x_min, y_min, f]

q_temp = [ q1;
           q2;
           q3;
           q4];

q_temp = sortrows(q_temp,-2);
q_temp = [sortrows(q_temp(1:2,:),-1) ; sortrows(q_temp(3:4,:),-1)];
