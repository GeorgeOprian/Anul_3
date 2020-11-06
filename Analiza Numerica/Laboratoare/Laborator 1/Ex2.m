%% Ex 2

%% a
g=@(x) exp(-x).*(x.^2-5*x+2)-1;
fplot(g, [-3,3]);
hold on;
fplot(0, [-3,3]);
axis([-5 5 -5 5]);

%% b

a=-1;
b=1;

n=1;
x(n)=(a+b)/2;

for n=1:9
    if g(a)*g(x(n))<0
        b=x(n);
    else
        a=x(n);
    end
    x(n+1)=(a+b)/2;
end
x(10)

%% c

syms xs
gs=symfun(exp(-xs).*(xs.^2-5.*xs+2)-1,xs);

x_star=double(solve(gs==0));
x = -1: 0.0001: 1;
err_abs=abs(x_star-x);

err_rel=err_abs/abs(x_star);

figure(2)
plot(err_abs)
figure(3)
plot(err_rel)

%%
figure(4)
loglog(err_abs)

%% d

x0=0
fzero(gs,x0)