function [n, k, g] = find_code(rate, rate_tolerance, min_dist)
%find_code Finds a cylic code with the requirements
%   Finds a cyclic code with the requirements
%   and the smallest word size and the highest rate
dist_iter = -1;
n = 1;
while dist_iter < min_dist
    for k=floor(n*rate*(1 + rate_tolerance)):-1:ceil(n*rate*(1 - rate_tolerance))
        [g, dist_iter] = best_cyclcode(n, k);
        if dist_iter >= min_dist
            return
        end
    end
    n = n + 1;
end
end
