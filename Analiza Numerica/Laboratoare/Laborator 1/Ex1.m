%% Ex 1

%% a

f=@(x)(x.^6-x-1);
figure(1)
fplot(f,[-2,2]);
hold on;
fplot(0,[-2,2]);
legend('f','Ox');

%% b

a=1;
b=2;
TOL=10^(-5);

n=1;
x(n)=(a+b)/2;

while abs(f(x(n)))>TOL
    if f(a)*f(x(n))<0
        b=x(n);
    else
        a=x(n);
    end
    n=n+1;
    x(n)=(a+b)/2;
end
n
x(n)

%% c

syms xs
fs=symfun(xs.^6-xs-1,xs);
double(solve(fs==0))