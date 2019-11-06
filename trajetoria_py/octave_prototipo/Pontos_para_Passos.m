function [passos_ep] = Pontos_para_Passos(Phi,ra)

% Descrição :

% recebe a sequência de pontos da trajetória end-effector( na forma de ângulos que os motores devem assumir)
% e retorna e sequência de passos a serem realizados

% Entradas :

% Phi : ângulos do motor que levam aos pontos desejados do end-effector [rad]
% ra : resolução ângular do motor [graus]

% Saída :

% passos a serem realizados

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% alocação de variaveis

n_seg = size(Phi,1) -1; % numero de segmentos
passos_ep_temp=zeros(size(Phi,1),3); % passos entre pontos temporário
passos_ep=zeros(1,3); % passos entre pontos

%passos entre pontos

for j=1:1:n_seg

passos_ep_temp(j,:) = (Phi(j+1,:)- Phi(j,:))/(ra*((2*pi())/(360)));

end

% remove os passos nulos :000

passos_ep_temp(~any(passos_ep_temp,2),:)=[];

% arredondamento

passos_ep_temp=round(passos_ep_temp);

% divide passos multiplos em sequência de passos simples
% exemplo : 020 -> 010 010 ; -102 -> -101 001 ; -12-3 -> -11-1 01-1 00-1

for i=1:1:size(passos_ep_temp,1)% verificar  fim do passos_ep_temp

a = max(abs(passos_ep_temp(i,:)));

if a > 1 % maior ta fucionando como maior igual ?????????

temp = [[sign(passos_ep_temp(i,1))*ones(abs(passos_ep_temp(i,1)),1);zeros(a-abs(passos_ep_temp(i,1)),1)]...
       ,[sign(passos_ep_temp(i,2))*ones(abs(passos_ep_temp(i,2)),1);zeros(a-abs(passos_ep_temp(i,2)),1)]...
       ,[sign(passos_ep_temp(i,3))*ones(abs(passos_ep_temp(i,3)),1);zeros(a-abs(passos_ep_temp(i,3)),1)]];

passos_ep = [ passos_ep ; temp ];

else

passos_ep  = [ passos_ep ; passos_ep_temp(i,:)];

end
end


% remove os passos nulos :000

passos_ep(~any(passos_ep,2),:)=[];

% transforma os passos da forma direção(+ ou -) passo( 1 ou 0) para a forma
% direção(1 ou 0) passo( 1 ou 0). Exemplos :-110 -> 011100 ; 101 - > 110011

passos_ep = [[passos_ep(:,1) > 0 , abs(passos_ep(:,1))]...
            ,[passos_ep(:,2) > 0 , abs(passos_ep(:,2))]...
            ,[passos_ep(:,3) > 0 , abs(passos_ep(:,3))]];
            
% arredondamento

passos_ep=round(passos_ep);