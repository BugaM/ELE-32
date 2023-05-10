function num = syndrome2num(syndrome)
%syndrome2num Converts a polynomial syndrome to a number one
%   Converts the polynomial syndrome to a number
%   This number is the polynomial evaluated on 2
%   It is equivalent of using the polynomials coefficients
%   as the digits of a base two number.
num = polyval(syndrome, 2);
end
