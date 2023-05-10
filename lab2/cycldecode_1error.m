function [fixed_codeword, worked] = cycldecode_1error(codeword, n, k, g, syndrome_1error)
%UNTITLED22 Summary of this function goes here
%   Detailed explanation goes here
rotations = 0;
syndrome = get_syndrome(codeword, g, n, k);
syndrome_num = syndrome2num(syndrome);
while (rotations < n)
    if syndrome_num == 0
        worked = true;
        fixed_codeword = cycle_poly(codeword, n, -rotations);
        return
    end
    % Known syndrome found
    if syndrome_num == syndrome_1error
        % Fix the error that is on the first position
        codeword(1) = ~codeword(1);
        % Get new syndrome
        syndrome = get_syndrome(codeword, g, n, k);
        syndrome_num = syndrome2num(syndrome);
    % No known syndrome found, rotate it
    else
        % Rotate syndrome with respect to g
        %syndrome = cycle_poly_g(syndrome, g);
        %syndrome_num = syndrome2num(syndrome);
        % Rotate codeword
        codeword = cycle_poly(codeword, n, 1);
        rotations = rotations + 1;
        % Get new syndrome
        syndrome = get_syndrome(codeword, g, n, k);
        syndrome_num = syndrome2num(syndrome);
    end
end
% Un-rotate codeword
worked = false;
fixed_codeword = cycle_poly(codeword, n, -rotations);
end
