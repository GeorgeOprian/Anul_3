%% Ex 2

%% a

function P=MetLagrange(f,n,a,b)
X = linspace (a, b, n + 1);
y=f(X');
L=cell(1,n+1);
P=@(x)0;
for i=1:n+1
    L{i}=@(x)1;
    
%     for j=1:i-1
%         L{i}=@(x)L{i}(x)*(x-X(j))./(X(i)-X(j));
%     end
%     for j=i+1:n+1
%         L{i}=@(x)L{i}(x)*(x-X(j))./(X(i)-X(j));
%     end

    L{i}=@(x)L{i}(x)*prod(x-X([1:i-1,i+1:n+1]))./(X(i)-X([1:i-1,i+1:n+1]));
    
    P=@(x)P(x)+y(i)*L{i}(x);
end
end