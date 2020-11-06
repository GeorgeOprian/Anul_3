
function [x,n, ea, er]=NRm2(f,df,d2f,x0,ITMAX,TOL)
x(1)=x0;
x(2)=x(1)-f(x(1))*df(x(1))/(df(x(1))^2-f(x(1))*d2f(x(1)));
n=2;

ea(1)= abs(x(2)-x(1));
er(1)=abs(x(2)-x(1))/abs(x(2));

while n<=ITMAX && abs(f(x(n)))>TOL && ea(n-1)>TOL && er(n-1)>TOL
   n=n+1;
   x(n)=x(n-1)-f(x(n-1))*df(x(n-1))/(df(x(n-1))^2-f(x(n-1))*d2f(x(n-1)));
   
   ea(n-1)=abs(x(n)-x(n-1));
   er(n-1)=abs(x(n)-x(n-1))/abs(x(n));
   
end

end