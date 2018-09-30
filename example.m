% ---a---

UP = [1 5];
DOWN = [1 4 16 0];

G = tf(UP,DOWN)

K = input('Type K : ');

% ---b, c---
T = feedback(K*G, 1)
bode(T)

[M, P, w] = bode(T);
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


