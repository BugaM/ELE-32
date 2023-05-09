function [n, k, g] = find_code(rate, rate_tolerance, max_dist)
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
max_dist_iter = -1;
n = 1;
while max_dist_iter < max_dist
    for k=floor(n*rate*(1 + rate_tolerance)):-1:ceil(n*rate*(1 - rate_tolerance))
        [g, max_dist_iter] = best_cyclcode(n, k);
        if max_dist_iter >= max_dist
            return
        end
    end
    fprintf('No gen poly found for n = %d\n', n);
    n = n + 1;
end
end
