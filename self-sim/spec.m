%     Divide the signal into sections of length .
% 
%     Window the sections using a Hamming window.
% 
%     Specify 50% overlap between contiguous sections.
% 
%     To compute the FFT, use points, where .

[X, sr] = audioread('track.wav');

% Mel Frequency Sepstrum Coefficients
mels = mfcc(X, sr);

% Compute cosine similarity of matrix (Vector output)
%cos_sim = pdist(X, 'cosine');

Dm = dot(mels, mels);
Dx = dot(X, X);

% Pairwise distance between all observations (Symmetric matrix output)
%Zm = squareform(Dm);
Zx = squareform(Dx);

% Size of matrix X
Na = length(X);

% No of sections
nsc = floor(Na/4.5);

% 50% Overlapping Hamming window
nov = floor(nsc/2);

% p = ceil(log_2 nsc)
nff = max(256,2^nextpow2(nsc));

%V = spectrogram(X,hamming(nsc),nov,nff);
V = spectrogram(X,hamming(nsc),nov,sr);

% Magnitude of V
Vm = abs(V);

% Normalize matrix A by Euclidian norm
Vn = normalize(Vm, 'norm');

S = mtimes(transpose(Vn), Vn);