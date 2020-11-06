%% Ex 2

%% a

function [x_hat,n, ea, er]=Aitken(f,phi,x0,ITMAX,TOL)
x(1)=x0;
x(2)=phi(x(1));
x_hat(1:2)=x(1:2);
n=2;

ea(1) = abs(x_hat(2)-x_hat(1));
er(1) = abs(x_hat(2)-x_hat(1))/abs(x_hat(2));

while abs(f(x_hat(n)))>TOL && n<=ITMAX && abs(x_hat(n)-x_hat(n-1))>TOL &&...
        abs(x_hat(n)-x_hat(n-1))/abs(x_hat(n))>TOL
    n=n+1;
    x(n)=phi(x(n-1));
    x_hat(n)=A(x(n),x(n-1),x(n-2));
    ea(n-1) = abs(x_hat(n)-x_hat(n-1));
    er(n-1) = abs(x_hat(n)-x_hat(n-1))/abs(x_hat(n));
end
end