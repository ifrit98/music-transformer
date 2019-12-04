% Load audio
[x, sr] = audioread('./wav/tmp6xn3jfbd_decode.wav');

% Convert Stereo to mono
% x = (x(:,1)+x(:,2))/2;

% Size of matrix X
Na = length(x);

% No of sections
nsc = floor(Na/500);

% 50 Overlapping matlab Hamming window
nov = floor(nsc/2);

% p = ceil(log_2 nsc)
nff = max(256,2^nextpow2(nsc));

% Compute STFT with hamming window
[X, f, s] = spectrogram(x,hamming(nsc),nov,44100); 

% Take Magnitude
X_mag = abs(X);

% Normalize columns using Euclidian norm
V = normalize((X_mag), 'norm');

% Vector of cosine similarities of V
Cs = pdist(transpose(V), 'cosine');

% Cosine similarity matrix
CsM = squareform(Cs);

% Compute average similarity metric
M = mean(CsM, 'all');

% Simple Similarity Matrix computation (Unused)
% S = mtimes(V, transpose(V));
% S_log = log(S);

% Uncomment one to change colormap
%colormap(parula(5))
%colormap(winter)
%colormap(summer)
%colormap(autumn)

figure(1)
imagesc(sr, f, CsM)
%colorbar
% figure(2)
% imagesc(sr, f, S_log)