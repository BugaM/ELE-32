function syndrome = get_syndrome(v, g, n, k)
%UNTITLED11 Summary of this function goes here
%   Detailed explanation goes here
[~, syndrome] = divpoly(v, g);
if length(syndrome) >= n - k - 1
    syndrome = syndrome(1: n - k -1);
else
    syndrome = [syndrome zeros(1, n - k - 1 - length(syndrome))];
end
end
