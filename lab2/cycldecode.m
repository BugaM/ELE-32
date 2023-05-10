function infoword = cycldecode(codeword, n, k, g, syndromes, max_errors_fixed)
%cycldecode Decodes a cyclic code, using its parameters
%   Decodes the cylic code
%   n is the length of the codeword
%   k is the number of information bits transmitted
%   g is the generating polynomial
%   syndromes is a list of syndromes corresponding to erros patterns
%   that can be fixed
%   max_errors_fixed is the maximum amount of errors that can be fixed
errors_fixed = 0;
rotations = 0;
syndrome = get_syndrome(codeword, g, n, k);
syndrome_num = syndrome2num(syndrome);
while (syndrome_num ~= 0) && (errors_fixed < max_errors_fixed)
    % Known syndrome found
    if sum(syndrome_num == syndromes) ~= 0
        % Fix the error that is on the first position
        errors_fixed = errors_fixed + 1;
        codeword(1) = ~codeword(1);
        % Get new syndrome
        syndrome = get_syndrome(codeword, g, n, k);
        syndrome_num = syndrome2num(syndrome);
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
codeword = cycle_poly(codeword, n, -rotations);
% Decode it
[infoword, ~] = divpoly(codeword, g);
infoword = infoword(1:k);
end
