function [quotient, remainder] = divpoly(u, v)
%UNTITLED13 Divides u by v
%   Finds quotient and remainder such that: u = q*v + r

u = flip(u);
v = flip(v);

start_v = 1;
while v(start_v) == 0
   start_v = start_v + 1;
end
v = v(start_v:end);

[quotient, remainder] = deconv(u, v);
quotient = flip(mod(quotient, 2));
remainder = flip(mod(remainder, 2));
end
