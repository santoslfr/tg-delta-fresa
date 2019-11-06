clc
clear

% parâmetros do robô
[l1,l2,a,b,d_externo,d_interno,d,alfa,mp,m1,m2,g,I_motor] = delta_parametros_prototipo;

t=0;
omega = 15; %[rad/s)
p=[0;0;0];
[Phi1,Phi2,ri,l1i,l2i] = delta_cine_inv(p,l1,l2,a,b,alfa);
[h1,h2,h3,h4,h5,h6]=plot_delta_1a_vista(a,b,l1i,l2i,alfa,p);
pa=zeros(size(p));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Carregar arquivo

load deslocamento_teste.mat

for t = 1:1:size(pt,1)

p=[pt(t,1);pt(t,2);pt(t,3)];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Infinito

%for t = 0:0.01:1

%p=[0.02*sin(omega*t);0.02*sin(2*omega*t);0.08];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%Lissajous

%for t = 0:0.01:1

%al = 18; %[rad/s)
%bl = 24;
%dl = pi/2;
%p=[0.03*sin(al*t + dl);0.02*sin(bl*t);0.08];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Espiral Circular

%for t = 0:0.05:2*pi;
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
%p=[x,y,z];
%
%p=p';
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Esfera_3D

%for t = 0:0.005:pi/3;
%
%phi=t*16*pi;
%theta=t*pi;
%
%a1 = 0.01;
%b1 = 0.01;
%c1 = 0.005;
%c2 = 0.10;
%
%x = a1*(cos(phi).*sin(theta));
%y = b1*(sin(phi).*sin(theta));
%z = c1*(cos(theta)) + c2;
%
%p=[x,y,z];
%
%p=p';

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Lissajous v2
%
%for t = 0:0.02:2*pi;
%
%A = 0.02;
%B = 0.02;
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
%p=[x,y,z];
%
%p=p';

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pa=[pa,p];
[Phi1,Phi2,ri,l1i,l2i] = delta_cine_inv(p,l1,l2,a,b,alfa);
[i,j,k,i2,j2,k2,i3,j3,k3]=plot_delta_1b_vista(a,b,l1i,l2i,alfa,p);
set(h1,'XData', p(1,1) ,'YData',p(2,1),'Zdata',p(3,1));
set(h2,'XData', i  ,'YData', j ,'Zdata',k );
set(h3,'XData', i2 ,'YData', j2,'Zdata',k2);
set(h4,'XData', i3 ,'YData', j3,'Zdata',k3);
set(h5,'XData', [0,p(1,1)] ,'YData',[0,p(2,1)],'Zdata',[0,p(3,1)]);
%set(h6,'XData', p(1,1) ,'YData',p(2,1),'Zdata',p(3,1));
hold on
scatter3(p(1,1),p(2,1),p(3,1),'r',".");
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
%scatter3(pa(1,:),pa(2,:),pa(3,:),'r',".");
drawnow();

%Salva sequencia de imagens
%
%if (mod(t,0.3)==0)
%
%saveas(1,strcat('simulacao_',num2str(t),'.png'))
%
%end

end

%hold off
%pause(0.01)