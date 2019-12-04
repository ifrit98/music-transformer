function[mel,mr] = v_frq2mel(frq)
persistent k
if isempty(k)
    k=1000/log(1+1000/700); % 1127.01048
end
af=abs(frq);
mel = sign(frq).*log(1+af/700)*k;
mr=(700+af)/k;
if ~nargout
    plot(frq,mel,'-x');
    xlabel(['Frequency (' v_xticksi 'Hz)'])
    ylabel(['Frequency (' v_yticksi 'Mel)'])
end


% Implement Self-Similarity from paper: http://music.cs.northwestern.edu/publications/Rafii-Pardo%20-%20Music-Voice%20Separation%20using%20the%20Similarity%20Matrix%20-%20ISMIR%202012.pdf
% 