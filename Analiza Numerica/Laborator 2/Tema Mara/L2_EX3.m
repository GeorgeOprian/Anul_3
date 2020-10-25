f =@(x)cos(x)-x;
fp=@(x)-sin(x)-1;


xz=pi/4;
TOL = 10^-5;

fplot(f,[0,pi/2]);
hold on
fplot(0, [0,pi/2]);


x = NewtonRaphson(f,fp,xz,TOL)
%plot(x)