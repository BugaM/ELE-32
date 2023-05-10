P = [0.5, 0.2, 0.1];


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



probabilities = get_probabilities(P);
sz = length(probabilities);
pe = zeros(1, sz);

for i = 1:sz 
    p = probabilities(i)
    chebyshev = ceil(8000/p);
    chebyshev_n = ceil(chebyshev/k);
    error_count = 0;
    for j = 1:chebyshev_n
        bsc_out = bsc(codeword,p);
        decode = cycldecode(bsc_out, n, k, g, syndromes);
        error_count = error_count + sum(decode);
    end
    pe(i) = error_count/(chebyshev_n*k);
end
pe
