function weight = hamming_weight(vec)
%hamming_weight Calculates the hamming weight of a vector
%   The hamming weight is the number of non-zero entries of the vector
weight = sum(vec ~= zeros(1, length(vec)));
end
