%% Ex 1 

%% b

f = @(x) exp(2*x);
a = -1;
b = 1;
n = 3;

%% 1
C=MetNaiva(f, n, a, b);
P=@(t)C(1);
for i=2:n+1
    P = @(t) P(t)+C(i) * t.^(i-1);
end

%% 2
P=MetLagrange(f,n,a,b)
vpa(simplify(sym(P)))

%%
figure(1)
fplot(f,[a,b]);
hold on;
fplot(P,[a,b]);
legend('f','P');

%%
err_abs=@(x)abs(f(x)-P(x));
figure(2)
fplot(err_abs,[a,b]);
title('Eroare absoluta');




