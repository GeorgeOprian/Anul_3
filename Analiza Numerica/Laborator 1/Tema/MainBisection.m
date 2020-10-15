clc;
clear;
syms x;
f = symfun(x.^2 - 3, x);
a = 1;
b = 2;
TOL = 10 ^ -10;

[x, n] = Bisection(f, a, b, TOL, 1);
fprintf('OPT = 1: solutia = %f nrPasi = %i\n', x, n); 
[x, n] = Bisection(f, a, b, TOL, 3);
fprintf('OPT = 2: solutia = %f nrPasi = %i\n', x, n);
[x, n] = Bisection(f, a, b, TOL, 3);
fprintf('OPT = 3: solutia = %f nrPasi = %i\n', x, n);
