function [code] = bsc(code,p)
%BSC Summary of this function goes here
%   Detailed explanation goes here
size = length(code);
for i=1:size
    if rand(1) < p
        code(i) = ~code(i);
    end
end
end

