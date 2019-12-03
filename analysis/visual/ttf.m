% ttf.m
% 08/12/19 - ryan pili
%
% time to frame 
% given an amount of time, gives the number of frames
% 
% frames = ttf(dur)
% input:
%       dur = duration in seconds
%       fps = frames per second
% output: 
%       frames = number of frames span

function frames = ttf(dur, fps)

dur = round(dur);

frames = dur*fps;

end


