function infoword = cycldecode(codeword, n, k, g, syndromes, max_errors_fixed)
%UNTITLED19 Summary of this function goes here
%   Detailed explanation goes here
errors_fixed = 0;
rotations = 0;
syndrome = get_syndrome(codeword, g, n, k);
syndrome_num = syndrome2num(syndrome);
while (syndrome_num ~= 0) && (errors_fixed < max_errors_fixed)
    if sum(syndrome_num == syndromes) ~= 0
        errors_fixed = errors_fixed + 1;
        codeword(1) = ~codeword(1);
        syndrome = get_syndrome(codeword, g, n, k);
        syndrome_num = syndrome2num(syndrome);
    else
        rotations = rotations + 1;
        syndrome = cycle_poly_g(syndrome, g);
        syndrome_num = syndrome2num(syndrome);
        codeword = cycle_poly(codeword, n, 1);
    end
end

codeword = cycle_poly(codeword, n, -rotations);
[infoword, ~] = divpoly(codeword, g);
infoword = infoword(1:k);
end
