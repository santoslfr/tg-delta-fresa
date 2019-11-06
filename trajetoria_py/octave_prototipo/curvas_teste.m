%% Logo UFABC
%
%r = 0.02;
%
%xa = -r;
%ya = -(1/3)*r*sqrt(3);
%
%xb = 0;
%yb = (2/3)*r*sqrt(3);
%
%xc = r;
%yc = -(1/3)*r*sqrt(3);
%
%hold on
%
%t1 = 5*pi/8:0.01:17*pi/8;
%%t1 = 0:0.01:2*pi;
%
%x1 = r*cos(t1) + xa;
%y1 = r*sin(t1) + ya;
%
%plot(x1,y1)
%
%t2 = 9*pi/8:-0.01:-3*pi/8;
%%t2 = 0:0.01:2*pi;
%
%x2 = r*cos(t2) + xb;
%y2 = r*sin(t2) + yb;
%
%plot(x2,y2)
%
%t3 = 3*pi/8:0.01:17*pi/8;
%%t3 = 0:0.01:2*pi;
%
%x3 = r*cos(t3) + xc;
%y3 = r*sin(t3) + yc;
%
%plot(x3,y3)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% curva que define o perfil da peça

dep = 10^-3; % distancia entre pontos [m]
ra = 0.45; % resolução ângular do motor em graus

% curva

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 3D
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Helicoidal

%t = 0:0.05:6*pi;
%a1 = 0.05;
%zi = 0.08
%zf = 0.10;
%
%x = a1*cos(t);
%y = a1*sin(t);
%z = zi:(zf - zi)/(size(t,2)-1):zf;
%
%pd=[x',y',z'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Trefoil

%t = 0:0.1:6.5;
%
%a1 = 0.02;
%b1 = 0.02;
%c1 = 0.01;
%c2 = 0.08;
%
%x = a1*(sin(t) + 2*sin(2*t));
%y = b1*(cos(t) - 2*cos(2*t));
%z = c1*(-sin(3*t)) + c2;
%
%pd=[x',y',z'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Espiral Circular

%t = 0:0.05:2*pi;
%
%a1 = 0.005;
%b1 = 0.005;
%c1 = 0.01;
%c2 = 0.1;
%
%x = a1*(3*cos(t) + cos(10*t).*cos(t));
%y = b1*(3*sin(t) + cos(10*t).*sin(t));
%z = c1*(sin(10*t)) +c2;
%
%pd=[x',y',z'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Esfera_3D

t = 0:0.005:pi/3;

phi=t*16*pi;
theta=t*pi;

a1 = 0.01;
b1 = 0.01;
c1 = 0.005;
c2 = 0.1;

x = a1*(cos(phi).*sin(theta));
y = b1*(sin(phi).*sin(theta));
z = c1*(cos(theta)) + c2;

pd=[x',y',z'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 2D
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Lissajous

%t = 0:0.02:2*pi;
%
%A = 0.01;
%B = 0.01;
%
%d = pi/2;
%
%a1 = 5; %impar
%b1 = 6; %par
%
%% |a-b| = 1
%
%zi = 0.1;
%
%x = A*sin(a1*t + d);
%y = B*sin(b1*t);
%z = zi*ones(1,size(x,2));
%
%pd=[x',y',z'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% deslovamento vertical:

z = [0.13:-0.01:pd(1,3)];
x = zeros(size(z));
y = zeros(size(z));

pv = [x',y',z'];

% deslocamento horizontal:

xi = pv(size(pv,1),1);
yi = pv(size(pv,1),2);
zi = pv(size(pv,1),3);
xf = pd(1,1);
yf = pd(1,2);

if (xf != xi)

% distancia entre os pontos

d = ((xf - xi)^2 + (yf - yi)^2)^0.5 ;

% coeficiente angular

m = ((yf - yi)/(xf - xi));

% coeficiente linear

c = yi - m*xi;

% segmentos:

n = ceil(d/(dep));

% y = m*x

o = [1:1:n]';
p = ones(n,1);

x = (xf/n)*o;
y = (xf/n)*o*m + p*c;
z = zi*p;

ph =[x,y,z];

elseif (yf != yi)

% distancia entre os pontos

d = ((xf - xi)^2 + (yf - yi)^2)^0.5 ;

% segmentos:

n = ceil(d/(dep));
p = ones(n,1);

x = [xi*ones(1,n)]';
y = [yi:(yf - yi)/(n-1):yf]';
z = zi*p;

ph = [x,y,z];

else

t = size(pv,1)

ph = [pv(t,1),pv(t,2),pv(t,3)];

end

% movimento total

pt=[pv;ph;pd];

%plot3(pt(:,1),pt(:,2),pt(:,3))
%
%plot3(pv(:,1),pv(:,2),pv(:,3))
%plot3(ph(:,1),ph(:,2),ph(:,3))
%plot3(pd(:,1),pd(:,2),pd(:,3))

save -6 deslocamento_teste.mat pt
save -6 -append deslocamento_teste.mat pd
save -6 -append deslocamento_teste.mat ph
save -6 -append deslocamento_teste.mat pv