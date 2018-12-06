c = s * (s + 1) * (s + 15);
cc = expand(c)
% 1 16 15 0

temp = [1 16 15 0];
G1 = tf([1],temp);

K = 30;

[UP, DOWN] = pade(0.2,1);
G2 = tf(UP,DOWN);

G = G1 * G2
T = feedback(K*G1, 1)

bode(T)

%? 10.73
syms x
ss = ((2*x)/sqrt(-2*x^2 + sqrt(1+4*x^4))-tan(-135) == 0)
anss=solve(ss, x);

xx = 0.443

OS = exp(-(xx*pi/sqrt(1-xx^2)))*100



