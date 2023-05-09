function product = multpoly(u, v)
%UNTITLED12 Summary of this function goes here
%   Detailed explanation goes here
product = mod(conv(u, v), 2);
end
