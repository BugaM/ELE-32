function syndrome_num = get_syndrome_num(v, g, n, k)
%UNTITLED17 Summary of this function goes here
%   Detailed explanation goes here
syndrome = get_syndrome(v, g, n, k);
syndrome_num = syndrome2num(syndrome);
end
