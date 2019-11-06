% Volume de trabalho Robô Delta com base na cinemátiva direta

% parâmetros do robô
[l1,l2,a,b,d_externo,d_interno,d,alfa,mp,m1,m2,g,I_motor] = delta_parametros_prototipo;

l = 0  ; %ângulo minimo
m = 5 ; %passo ângulo
n = 90 ; %ângulo máximo
o = size([l:m:n],2)^3 + 1 ; % contador primários
p = size([l:m:n],2)^3     ; % contador secundários
q = zeros(p,3)            ; % pontos do volume de trabalho
ang = zeros(p,3)          ; % ângulos admissiveis
ang_na = zeros(p,3)       ; % ângulos não-admissiveis
erros = 0;

warning('off','Octave:divide-by-zero');

for k=l:m:n
for j=l:m:n
for i=l:m:n

Phi = [i,j,k]*((2*pi())/360);
r = delta_cine_dir(Phi,l1,l2,a,b,alfa);
q(o - p,:) = r';
ang(o - p,:) = [i,j,k];
p = p - 1;

end
end
end

warning('on','Octave:divide-by-zero');

figure(1)
plot3(q(:,1),q(:,2),q(:,3),'.');
title('Volume de Trabalho do Manipulador Delta')
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
saveas(1,'volume_de_trabalho_3d.png')

figure(2)
plot3(q(:,1),q(:,2),q(:,3),'.');
title('Volume de Trabalho do Manipulador Delta')
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
view(90,0)
saveas(2,'volume_de_trabalho_frontal.png')

figure(3)
plot3(q(:,1),q(:,2),q(:,3),'.');
title('Volume de Trabalho do Manipulador Delta')
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
view(0,0)
saveas(3,'volume_de_trabalho_lateral.png')

figure(4)
plot3(q(:,1),q(:,2),q(:,3),'.');
title('Volume de Trabalho do Manipulador Delta')
xlabel('x [m]')
ylabel('y [m]')
zlabel('z [m]')
view(2)
saveas(4,'volume_de_trabalho_superior.png')

w=q;
w(any(isnan(w),2),:)=[];
[triHull, vbOutside, vbInside] = AlphaHull(w,0.001);
trisurf(triHull(vbOutside,:),w(:,1),w(:,2),w(:,3))

%save('Volume_trabalho_dir','q')
%load('Volume_trabalho_dir')

