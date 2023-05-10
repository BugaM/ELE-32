function cycledpoly = cycle_poly(poly, n, i)
%cycle_poly Rotates a polynomial circularly
%   Rotates the polynomial poly
%   i steps to the right circularly
%   The cycle has n positions.
i = mod(i, n);

% Add zero padding
if length(poly) < n
    poly = [poly zeros(1, n - length(poly))];
end

% Rotate circularly
cycledpoly = [poly(i + 1:end) poly(1:i)];
end
