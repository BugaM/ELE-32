% Encoding parameters
rate = 4/7;
rate_tolerance = 0.1;
min_dist = 5;

% Finding code
[n, k, g] = find_code(rate, rate_tolerance, min_dist);
syndromes = syndromes_2errors(n, k, g);

% Encoding
infoword = zeros(1, k);
codeword = cyclencode(infoword, g);

% Decoding
% Testing if it works with 0 errors
infoword_dec = cycldecode(codeword, n, k, g, syndromes);
if sum(abs(infoword - infoword_dec)) == 0
    fprintf("Worked when there are no errors.\n")
end
% Testing if it works with 1 error
worked = true;
for i=1:n
    codeword(i) = ~codeword(i);
    infoword_dec = cycldecode(codeword, n, k, g, syndromes);
    if sum(abs(infoword - infoword_dec)) ~= 0
        worked = false;
        break
    end
    codeword(i) = ~codeword(i);
end
if worked
    fprintf("Worked when there is one error.\n")
end
% Testing if it works with 2 errors
worked = true;
for i=1:(n-1)
    codeword(i) = ~codeword(i);
    for j=(i+1):n
        codeword(j) = ~codeword(j);
        infoword_dec = cycldecode(codeword, n, k, g, syndromes);
        codeword(j) = ~codeword(j);
        if sum(abs(infoword - infoword_dec)) ~= 0
            worked = false;
            break
        end
    end
    codeword(i) = ~codeword(i);
    if ~worked
        break
    end
end
if worked
    fprintf("Worked when there are two errors.\n")
end
