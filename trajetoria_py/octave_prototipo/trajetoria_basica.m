% trajetória básica

% váriaveis

dep = 10^-4; % distancia entre pontos [m]
ra = 0.45; % resolução ângular do motor em graus

% 1 : gerar curva que define o perfil da peça

% circulo

theta = 0:2*pi()/720:2*pi();
theta = theta';
r =0.01;
x = r*cos(theta);
y = r*sin(theta);
z = 0.11*ones(size(x));

pc =[x,y,z];

% 2 : ajustar a distacia entre pontos de forma que eles fique aproximadamente
% igualmente espaçados

pd = Ajuste_distancia_pontos(pc,dep);

% 3 :Ajuste dos pontos requeridos pela curva pelos pontos possiveis de serem
% alcançados pelo robô


for j = 1:1:size(pd,1);

[Phi_m(j,:),p_m(j,:)] = Ajuste_dos_Pontos(pd(j,:)',ra);

end

% 4 : tranforma pontos em sequencia de passos

passos = Pontos_para_Passos(Phi_m,ra);