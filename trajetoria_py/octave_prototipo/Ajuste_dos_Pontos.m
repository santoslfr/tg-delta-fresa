function [Phi_m,p_m] = Ajuste_dos_Pontos(p,ra_g)

warning('off','Octave:divide-by-zero');

% Ajuste dos pontos requeridos pela curva pelos pontos possiveis de serem alcançados pelo robô

pkg load statistics

% parâmetros do robô

[l1,l2,a,b,d_externo,d_interno,d,alfa,mp,m1,m2,g,I_motor] = delta_parametros_prototipo;

% váriaveis

pt   = zeros(27,3); % pontos próximos ao ponto "p"
p_m = zeros(1,3);   % ponto que melhor aproxima "p"
Phit = zeros(27,3); % ângulos Phi que levam aos pontos "pt"
Phi_m = zeros(1,3); % ângulos que levam ao ponto "p_m"
ra   = ra_g*((2*pi())/(360)); % Resolução ângular do passo do motor
dist = 10^3; % distnacia entre o ponto "p" e o ponto "p_m" (iniciada com um valor arbitário suficientemente grande )
d_temp = 0 ;% variável temporaria para distancia entre dois pontos 
c_temp = 1;% variável temporária para contagem dos pontos
% Determinação dos ângulos para o ponto esperado

[Phi1,Phi2,ri,l1i,l2i] = delta_cine_inv(p,l1,l2,a,b,alfa);

% Aproximação dos ângulos para os ângulos possiveis de serem alcançados pelo robô


% verificar se o ângulo é multiplo da resolução ângular do motor

for i=1:1:3
    for j=1:1:3
        for k=1:1:3

switch i

  case 1

    if (rem(Phi1(1,1),ra)==0)

    Phit(c_temp,1) = Phi1(1,1);

    end

  case 2

  Phit(c_temp,1) = ra*floor(Phi1(1,1)/ra);

  case 3

  Phit(c_temp,1) = ra*ceil(Phi1(1,1)/ra);

end

switch j

  case 1

    if (rem(Phi1(1,2),ra)==0)

    Phit(c_temp,2) = Phi1(1,2);

    end

  case 2

  Phit(c_temp,2) = ra*floor(Phi1(1,2)/ra);

  case 3

  Phit(c_temp,2) = ra*ceil(Phi1(1,2)/ra);

end

switch k

  case 1

    if (rem(Phi1(1,3),ra)==0)

    Phit(c_temp,3) = Phi1(1,3);

    end

  case 2

  Phit(c_temp,3) = ra*floor(Phi1(1,3)/ra);

  case 3

  Phit(c_temp,3) = ra*ceil(Phi1(1,3)/ra);

end

% determinação do ponto "pt" mais próximo de "p"

pt(c_temp,:) = delta_cine_dir(Phit(c_temp,:),l1,l2,a,b,alfa);

d_temp = pdist([p';pt(c_temp,:)],"euclidean");

if d_temp < dist

    dist = d_temp;
    p_m = pt(c_temp,:);
    Phi_m = Phit(c_temp,:);

    else if dist == d_temp

    da_m = pdist([Phi1;Phi_m],"euclidean");
    da_temp = pdist([Phi1;Phit(c_temp,:)],"euclidean");

      if da_temp < da_m

        p_m = pt(c_temp,:);
        Phi_m = Phit(c_temp,:);

      end
    end
end

c_temp = c_temp +1;

end
end
end
