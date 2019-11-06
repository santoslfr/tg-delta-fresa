function p = delta_cine_dir(Phi,l1,l2,a,b,alfa)

% parâmetros do robô

% dimensões

% l1 : comprimento do braço / distância entre a junta do ombro e do cotovelo
% l2 : comprimento do antebraço / distância entre a junta do cotovelo
% a  : distância entre a origem do sistema de coordenadas da base e a junta do ombro
% b  : distância entre a origem do sistema de coordenadas do end-effector e a junta do pulso
% d_externo : diametro da barra externa do link distal
% d_interno : diametro da barra interna do link distal
% d  : distância entre as juntas rotulares j1 e j2
% alfa : %ângulo entre os braços : 0º, 120º e 240°

% parâmetros cinemáticos

% p : posição do end-effector
% Phi : ângulos dos atuadores

% variáveis

% obs.: Variáveis com o prefixo "L_" estão no sistema de coordenadas local de cada braço

L_ai = [a;0;0];
L_bi = [b;0;0];
L_l1i=zeros(3,3);
Ci = zeros(3,3);
ai=zeros(3,3);
bi=zeros(3,3); 
l1i=zeros(3,3);

% inicio do programa

for i=1:3         

L_l1i(:,i) = [ l1*cos(Phi(1,i)) ;
               0                ;
               l1*sin(Phi(1,i)) ];
             
end 

%Transformação dos vetores dos sitemas de coordenadas locais para o sistema de coordenadas global

T0i = [ 1 , 0 , 0 ;
       -0 , 1 , 0 ;
        0 , 0 , 1 ];
        
T0i(:,:,2) = [ -0.50000 ,  0.86603 , 0.00000 ;
               -0.86603 , -0.50000 , 0.00000 ;
                0.00000 ,  0.00000 , 1.00000 ];

T0i(:,:,3) = [-0.50000 , -0.86603 ,  0.00000 ;
               0.86603 , -0.50000 ,  0.00000 ;
               0.00000 ,  0.00000 ,  1.00000 ];

inv_T0i =[ 1 , -0 ,  -0 ;
          -0 ,  1  , -0 ;
           0 ,  0  , 1  ];

inv_T0i(:,:,2) = [ -0.50000 , -0.86603 , -0.00000 ;
                    0.86603 , -0.50000 , -0.00000 ;
                    0.00000 ,  0.00000 ,  1.00000 ];

inv_T0i(:,:,3) = [ -0.50000 ,  0.86603 , -0.00000 ;
                   -0.86603 , -0.50000 , -0.00000 ;
                    0.00000 ,  0.00000 ,  1.00000 ];
                    

for i=1:3

%T0i(:,:,i) = [ cos(alfa(i,1))    , sin(alfa(i,1)) , 0 ;
%               -1*sin(alfa(i,1)) , cos(alfa(i,1)) , 0 ;
%               0                 , 0              , 1 ];
%   
%inv_T0i(:,:,i) = inv(T0i(:,:,i));



ai(:,i) = inv_T0i(:,:,i)*L_ai;
bi(:,i) = inv_T0i(:,:,i)*L_bi;
l1i(:,i)= inv_T0i(:,:,i)*L_l1i(:,i);

end

% Análise da Posição : cinemática direta ( dado os ângulos Phi1i determinar a posição do end-effector )

% centro da esferas

%Ci = ai + l1i - bi 

for i=1:1:3

Ci(:,i) = ai(:,i) + l1i(:,i) - bi(:,i);

end

if (Ci(3,1) == Ci(3,2))

x1 = Ci(1,1);
y1 = Ci(2,1);
z1 = Ci(3,1);
x2 = Ci(1,2);
y2 = Ci(2,2);
z2 = Ci(3,2);
x3 = Ci(1,3);
y3 = Ci(2,3);
z3 = Ci(3,3);

elseif (Ci(3,1) == Ci(3,3))

x1 = Ci(1,1);
y1 = Ci(2,1);
z1 = Ci(3,1);
x2 = Ci(1,3);
y2 = Ci(2,3);
z2 = Ci(3,3);
x3 = Ci(1,2);
y3 = Ci(2,2);
z3 = Ci(3,2);

else %(Ci(3,2) == Ci(3,3))

x1 = Ci(1,2);
y1 = Ci(2,2);
z1 = Ci(3,2);
x2 = Ci(1,3);
y2 = Ci(2,3);
z2 = Ci(3,3);
x3 = Ci(1,1);
y3 = Ci(2,1);
z3 = Ci(3,1);

end

r1 = r2 = r3 = l2;

if ( z1 != z2 || z1 != z3 || z2 != z3 )

a11 = 2*(x3 - x1);
a12 = 2*(y3 - y1);
a13 = 2*(z3 - z1);
a21 = 2*(x3 - x2);
a22 = 2*(y3 - y2);
a23 = 2*(z3 - z2);
b1 = r1^2 - r3^2 - x1^2 - y1^2 - z1^2 + x3^2 + y3^2 + z3^2;
b2 = r2^2 - r3^2 - x2^2 - y2^2 - z2^2 + x3^2 + y3^2 + z3^2;

a1 = (a11/a13) - (a21/a23);
a2 = (a12/a13) - (a22/a23);
a3 = (b2/a23)  - (b1/a13);
a4 = -(a2/a1);
a5 = -(a3/a1);

a6 = (-a21*a4 - a22)/a23;
a7 = (b2 - a21*a5)/a23;

a = a4^2 + 1 + a6^2;
b = 2*a4*(a5 - x1) - 2*y1 + 2*a6*(a7 - z1);
c = a5*(a5 - 2*x1) + a7*(a7 - 2*z1) + x1^2 + y1^2 + z1^2 - r1^2;

y_p = (-b + (b^2 -4*a*c)^(1/2))/(2*a);
y_n = (-b - (b^2 -4*a*c)^(1/2))/(2*a);

x_p = a4*y_p + a5;
x_n = a4*y_n + a5;

z_p = a6*y_p + a7;
z_n = a6*y_n + a7;


if ( z_p < 0 )

p(1,1) = x_n;
p(2,1) = y_n;
p(3,1) = z_n;

else

p(1,1) = x_p;
p(2,1) = y_p;
p(3,1) = z_p;

end

elseif ( z1 == z3 && z2 == z3 )

zn = z1;

a = 2*(x3 -x1);
b = 2*(y3 -y1);
c = r1^2 - r3^2 - x1^2 - y1^2 + x3^2 + y3^2;
d = 2*(x3 -x2);
e = 2*(y3 -y2);
f = r2^2 - r3^2 - x2^2 - y2^2 + x3^2 + y3^2;

x = (c*e - b*f)/(a*e - b*d);
y = (a*f - c*d)/(a*e - b*d);

A = 1;
B = -2*zn;
C = zn^2 - r1^2 + ( x - x1 )^2 + ( y - y1 )^2;

z_pa = (-B + (B^2 -4*C)^(1/2))/(2);
z_pb = (-B - (B^2 -4*C)^(1/2))/(2);

if ( z_pb < 0 )

p(1,1) = x;
p(2,1) = y;
p(3,1) = z_pa;

else

p(1,1) = x;
p(2,1) = y;
p(3,1) = z_pb;

end

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Equações baseadas no trabalho :

%"The Delta Parallel Robot Kinematics Solutions"
%
% autor :
%
% Robert L. Williams II

% Bases matemáticas do algoritimo

% intersecção de três esferas

%Parte A

%1.equação das três esferas

% I   :(x -x1)^2 + (y -y1)^2 + (z -z1)^2 = r1^2
% II  :(x -x2)^2 + (y -y2)^2 + (z -z2)^2 = r2^2
% III :(x -x3)^2 + (y -y3)^2 + (z -z3)^2 = r3^2

%2.expanção  dos termos do lado esquerdo das equações de (1). Subtração da equação (III) da (I)
% e da (III) da (II)

% IV : a11*x + a12*y + a13*z = b1
% V  : a21*x + a22*y + a23*z = b2

% onde :

% a11 = 2*(x3 -x1)
% a12 = 2*(y3 -y1)
% a13 = 2*(z3 -z1)
% a21 = 2*(x3 -x2)
% a32 = 2*(y3 -y2)
% a23 = 2*(z3 -z2)
% b1 = r1^2 - r3^2 - x1^2 - y1^2 - z1^2 + x3^2 + y3^2 + z3^2
% b2 = r2^2 - r3^2 - x2^2 - y2^2 - z2^2 + x3^2 + y3^2 + z3^2

%3.isolar z em (IV) e (V)

% VI  : z = (b1/a13) - (a11/a13)*x - (a12/a13)*y
% VII : z = (b2/a23) - (a21/a23)*x - (a22/a23)*y

%4. subtrair (VI) de (VII) para eliminar z e obter x=f(y)

% VIII : x=f(y)= a4*y +a5

% onde :

% a4 = -(a2/a1)
% a5 = -(a3/a1)
% a1 = (a11/a13) - (a21/a23)
% a2 = (a12/a13) - (a22/a23)
% a3 = (b2/a23) - (b1/a13)

%5. substituir (VIII) em (VII) para eliminar x e obter z=f(y)

% IX : z=f(y)= a6*y +a7

% onde :

% a6 = (-a21*a4 - a22)/a23
% a7 = (b2 - a21*a5)/a23

%6. substituir (VIII) e (IX) em (I) para eliminar x e z e obter uma unica equação quadratica somente com y

% X : a*y^2 + b*y + c = 0

% onde :

% a = a4^2 + 1 + a6^2
% b = 2*a4*(a5 - x1) - 2*y1 + 2*a6*(a7 - z1)
% c = a5*(a5 - 2*x1) + a7*(a7 - 2*z1) + x1^2 + y1^2 + z1^2 - r1^2

% duas soluções para y

% y± = (-b ± (b^2 -4*a*c)^(1/2))/2*a

%7. substituir y+ e y- de (X) em (VIII) e (IX)

% (XI)  : x± = a4*y± + a5
% (XII) : z± = a6*y± + a7

%8. são obtidas duas soluções uma para y+ e uma para y-

% {x+ y+ z+} e {x- y- z-}

% Soluçõe imaginárias, singularidades e multiplas soluções

% Soluçõe imaginárias :

% ocorrem quando b^2 -4*a*c < 0, o que equivale a fisicamente não haver intersecção entre todas as esferas
% no caso em que b^2 -4*a*c = 0 há intersecção tangencial entre 2 esferas e a terceira também passa por esse ponto

% Singularidades :

% Podem ocorrer singularidades no algoritimo ( divisão por zero ). Diferentes singularidades podem sugir
% em função de diferentes combinações das equações em (1) para eliminação e determinação das variaveis x, y e z

% sigularidades apresentadas na equações desenvolvidas

% condições para singularidade :

% a13 = 0
% a23 = 0
% a1 = 0
% a = 0

% As duas primeiras condições :

% a13 = 2*(z3 - z1) = 0
% a23 = 2*(z3 - z2) = 0

% São satisfeitas qunado o centro das esferas 1 e 3 ou 2 e 3 tem a mesma altura isto é
% z1 = z3 ou z2 = z3. Portanto no caso em que todas as esferas possuem a mesma altura o algoritimo 
% sempre é singular (será proposta uma solução na Parte B)

% A terceira condição de singularidade :

% a1 = (a11/a13) - (a21/a23) = 0

% simplificando

% (x3 - x1)/(z3 - z1) = (x3 - x2)/(z3 - z2)

% Para que esss condição seja atendida o centro das esferas 1,2 e 3 devem ser colineares no plano XZ
% Em geral essa  codição de singularidade só é atendida no limite do volume de trabalho. Desde que
% não se trabalhe nesse limite a terceira condição não causa problemas 

% A quarta condição de singularidade :

% a = a4^2 + 1 + a6^2 = 0

% é satisfeita quando :

% a4^2 + a6^2 = -1

% É impossivel satisfazer essa condição contato que a4 e a6 sejam numeros reais ( oque é o caso na
%implementação do hardware). Portanto a quarta condição de singularidade numca é um problema

% Multiplas Soluções

% Em geral o algoritiomo de determinação da intersecção de três esferas gera duas soluções 
% Geralmente somente uma dessas soluções é valida, determinada pelas configurações admissiveis pelo robo delta

% Parte B

% Algoritimo para determinação do ponto de intersecção de três esferas quando todas as esferas tem a mesma
% altura no eixo vertical. Assumindo que as três esferas dadas são (c1 , r1) , (c2 , r2) e (c3 , r3)]
% Isso é, vetores do centro c1 ={ x1 , y1 e z1 } , c2 ={ x2 , y2 e z2 } e c3 ={ x3 , y3 e z3 } e raios
% r1  r2 e r3. Os três centros das esferas devem seer dados no mesmo sistema de coordenadas.
% As equações das três esferas a se interseptar são :

% I   :(x -x1)^2 + (y -y1)^2 + (z -zn)^2 = r1^2
% II  :(x -x2)^2 + (y -y2)^2 + (z -zn)^2 = r2^2
% III :(x -x3)^2 + (y -y3)^2 + (z -zn)^2 = r3^2

% Uma vez que a altura do centro de todas as esferas é a mesma temos z1 = z2 = z3 = zn
% o ponto de intersecção desconhecido P = { z, y , z }. Expandido as equações (I) a (III) :

% IV : x^2 -2*x1*x + x1^2 + y^2 -2*y1*y + y1^2 + z^2 - 2*zn*z + zn^2 = r1^2
% V  : x^2 -2*x2*x + x2^2 + y^2 -2*y2*y + y2^2 + z^2 - 2*zn*z + zn^2 = r2^2
% VI : x^2 -2*x3*x + x3^2 + y^2 -2*y3*y + y3^2 + z^2 - 2*zn*z + zn^2 = r3^2

% Subtraindo (VI) de (IV) e (VI) de (V) leva a :

% VII  : 2*(x3 - x1)*x + 2*(y3 - y1)*y + x1^2 + y1^2 - x3^2 - y3^2 = r1^2 - r3^2
% VIII : 2*(x3 - x2)*x + 2*(y3 - y2)*y + x2^2 + y2^2 - x3^2 - y3^2 = r2^2 - r3^2

% Todos os termos não lineares das váriaveis x e y são cancelados na subtração acima
% Alem disso todos os termos contendo a váriavel z tambem são cancelados na subtração uma vez que
% todas as altura z dos centros das esferas são identicas. As equações (VII) e (VIII) são duas 
% equações lineares com duas váriaveis da seguinte forma :

% /a b\ /x\ = /c\
% \c d/ \y/   \f/

% Onde :

% a = 2*(x3 -x1)
% b = 2*(y3 -x1)
% c = r1^2 - r3^2 - x1^2 - y1^2 + x3^2 + y3^2
% d = 2*(x3 -x2)
% e = 2*(y3 -y2)
% f = r2^2 - r3^2 - x2^2 - y2^2 + x3^2 + y3^2

% A solução das váriaveis é dada por :

% x = (c*e - b*f)/(a*e - b*d)
% y = (a*f - c*d)/(a*e - b*d)

% Retornando a (I) para resolver a váriavel remanecente, z:

% A*z^2 + B*z + C = 0

% Onde

% A = 1
% B = -2*zn
% C = zn^2 - r1^2 + ( x - x1 )^2 + ( y - y1 )^2

% Conhecendo os valores de x e y as duas possiveis soluções para a váriavel z são encontradas
% a partir da seguinte fórmula :

% zpm = (-B ± (B^2 -4*C)^(1/2))/(2)

% Deve ser escohida a solução da altura z que está acima da base do robô uma vez que essa é
% a unica solução fisicamente admissivel

% Esse solução simplificada do algoritimo de intersecção de três esferas falha em dois casos :

% Caso 1 : Quando o determinante da matriz de coeficientes da solução do sistema linear x, y é zero :

% I  : a*e - b*d = 2*(x3 - x1)*2*(y3 - y2) -2*(y3 - y1)*2*(x3 - x2) = 0

% Essa é uma singularidade do algoritimo cuja condição pode ser siplificada como :

% II : (x3 - x1)*(y3 - y2) = (y3 - y1)*(x3 - x2)

% Se (II) é satisfeita haverá uma singularidade. A condição de singularidade (II) é função somente
% de constantes. Portanto essa singularidade pode ser evitada por design ,isto é, posicionando a base
% do robo no plano xy. Para um robo delta simétrico essa singularidade é naturalmente evitada.

% Caso 2 : Quando o radicando da raiz de zpm é negativo a sua solução será imáginaria. A condição
% B^2 -4*C < 0 leva-a :

% (x - x1)^2 + (y -y1)^2 > r1^2

% Quando essa inigualdade é satisfeita a solução para z será imáginaria o que significa que o robô não irá
% assumir essa configuração. Essa é uma inigualdade de um circulo. Essa inigualdade nunca irá ocorrer se 
% entrada válidas forem fornecidas para a equação cinemática.

