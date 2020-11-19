%% Ex 1

%% a

function C=MetNaiva2(f,n,a,b)
tic
x = linspace (a, b, n + 1);
A = zeros (n + 1);
C=zeros(1,n+1);
for i = 1: n + 1
    A(:,i)= (x.^(i - 1))';
end 
y=f(x');
% p=det(A);
p=1;
for i=n+1:-1:2
    p=p*prod(x(i)-x(1:i-1));
end
for i=1:n+1
    A_tilde=A;
    A_tilde(:,i)=y;
    C(i)=det(A_tilde)/p;
end
toc
end