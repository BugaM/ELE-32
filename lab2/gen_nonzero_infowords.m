function possible_u = gen_nonzero_infowords(k)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
two_to_power_k = 2^k;
possible_u = zeros(two_to_power_k - 1, k);
counter = 1;

for i=1:(two_to_power_k - 1)
    aux = counter;
    for j=1:k
        possible_u(i, j) = rem(aux, 2);
        aux = floor(aux/2);
    end
    counter = counter + 1;
end

end
