% deslocamento vertical

% váriaveis

dep = 10^-4; % distancia entre pontos [m]
ra = 0.45; % resolução ângular do motor em graus

% 1 : deslocamento vertical do ponto de calibração até a penetração
% da fresa no material a ser cortado


z = [0.13:-0.01:0.08];
x = zeros(size(z));
y = zeros(size(z));

pc =[x',y',z'];

% 2 : ajustar a distacia entre pontos de forma que eles fique aproximadamente
% igualmente espaçados

save -6 deslocamento_vertical.mat pc