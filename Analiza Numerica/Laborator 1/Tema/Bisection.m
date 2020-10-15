function [sol, n] = Bisection(f,a, b, TOL, OPT)

switch (OPT)
    case 1
        n=1;
        x(n)=(a+b)/2;
        while abs(b - a)>TOL
            if f(a)*f(x(n))<0
                b=x(n);
            else
                a=x(n);
            end
            n=n+1;
            x(n)=(a+b)/2;
        end
        sol = x(n);
        
    case 2
        n=1;
        x(n)=(a+b)/2;
        while 1 %simulez un do while
            if f(a)*f(x(n))<0
                b=x(n);
            else
                a=x(n);
            end
            n=n+1;
            x(n)=(a+b)/2;
            if ((abs(x(n) - x(n - 1)) / abs(x(n - 1))) > TOL)
                break;
            end
        end
        sol = x(n);
    case 3
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
        sol = x(n);
        
end