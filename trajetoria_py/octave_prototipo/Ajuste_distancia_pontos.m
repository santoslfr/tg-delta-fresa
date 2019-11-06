function [pd] = Ajuste_distancia_pontos(p,dep)

% ajusta a distancia entre os pontos que formam uma curva para que esses fiquem
% igualmnete espaçados (aumentando ou diminuindo o numero de pontos se necessario)

% cálculo do comprimento do segmento do perimetro da peça

[arclen,seglen] = arclength(p(:,1),p(:,2),p(:,3));

% alocação de variaveis

n_seg = ceil(arclen/dep);% numero de segmentos
pd=zeros(n_seg,3); % pontos ajustados

% divide o segmento do perimetro em pontos igualmente espaçados de aproximadamente 1 mm

pd = curvspace(p,n_seg);