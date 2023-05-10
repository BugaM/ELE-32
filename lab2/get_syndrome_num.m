function syndrome_num = get_syndrome_num(v, g, n, k)
%get_syndrome_num Calculates the codeword's syndrome
%   Calculates the codeword's syndrome which indicates the error
%   The syndrome is represented as a number for easier comparisons
syndrome = get_syndrome(v, g, n, k);
syndrome_num = syndrome2num(syndrome);
end
