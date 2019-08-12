% visMagnitude.m
% 07/12/19 - ryan pili
%
% script to process the relevant nods/headshakes from each dyad
% first:
%       needs to access a text file with all the relevant onsets and
%       durations for each nod or headshake
% second:
%       needs to call ttf and nodmag, and access the relevant .csv output
%       from OpenFace
% third:
%       keep a running list of the magnitude of each nod and headshake
% fourth:
%       take an average, and compare across conditions
%       
% 
% [dx, dy, dz] = visMagnitude(csv)
% input:
%       csv = file name for the visDurs.csv (probably just visDurs, does
%       this even need to be a function?)
% output: 
%       av_dx = average magnitude of x movements in AV
%       av_dy = average magnitude of y movements in AV
%       av_dz = average magnitude of z movements in AV
%       ao_dx = average magnitude of x movements in AO
%       ao_dy = average magnitude of y movements in AO
%       ao_dz = average magnitude of z movements in AO


