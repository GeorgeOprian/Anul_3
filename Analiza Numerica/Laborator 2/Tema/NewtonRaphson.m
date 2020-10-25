function [x, n] = NewtonRaphson(f, df, x0, TOL)

x(1) = x0;
n = 1;
while (abs(f(x(n))) >= TOL)
    n = n + 1;
    x(n) = x(n - 1) - f(x(n - 1)) / df(x(n - 1));
    %print (x(n))
    %n = n + 1;
    %if (abs(f(x(n))) < TOL)
     %   break;
    %end
end


end

