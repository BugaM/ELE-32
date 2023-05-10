function product = multpoly(u, v)
%multpoly Multiplies two polymials
%   Returns u*v
product = mod(conv(u, v), 2);
end
