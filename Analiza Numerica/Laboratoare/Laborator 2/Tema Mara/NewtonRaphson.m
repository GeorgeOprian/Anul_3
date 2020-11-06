function x = NewtonRaphson(f,fp,xz,TOL)

x(1)=xz;
n=2;
while abs(f(x(n-1)))>= TOL
    x(n)=x(n-1)-f(x(n-1))/fp(x(n-1));
    n=n+1;
    
end
end

