clc; clear;
syms xs;
fs  = symfun(xs^3 - 4*xs^2+5*xs-2, xs);
dfs = diff(fs);
f  = matlabFunction (fs);
df = matlabFunction (dfs);

x0 = 0;
ITMAX = 20;
TOL = 10^(-10);
phi = matlabFunction (xs - fs / dfs);

[x1,n1, ea1, er1] = Aitken (f, phi, x0, ITMAX, TOL);
[x2,n2, ea2, er2] = Steffensen(f, phi, x0, ITMAX, TOL);
[x3,n3, ea3, er3] = NRclasic(f, phi, x0, ITMAX, TOL);


Tabel1=table((1:n1)',x1',[1 ea1]',[1 er1]','VariableNames',{'iteratie','aprox','Eroare_absoluta','Eroare_relativa'})

Tabel2=table((1:n2)',x2',[1 ea2]',[1 er2]','VariableNames',{'iteratie','aprox','Eroare_absoluta','Eroare_relativa'})
Tabel3=table((1:n3)',x3',[1 ea3]',[1 er3]','VariableNames',{'iteratie','aprox','Eroare_absoluta','Eroare_relativa'})
