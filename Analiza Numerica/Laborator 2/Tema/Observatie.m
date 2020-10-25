f = @(x) cos(x) - x;
fd = @(x) -sin(x) - 1;
NewtonRaphson(f, fd, 0.5, 10^-5);