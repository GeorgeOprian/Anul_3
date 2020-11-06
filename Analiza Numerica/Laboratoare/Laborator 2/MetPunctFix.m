%% Ex 1

%% a

function x=MetPunctFix(phi,x0,N)
x(1)=phi(x0);
for i=2:N
    x(i)=phi(x(i-1));
end
end