%% Ex 2

%% a

function x=GaussSeidel(A,b,x0,ITMAX,TOL)
x_old=x0;
n=length(b);
i=0;
x=zeros(n,1);
while norm(A*x_old-b)>TOL && ITMAX>=i
    i=i+1;
%     x(1)=
    for j=1:n
        x(j)=(b(j)-A(j,1:j-1)*x(1:j-1)-A(j,j+1:n)*x_old(j+1:n))/A(j,j);
    end
%     x(n)=
    x_old=x;
end
end