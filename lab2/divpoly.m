function [quotient, remainder] = divpoly(u, v)
%divpoly Divides u by v
%   Finds quotient and remainder such that: u = q*v + r

% Flips for coefficients to be in decreasing order of exponents
u = flip(u);
v = flip(v);
% Remove trailling zeros for v
start_v = 1;
while v(start_v) == 0
   start_v = start_v + 1;
end
v = v(start_v:end);
% Do the division
[quotient, remainder] = deconv(u, v);
% Flip back the results
quotient = flip(mod(quotient, 2));
remainder = flip(mod(remainder, 2));
end
