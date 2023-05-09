function syndromes = syndromes_2errors(n, k, g)
%UNTITLED16 Summary of this function goes here
%   Detailed explanation goes here
syndromes = zeros(1, n);
error = zeros(1, n);
error(1) = 1;
syndromes(1) = get_syndrome_num(error, g, n, k);
for i=2:n
    error(i) = 1;
    syndromes(i) = get_syndrome_num(error, g, n, k);
    error(i) = 0;
end
end
