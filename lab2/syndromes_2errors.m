function syndromes = syndromes_2errors(n, k, g)
%syndromes_2errors Lists all syndromes corresponding to two errors
%   Returns a vector with the numeric representation of the syndromes
%   of errors with one or two errors, one of which is on the first position
syndromes = zeros(1, n);
error = zeros(1, n);
% 1 error in the first position
error(1) = 1;
syndromes(1) = get_syndrome_num(error, g, n, k);
% 2 errors, with one in the first position
for i=2:n
    error(i) = 1;
    syndromes(i) = get_syndrome_num(error, g, n, k);
    error(i) = 0;
end
end
