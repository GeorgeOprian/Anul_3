%% Ex 1

%% a

function C=MetNaiva(f,n,a,b)
tic
x = linspace (a, b, n + 1);
A = zeros (n + 1);
for i = 1: n + 1
    A(:,i)= (x.^(i - 1))';
end 
y=f(x');
C = A\y; % folsind solver MATLAB pentru a rezolva sistem A*C=y
toc
end