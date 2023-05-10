function [fixed_codeword, worked] = cycldecode_2errors(codeword, n, k, g, syndromes_2errors)
%UNTITLED25 Summary of this function goes here
%   Detailed explanation goes here
rotations = 0;
syndrome = get_syndrome(codeword, g, n, k);
syndrome_num = syndrome2num(syndrome);
while (rotations < n)
    % Known syndrome found
    if sum(syndrome_num == syndromes_2errors) ~= 0
        % Fix the error that is on the first position
        codeword(1) = ~codeword(1);
        % Fixed one of two errors
        worked = true;
        fixed_codeword = cycle_poly(codeword, n, -rotations);
        return
    % No known syndrome found, rotate it
    else
        % Rotate syndrome with respect to g
        syndrome = cycle_poly_g(syndrome, g);
        syndrome_num = syndrome2num(syndrome);
        % Rotate codeword
        codeword = cycle_poly(codeword, n, 1);
        rotations = rotations + 1;
    end
end
% Un-rotate codeword
worked = false;
fixed_codeword = cycle_poly(codeword, n, -rotations);
end
