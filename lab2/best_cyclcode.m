function [best_g, min_dist] = best_cyclcode(n, k)
%best_cyclic_code Finds the best cyclic code
%   Returns the cyclic code as the generator polynomial
%   if no such polynomial exists, returns an empty array
%   n is the length of the codeword
%   k is the number of information bits transmitted
best_g = [];
min_dist = -1;
warning('off','all');
g_candidates = cyclpoly(n, k, 'all');
warning('on','all');

possible_u = gen_nonzero_infowords(k);

for i=1:size(g_candidates, 1)
    g = g_candidates(i, :);
    dist_iter = n + 1;
    for j=1:size(possible_u, 1)
        u = possible_u(j, :);
        v = cyclencode(u, g);
        dist_iter = min(dist_iter, hamming_weight(v));
    end
    if dist_iter > min_dist
        min_dist = dist_iter;
        best_g = g;
    end
end
end
