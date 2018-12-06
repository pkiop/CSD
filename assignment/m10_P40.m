syms x;
temp = (x+5) * (x^2 + 1.2*x + 9);
expand(temp);

%x^3 + (31*x^2)/5 + 15*x + 45

K = 5 * 0.5 * 9;
G = tf([K],[1 31/5 15 45]);
T = feedback(G, 1)

bode(T)

