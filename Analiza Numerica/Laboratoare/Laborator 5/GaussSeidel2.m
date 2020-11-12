%% Ex 2

%% a

function x=GaussSeidel2(A,b,x0,ITMAX,TOL)
x=x0;
n=length(b);
i=0;
while norm(A*x-b)>TOL && ITMAX>=i
    i=i+1;
%     x(1)=
    for j=1:n
        x(j)=(b(j)-A(j,1:j-1)*x(1:j-1)-A(j,j+1:n)*x(j+1:n))/A(j,j);
    end
%     x(n)=
end
end