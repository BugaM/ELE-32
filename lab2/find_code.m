function [n, k, g] = find_code(rate, rate_tolerance, min_dist)
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
dist_iter = -1;
n = 1;
while dist_iter < min_dist
    for k=floor(n*rate*(1 + rate_tolerance)):-1:ceil(n*rate*(1 - rate_tolerance))
        [g, dist_iter] = best_cyclcode(n, k);
        if dist_iter >= min_dist
            fprintf('Gen poly found for n = %d\n', n);
            return
        end
    end
    fprintf('No gen poly found for n = %d\n', n);
    n = n + 1;
end
end
