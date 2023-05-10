function cycled_poly = cycle_poly_g(poly, g)
%cycle_poly_g Rotates a polynomial with respect to g
%   Rotates the polynomial poly one step to the right
%   with respect to another polynomial g
sum_factor = g(1:length(poly));

poly_end = poly(end);

cycled_poly = [0 poly(1:length(poly) - 1)];

if poly_end == 1
    cycled_poly = mod(cycled_poly + sum_factor, 2);
end
end
