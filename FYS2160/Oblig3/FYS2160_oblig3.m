%---Constants---
N = 10;
T = 0.9;

V = linspace(1/2., 1/0.2, N);

%---Declare arrays---
p = zeros(N,1);
g = zeros(N,1);

for i = 1:N
   p(i) = 8*T/(3*V(i)-1)-3/V(i)^2;
   g(i) = -3./V(i)-(8/3.)*T*log(3*V(i)-1)+p(i)*V(i);
end;
[p0,g0,segments]=selfintersect(p,g)
plot(p0,g0,'g')
hold on;
plot(p,g,'b',p0,g0,'.r')
axis ('equal'); grid