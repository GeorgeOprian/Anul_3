%% Ex 3

%% a

function x_tilde=CorectieReziduala(A,b,TOL,ITMAX)
% x_tilde=A\b; % rez Ax=b folosind solver MatLab
x_tilde=inv(A)*b;
r=b-A*x_tilde;
it=0;
while norm(r)>TOL %&& it<=ITMAX
    it=it+1;
%     deltax=A\r;
    deltax=inv(A)*r;
    x_tilde=x_tilde+deltax;
    r=b-A*x_tilde;
end
end