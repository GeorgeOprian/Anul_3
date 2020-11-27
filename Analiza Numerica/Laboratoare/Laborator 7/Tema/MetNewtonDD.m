function P=MetNewtonDD(f,a,b,n)
X=linspace(a,b,n+1);
%y=f(X);
c=zeros(1,n+1);
DD = zeros(n + 1,n + 1);
DD(:,1)= f(X)';

%c(1)=y(1);
c(1)= f(1);
P=@(x)c(1);
p=@(x)1;
for i=2:n+1
    p=@(x)p(x).*(x-X(i-1));
    %c(k)=(y(k)-P(X(k)))/p(X(k));
    %c(k) = f(1:k);
    for j = 2:i
        DD(i, j) = (DD(i, j-1) - DD(i - 1, j-1))/(X(i) - X(i - j + 1));
    end
    c(i) = DD (i,i);
    P=@(x)P(x)+c(i)*p(x);
end
end