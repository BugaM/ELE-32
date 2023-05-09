function cycledpoly = cycle_poly(poly, n, i)
%UNTITLED10 Summary of this function goes here
%   Detailed explanation goes here
one_plus_D_n = zeros(1, n + 1);
one_plus_D_n(1) = 1;
one_plus_D_n(end) = 1;

i = mod(i, n);

% Add zero padding and multiply by D^i
poly = [zeros(1, n - length(poly)) poly zeros(1, i)];

[~, cycledpoly] = deconv(poly, one_plus_D_n);

cycledpoly = mod(cycledpoly, 2);
cycledpoly = cycledpoly(length(cycledpoly) - n + 1:end);

end
