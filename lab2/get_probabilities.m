function [x] = get_probabilities(P)
    x = [];
    while P(end) > 1e-5
        x = [x P];
        P = P/10;
    end
end

