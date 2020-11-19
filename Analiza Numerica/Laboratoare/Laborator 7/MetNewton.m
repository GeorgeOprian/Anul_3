%% Ex 1

%% a

function P=MetNewton(f,a,b,n)
X=linspace(a,b,n+1);
y=f(X);
c=zeros(1,n+1);
c(1)=y(1);
P=@(x)c(1);
p=@(x)1;
for k=2:n+1
    p=@(x)p(x).*(x-X(k-1));
    c(k)=(y(k)-P(X(k)))/p(X(k));
    P=@(x)P(x)+c(k)*p(x);
end
end