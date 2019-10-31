% visMagnitude.m
% 08/12/19 - ryan pili
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
tic
visDur = readtable("visDur.csv");

av_dx = [];
av_dy = [];
av_dz = [];
ao_dx = [];
ao_dy = [];
ao_dz = [];

for line = 1:height(visDur)
    if line == 1 || visDur.pptno(line) ~= visDur.pptno(line - 1)
        visDur.pptno(line)
        ofdata = readtable(sprintf('/home/ryan/GS/CECLAB/vgcmd/dataanalysis/ofcsv/vg%02d.csv', visDur.pptno(line)), 'Delimiter', ',');
    end
    
    if string(visDur.condition(line)) == 'ao' || string(visDur.condition(line)) == 'AO'
        [ao_dx(line) ao_dy(line) ao_dz(line)] = nodmag(visDur.onset(line), visDur.duration(line), ofdata);
        aobydyad(line, :) = [visDur.dyadno(line), ao_dx(line), ao_dy(line), ao_dz(line)];
        
    elseif string(visDur.condition(line)) == 'av' || string(visDur.condition(line)) == 'AV'
        [av_dx(line) av_dy(line) av_dz(line)] = nodmag(visDur.onset(line), visDur.duration(line), ofdata);
        avbydyad(line, :) = [visDur.dyadno(line), av_dx(line), av_dy(line), av_dz(line)];
    end
end

av_dx(av_dx == 0) = [];
av_dy(av_dy == 0) = [];
av_dz(av_dz == 0) = [];
ao_dx(ao_dx == 0) = [];
ao_dy(ao_dy == 0) = [];
ao_dz(ao_dz == 0) = [];

save("visMagout.mat","avbydyad","aobydyad")

toc
    
