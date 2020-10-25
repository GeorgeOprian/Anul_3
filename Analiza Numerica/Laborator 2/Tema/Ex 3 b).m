%% b)
%f = @(x) cos(x) - x;
%df = @(x) -sin(x) - 1;
syms xs;
fs = symfun(cos(xs) - xs, xs);
dfs = diff(fs);
f = matlabFunction(fs);
df = matlabFunction(dfs);

x0 = pi/4;
TOL = 10 ^ -5;
xAprox = NewtonRaphson(f, df, x0, TOL);


fplot(f, [0, pi/2]);
hold on;
fplot(0, [0, pi/2]);
scatter(xAprox, f(xAprox));
legend ('f', 'y = 0', 'aproximari');


%%
for i = 1:2:5
   i 
end

