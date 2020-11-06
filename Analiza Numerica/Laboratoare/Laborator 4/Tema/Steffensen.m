function [x_hat,n, ea, er]=Steffensen(f,phi,x0,ITMAX,TOL)

x_hat(1)=x0;
x_hat(2) = phi(x_hat(1));
n=2;
ea(1) = abs(x_hat(2)-x_hat(1));
er(1) = abs(x_hat(2)-x_hat(1))/abs(x_hat(2));

while abs(f(x_hat(n)))>TOL && n<ITMAX && abs(x_hat(n)-x_hat(n - 1))>TOL &&...
       abs(x_hat(2)-x_hat(1))/abs(x_hat(2)) >TOL
    
    n=n+1;
    x_hat(n)=phi(x_hat(n-1));
    if(mod(n-1, 3) ==0)        
        x_hat(n)= A( x_hat(n-1), x_hat(n-2), x_hat(n-3)); 
    else
        x_hat(n) = phi(x_hat(n-1));    
    end
    ea(n-1) = abs(x_hat(n)-x_hat(n-1));
    er(n-1) = abs(x_hat(n)-x_hat(n-1))/abs(x_hat(n));
end
end
