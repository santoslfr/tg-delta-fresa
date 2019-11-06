function [P_cent,P_abs] = inter_ret(R,T,P_ref)

% calcula a intersecção de duas retas coplanares

P_abs = zeros(size(P_ref));

%P_abs = (R*(P_ref') + T)';

for i=1:4

P_abs(i,:) = ((R')*(P_ref(i,:)') - T)';

end

x1 = P_abs(1,1);
y1 = P_abs(1,2);
x2 = P_abs(3,1);
y2 = P_abs(3,2);
x3 = P_abs(2,1);
y3 = P_abs(2,2);
x4 = P_abs(4,1);
y4 = P_abs(4,2);

P_cent=zeros(1,2);

P_cent(1,1) = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4))/((x1 - x2)*(y3 -y4) - (y1 - y2)*(x3 - x4));
P_cent(1,2) = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4))/((x1 - x2)*(y3 -y4) - (y1 - y2)*(x3 - x4));