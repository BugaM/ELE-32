function infoword = cycldecode(codeword, n, k, g, syndromes)
%cycldecode Decodes a cyclic code, using its parameters
%   Decodes the cylic code
%   n is the length of the codeword
%   k is the number of information bits transmitted
%   g is the generating polynomial
%   syndromes is a list of syndromes corresponding to erros patterns
%   that can be fixed
%   max_errors_fixed is the maximum amount of errors that can be fixed

syndrome_1error = syndromes(1);
syndromes_2errors = syndromes(2:end);

[fixed_codeword, worked] = cycldecode_1error(codeword, n, k, g, syndrome_1error);

if worked
    codeword = fixed_codeword;
else
    [fixed_codeword, worked] = cycldecode_2errors(codeword, n, k, g, syndromes_2errors);
    if worked
        [fixed_codeword, worked] = cycldecode_1error(fixed_codeword, n, k, g, syndrome_1error);
        if worked
            codeword = fixed_codeword;
        end
    end
end

% Decode it
[infoword, ~] = divpoly(codeword, g);
infoword = infoword(1:k);
end
