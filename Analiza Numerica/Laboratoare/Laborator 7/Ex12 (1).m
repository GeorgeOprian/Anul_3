%% Ex 1

%% b

f=@(x)exp(2*x);
a=-1;
b=1;
n=5;

%% 1
P=MetNeville(f,a,b,n)

%% 2
P=MetNewton(f,a,b,n)

%%
figure(1)
fplot(f,[a,b]);
hold on;
pause(1.5);
fplot(P,[a,b]);
legend('f','P');

%%
figure(2)
err_abs=@(t)abs(f(t)-P(t));
fplot(err_abs,[a,b]);
