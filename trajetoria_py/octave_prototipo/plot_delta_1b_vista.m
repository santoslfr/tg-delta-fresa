function [i,j,k,i2,j2,k2,i3,j3,k3]=plot_delta_1b_vista(a,b,l1i,l2i,alfa,p)

A1 = [a;0;0];

B1 = [b;0;0];

A=zeros(3,3);
B=zeros(3,3);

% transformação do sistema de coordenadas local ( pernas ) para o sistema de coorddenadas global

for i=1:1:3

T0i = [ cos(alfa(i,1))    , sin(alfa(i,1)) , 0 ;
        -1*sin(alfa(i,1)) , cos(alfa(i,1)) , 0 ;
        0                 , 0              , 1 ];
        
A(:,i) = inv(T0i)*A1;
B(:,i) = inv(T0i)*B1;
%l1i(:,i) = inv(T0i)*l1i(:,i);
%l2i(:,i) = inv(T0i)*l2i(:,i);
%
end

i = [0,A(1,1),A(1,1) + l1i(1,1),A(1,1) + l1i(1,1) + l2i(1,1),A(1,1) + l1i(1,1) + l2i(1,1) + -1*B(1,1)];
j = [0,A(2,1),A(2,1) + l1i(2,1),A(2,1) + l1i(2,1) + l2i(2,1),A(2,1) + l1i(2,1) + l2i(2,1) + -1*B(2,1)];
k = [0,A(3,1),A(3,1) + l1i(3,1),A(3,1) + l1i(3,1) + l2i(3,1),A(3,1) + l1i(3,1) + l2i(3,1) + -1*B(3,1)];

i2 = [0,A(1,2),A(1,2) + l1i(1,2),A(1,2) + l1i(1,2) + l2i(1,2),A(1,2) + l1i(1,2) + l2i(1,2) + -1*B(1,2)];
j2 = [0,A(2,2),A(2,2) + l1i(2,2),A(2,2) + l1i(2,2) + l2i(2,2),A(2,2) + l1i(2,2) + l2i(2,2) + -1*B(2,2)];
k2 = [0,A(3,2),A(3,2) + l1i(3,2),A(3,2) + l1i(3,2) + l2i(3,2),A(3,2) + l1i(3,2) + l2i(3,2) + -1*B(3,2)];

i3 = [0,A(1,3),A(1,3) + l1i(1,3),A(1,3) + l1i(1,3) + l2i(1,3),A(1,3) + l1i(1,3) + l2i(1,3) + -1*B(1,3)];
j3 = [0,A(2,3),A(2,3) + l1i(2,3),A(2,3) + l1i(2,3) + l2i(2,3),A(2,3) + l1i(2,3) + l2i(2,3) + -1*B(2,3)];
k3 = [0,A(3,3),A(3,3) + l1i(3,3),A(3,3) + l1i(3,3) + l2i(3,3),A(3,3) + l1i(3,3) + l2i(3,3) + -1*B(3,3)];


%hold off

