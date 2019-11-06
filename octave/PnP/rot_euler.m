clear
clc

a = 0;
b = 0;
c = pi/4;

R_x = [1       , 0      , 0      ;
       0       , cos(a) , -sin(a);
       0       , sin(a) , cos(a) ];

R_y = [cos(b)  , 0      , sin(b) ;
       0       , 1      , 0      ;
       -sin(b) , 0      , cos(b) ];

R_z = [cos(c)  ,-sin(c) , 0      ;
       sin(c)  , cos(c) , 0      ;
       0       , 0      , 1      ];

R = R_z*R_y*R_x;

v = [ 1 ; 0 ; 0 ];

%t = (v')*R;
%t = (v')*R';
t =  R*v;
%t = (R')*v;
 
 x = t(1);
 y = t(2);
 z = t(3);

 ax = atan2(sqrt(y^2+z^2),x);
 ay = atan2(sqrt(z^2+x^2),y);
 az = atan2(sqrt(x^2+y^2),z);
