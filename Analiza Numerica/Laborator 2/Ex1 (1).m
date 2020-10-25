%% Ex 2

%% b1

f=@(x)x.^3+4*x.^2-10
figure(1)
fplot(f,[1,2])
hold on
fplot(0,[1,2])
legend('f','Ox')

%% b2

syms xs
fs=symfun(xs^3+4*xs^2-10,xs)
x_star=double(solve(fs==0))
% x_star=x_star(1)
x_star=x_star(imag(x_star)==0 & real(x_star)>=1 & real(x_star)<=2)


%% b3

phi{1}=symfun(-xs^3-4*xs^2+xs+10,xs);
phi{2}=symfun(sqrt(10/xs-4*xs),xs);
phi{3}=symfun(1/2*sqrt(10-xs^3),xs);
phi{4}=symfun(sqrt(10/(xs+4)),xs);

for j=1:4
    dphi{j}=abs(diff(phi{j}));
end

%%

figure(2)
for j=1:4
    subplot(2,4,j)
    ezplot(phi{j},[1,2]);
    subplot(2,4,j+4)
    ezplot(dphi{j},[1,2]);
end

%% b4

x0=1;
N=20;

x3=double(MetPunctFix(phi{3},x0,N))
x4=double(MetPunctFix(phi{4},x0,N))

err_abs3=abs(x_star-x3)
err_abs4=abs(x_star-x4)

%%
figure(3)
loglog(err_abs3);
hold on;
loglog(err_abs4);
legend('err phi3','err phi4')

