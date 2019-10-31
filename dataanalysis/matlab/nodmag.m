% nodmag.m
% 08/12/19 - ryan pili
%
% script to take in a starting time and duration across which to measure
% changes in pitch, yaw, and roll in the csv output of OpenFace. For ONE
% nod or headshake.
% i.e. measures the distance travelled or angle travelled in each axis.
%
% [dpitch, dyaw, droll] = nodmag(onset, duration)
% input:
%       onset    = the second where a single head movement begins (or slightly
%       before)
%       duration = how many seconds the head movement lasts
% output:
%       dpitch = distance / angle travelled in pitch 
%       dyaw   = distance / angle travelled in yaw
%       droll  = distance / angle travelled in roll 

function [dx, dy, dz] = nodmag(onset, duration, data)

% clearvars -except data

% data = readtable('/home/ryan/GS/CECLAB/vgcmd/dataanalysis/ofcsv/vg08.csv', 'Delimiter', ',');
Rx = data.pose_Rx;
Ry = data.pose_Ry;
Rz = data.pose_Rz;
onset = ttf(onset, 30);
offset = onset + ttf(duration, 30);

dx = [];
dy = [];
dz = [];

for frame = onset:offset
    if frame == onset
        dx_onset = Rx(frame);
        dy_onset = Ry(frame);
        dz_onset = Rz(frame);
    elseif frame > onset
        dx(frame) = Rx(frame) - Rx(frame - 1);
        dy(frame) = Ry(frame) - Rx(frame - 1);
        dz(frame) = Rz(frame) - Rx(frame - 1);
    end
end

dx = abs(dx);
dy = abs(dy);
dz = abs(dz);

dx = sum(dx);
dy = sum(dy);
dz = sum(dz);

end 




