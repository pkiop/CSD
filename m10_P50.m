A = [25 25*1.2 25*12500];
B = [1 5.6 62000 0];
G = tf(A,B);
Kp = input('input : ');
Gp = (feedback(Kp*G,1));
bode(Gp);

[M, P, w] = bode(Gp);
[Mp i] = max(M);
Mp
MpdB = 20 * log10(Mp)
wp = w(i)
for i=1:1:length(M);
    if M(i) <= 0.707;
        fprintf('Bandwidth = %g', w(i))
        break
    end
end    
