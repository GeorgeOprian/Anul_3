%% Ex 1 

%% a

figure(1);
fplot(@f,[0, 1.75]);
hold on;
fplot(0, [0, 1.75]);
figure(2);
fplot(@df,[0, 1.75]);
hold on;
fplot(0, [0, 1.75]);

%% e

x0=0;
ITMAX=20;
TOL=10^(-10);
m=2;

d2f=@(x)6*x-8;

[x1,n1,]=NRm1(m,@f,@df,x0,ITMAX,TOL)
%%
[x2,n2, ea2, er2]=NRm2(@f,@df,d2f,x0,ITMAX,TOL)
[x,n, ea, er]=NRclasic(@f,@df,x0,ITMAX,TOL)

%%
Tabel1=table((1:n1)',x1',[1 ea1]',[1 er1]','VariableNames',{'iteratie','aprox','ea','er'})
%%
Tabel2=table((1:n2)',x2',[1 ea2]',[1 er2]','VariableNames',{'iteratie','aprox','ea','er'})

Tabelclasic=table((1:n)',x',[1 ea]',[1 er]','VariableNames',{'iteratie','aprox','ea','er'})
