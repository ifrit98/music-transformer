
function f=v_midi2frq(n,s)
if nargin > 1
  if s(1)=='p'
    r=[256/243 9/8 32/27 81/64 4/3 729/512 3/2 128/81 27/16 16/9 243/128];
  elseif s(1)=='j'
    r=[16/15 9/8 6/5 5/4 4/3 36/25 3/2 8/5 5/3 9/5 15/8];
  else
    r=0;
  end
  if r(1)
    c=[0 0 12*log(r)/log(2)-(1:11) 0];
    nm=mod(n,12);
    na=floor(nm);
    nb=nm-na;
    f=440*exp((n+c(na+2).*(1-nb)+c(na+3).*nb-69)*log(2)/12);
  else
    f=440*exp((n-69)*log(2)/12);
  end
else
  f=440*exp((n-69)*log(2)/12);
end
