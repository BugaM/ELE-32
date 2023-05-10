% Encoding parameters
rate = 4/7;
rate_tolerance = 0.1;
min_dist = 5;
max_errors_fixed = (min_dist - 1)/2;

% Finding code
[n, k, g] = find_code(rate, rate_tolerance, min_dist);
syndromes = syndromes_2errors(n, k, g);

% Encoding
infoword = ones(1, k);
codeword = cyclencode(infoword, g);

% Decoding
% Testing if it works with 0 errors
infoword_dec = cycldecode(codeword, n, k, g, syndromes, max_errors_fixed);
if sum(abs(infoword - infoword_dec)) == 0
    fprintf("Worked when there are no errors.\n")
end
% Testing if it works with 1 error
worked = true;
for i=1:n
    infoword_dec = cycldecode(codeword, n, k, g, syndromes, max_errors_fixed);
    if sum(abs(infoword - infoword_dec)) ~= 0
        worked = false;
        break
    end
end
if worked
    fprintf("Worked when there is one error.\n")
end
% Testing if it works with 2 errors
worked = true;
for i=1:(n-1)
    for j=(i+1):n
        infoword_dec = cycldecode(codeword, n, k, g, syndromes, max_errors_fixed);
        if sum(abs(infoword - infoword_dec)) ~= 0
            worked = false;
            break
        end
    end
    if ~worked
        break
    end
end
if worked
    fprintf("Worked when there are two errors.\n")
end
