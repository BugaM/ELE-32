function possible_u = gen_nonzero_infowords(k)
%gen_nonzero_infowords Creates all non-zero infowords
%   Creates all non-zero infowords and
%   store each as a line in the matrix
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
