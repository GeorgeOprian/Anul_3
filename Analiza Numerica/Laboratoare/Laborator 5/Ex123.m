%% Ex 1 2 3

%% b sistem 1

A=[9 1 1; 2 10 3; 3 4 11];
b=[10;19;0];
x0=zeros(3,1);
ITMAX=1000;
TOL=10^(-10);

%% b sistem 2

A=[4 -1 -1 0;-1 4  0 -1; -1 0 4 -1; 0 -1 -1 4];
b=[5;-3;-7;9];
x0=zeros(4,1);
ITMAX=1000;
TOL=10^(-10);

%% Ex 1-2
x1=Jacobi(A,b,x0,ITMAX,TOL)
x2=GaussSeidel(A,b,x0,ITMAX,TOL)

%%
norm(A*x1-b)
norm(A*x2-b)

%% Ex 3
clear; clc;
ITMAX=1000;
n=[5:8];
TOL=10.^[-14,-12:-10];

for i=1:length(n)
    n(i)
    H=hilb(n(i))
    b=[n(i):-1:1]'
%     x=H\b;
    x=inv(H)*b;
    x_tilde=CorectieReziduala(H,b,TOL,ITMAX);
    norm(H*x-b)
    norm(H*x_tilde-b)  
end

cond(H)
det(H)




