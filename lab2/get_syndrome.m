function syndrome = get_syndrome(codeword, g, n, k)
%get_syndrome Calculates the codeword's syndrome
%   Calculates the codeword's syndrome which indicates the error
%   The syndrome is represented normally, i.e., as a polynomial
[~, syndrome] = divpoly(codeword, g);

% Trims extra zeros if syndrome size is too large
if length(syndrome) >= n - k - 1
    syndrome = syndrome(1: n - k -1);
% Adds zero padding if syndrome size is too small
else
    syndrome = [syndrome zeros(1, n - k - 1 - length(syndrome))];
end
end
