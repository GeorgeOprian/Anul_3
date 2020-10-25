%% Ex 2

%% a

f=@(x)x+exp(-x.^2).*cos(x);
figure(1)
fplot(f,[-1,1]);
hold on;
fplot(0,[-1,1]);

%% d

syms xs
fs=symfun(xs+exp(-xs.^2).*cos(xs),xs)

x_star=double(solve(fs==0))

x=NewtonRaphsonf

err_abs=abs(x_star-x)

figure(2)
loglog(err_abs)
