%% Ex 2

%% c

function x=NewtonRaphsonf
x0=0;
x(1)=x0;
for n=2:10
    x(n)=x(n-1)-Functiaf(x(n-1))/Derivataf(x(n-1));
end
end