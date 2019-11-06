% trajetória básica

% váriaveis

dep = 10^-4; % distancia entre pontos [m]
ra = 0.45; % resolução ângular do motor em graus

% 1 : gerar curva que define o perfil da peça

% circulo

theta = 0:2*pi()/720:2*pi();
theta = theta';
r =0.20;
x = r*cos(theta);
y = r*sin(theta);
z = 0.11*ones(size(x));

pc =[x,y,z];

% 2 : ajustar a distacia entre pontos de forma que eles fique aproximadamente
% igualmente espaçados

save -6 perfil.mat pc