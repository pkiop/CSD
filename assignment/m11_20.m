numg = 0.1111*[4 5 1];
deng = poly([4 3.1 0.85 0.87 0.1111]);
G = tf(numg, deng);
'G(s)'
Gzpk = zpk(G)

Po = 13
Ts = 500
T = feedback(G,1);
step(T)
title('Gain Compensated')
pause

z = (-log(Po/100)) / (sqrt(pi^2 + log(Po/100) ^ 2));
wn = 4/ (z* Ts);

wBW = wn*sqrt((1-2*z^2) + sqrt (4*z^4 - 4*z^2 + 2));

Pmreq = atan(2*z / (sqrt(-1*z^2 + sqrt(1+4*z^4))))*(180/pi) + 5;

wpm = 0.8*wBW;

[M, P] = bode(G,wpm);
Pmreqc = Pmreq - (180 + P);
beta = (1 - sin(Pmreqc*pi/180)) / (1 + sin(Pmreqc*pi / 180));

fprintf('\nPercent Overshoot = %g', Po)
fprintf('\nSettling Time = %g', Ts)
fprintf('\nDamping Ratio = %g', z)
fprintf('\nRequired Phase Margin = %g', Pmreq);
fprintf('\nRequired Bandwidth = %g', wBW);
fprintf('\nNew Phase Margin Frequency = %g', wpm);
fprintf('\nRequired Phase from Lead Compensator = %g', Pmreqc);
fprintf('\nBeta = %g', beta);

bode(numg, deng)
title('Gain compensated')
pause

zclag = wpm / 10;
pclag = zclag * beta;
Kclag = beta;
'Lag compensator'
'Gclag'
Gclag = tf(Kclag * [1 zclag], [1 pclag]);
Gclagzpk = zpk(Gclag)
zclead = wpm * sqrt(beta);
pclead = zclead/beta;
Kclead = 1 / beta;
'Lead compensator'
'Gclead'
Gclead = tf(Kclead*[1 zclead], [1 pclead]);
Gcleadzpk = zpk(Gclead)

'Gclag(s)Gclead(s)G(s)'
Ge = G*Gclag*Gclead;
Gezpk = zpk(Ge)

T = feedback(Ge,1);
bode(Ge)
title('Lag - lead Compensated')

[M,P,w] = bode(Ge);
[Gm,Pm,wcp,wcg] = margin(M,P,w);
title('Lag-lead Compensated')






















