% Volume de trabalho Robô Delta com base na cinemátiva inversa

% parâmetros do robô

[l1,l2,a,b,d_externo,d_interno,d,alfa,mp,m1,m2,g,I_motor] = delta_parametros_prototipo;

% Contrução de uma grade regular

x = -0.08:0.005:0.08;
[xx , yy , zz] = meshgrid(x);
xxx = reshape(xx,size(xx,1)*size(xx,2)*size(xx,3),1);
yyy = reshape(yy,size(yy,1)*size(yy,2)*size(yy,3),1);
zzz = reshape(zz,size(zz,1)*size(zz,2)*size(zz,3),1);
zzz = zzz + 0.08*ones(size(zzz));
pts = [xxx,yyy,zzz];        % pontos para teste
%plot3(xxx,yyy,zzz,'.');

n = size(pts,1)          ;  % numero de pontos (xyz)
pt = zeros(n,3)          ;  % pontos admissiveis
pt_na = zeros(n,3)       ;  % pontos não-admissiveis
ang = zeros(n,3)         ;  % Ângulos que resultam em pontos admissiveis
ang_na = zeros(n,3)      ;  % Ângulos que resultam em pontos não-admissiveis

warning('off','Octave:divide-by-zero');

for k=1:1:n;

[r,Phi2,ri,l1i,l2i] = delta_cine_inv(pts(k,:)',l1,l2,a,b,alfa);

if  isreal(r) && not(isnan(r)) && not(isinf(r)) && r > 0

pt(k,:) = pts(k,:)';
ang(k,:) = r;

else

pt_na(k,:) = pts(k,:)';
ang_na(k,:) = r;

end

end

plot3(pt(:,1),pt(:,2),pt(:,3),'.')
axis([-0.08 , 0.08 , -0.08 , 0.08 , 0 , 0.16 ],"square")

warning('on','Octave:divide-by-zero');

%save('Volume_trabalho_inv','pt')
%load('Volume_trabalho_inv')
