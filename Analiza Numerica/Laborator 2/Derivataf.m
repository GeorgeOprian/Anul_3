%% Ex 2

%% b

function y=Derivataf(x)
y=1-2*x.*exp(-x.^2).*cos(x)-exp(-x.^2)*sin(x);
end