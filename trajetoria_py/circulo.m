% curva que define o perfil da peça

dep = 10^-4; % distancia entre pontos [m]
ra = 0.45; % resolução ângular do motor em graus

% circulo

theta = 0:2*pi()/720:2*pi();
theta = theta';
r =0.01;
x = r*cos(theta);
y = r*sin(theta);
z = 0.11*ones(size(x));

pc =[x,y,z];

pc = [pc;pc(1,:)];

%deslocamento horizontal

xi = 0;
yi = 0;
xf = pc(1,1);
yf = pc(1,2);

if xf != xi

% distancia entre os pontos

d = ((xf - xi)^2 + (yf - yi)^2)^0.5 ;

% coeficiente angular

m = ((yf - yi)/(xf - xi));

% segmentos:

n = ceil(d/(dep));

% y = m*x

o = [1:1:n]';

ph =[(xf/n)*o,(xf/n)*o*m,pc(1,3)*ones(n,1)];

else

ph = [ 0 , 0 , pv(size(v,1),3)];

end

p=[ph;pc;pc;pc;pc];

%geração dos passos

pd = Ajuste_distancia_pontos(p,dep);

for j = 1:1:size(pd,1);

[Phi_m(j,:),p_m(j,:)] = Ajuste_dos_Pontos(pd(j,:)',ra);

end

passos = Pontos_para_Passos(Phi_m,ra);

save('Passos_Motor_circulo','passos')

%plot3(p(:,1),p(:,2),p(:,3),"color",'r',"marker",'*')
%plot3(pd(:,1),pd(:,2),pd(:,3),"color",'g',"marker",'*')
%plot3(p_m(:,1),p_m(:,2),p_m(:,3),"color",'g',"marker",'*')