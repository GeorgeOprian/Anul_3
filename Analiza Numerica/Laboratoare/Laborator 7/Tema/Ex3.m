%%
%Tema realizata de Boranescu Alexandru si Oprian George
f = @(x) exp(2 * x);

xi = -1;
xf = 1;
n = 3;
P = MetNewtonDD(f, xi, xf, n);
%vpa(simplify(sym(P)))
%% b1)
figure(1)
fplot(f,[xi,xf]);
hold on;
fplot(P,[xi,xf]);
legend('functia f','Polinomul de interpolare Lagrange');

%% b2)
err_abs=@(x)abs(f(x)-P(x));
figure(2)
fplot(err_abs,[xi, xf]);
title('Eroare absoluta');
