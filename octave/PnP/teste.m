q = [ -1   1 -1;
       1   1 -1;
      -1  -1 -1;
       1  -1 -1;];

%r_i = 5
 
d12= 5.7735; %[mm]
d13= 5.7735; %[mm]
d24= 5.7735; %[mm]
d34= 5.7735; %[mm]
d14= 8.1650; %[mm]
d23= 8.1650; %[mm]

       % 1   2   3   4
d_ij = [ 1   d12 d13 d14;  %1
         d12 1   d23 d24;  %2
         d13 d23 1   d34;  %3
         d14 d24 d34 1   ]; %4
         
[c_tetha_ij] = cosseno_entre_raios(q);
[r_i] = distancia_ri(c_tetha_ij,d_ij);

%pkg load statistics

%l = (5/sqrt(3))*q
%pdist([l(1,:);l(4,:)],"euclidean")
%scatter3(q(:,1),q(:,2),q(:,3))
%hold on
%scatter3(l(:,1),l(:,2),l(:,3))