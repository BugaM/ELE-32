function v = cyclencode(u, g)
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here
v = rem(conv(u, g), 2);
end

