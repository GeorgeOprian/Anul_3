%% Ex 1

%% a

function P=MetNeville(f,a,b,n)
X=linspace(a,b,n+1);
y=f(X);
q=cell(n+1);
for i=1:n+1
    q{i, 1} = @(x)y(i);
end
for i = 2:n+1
    for j = 2:i
        q{i, j} = @(x)(q{i, j-1}(x).* (x - X(i-j+1)) - q{i-1,j-1}(x).*(x - X(i)))/(X(i) - X(i-j+1));
    end
end
P = q{n+1, n+1};
% P=@(x)q{n+1, n+1}(x);
end