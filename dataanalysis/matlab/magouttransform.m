% magouttransform.m
% 08/14/19 - ryan pili
%
% script that loads in visMagout.mat
% then removes zeros from aobydyad and avbydyad
% then gets the average of x y z angle splanned for each dyad

load("visMagout.mat")

ao.dyad = aobydyad(:,1);
ao.x = aobydyad(:,2) ;
ao.y = aobydyad(:,3);
ao.z = aobydyad(:,4);

ao.dyad(ao.dyad == 0) = [];
ao.x(ao.x == 0) = [];
ao.y(ao.y == 0) = [];
ao.z(ao.z == 0) = [];


av.dyad = avbydyad(:,1);
av.x = avbydyad(:,2);
av.y = avbydyad(:,3);
av.z = avbydyad(:,4);

av.dyad(av.dyad == 0) = [];
av.x(av.x == 0) = [];
av.y(av.y == 0) = [];
av.z(av.z == 0) = [];

iav1 = av.dyad == 1;
iav4 = av.dyad == 4;
iav5 = av.dyad == 5;
iav6 = av.dyad == 6;
iav8 = av.dyad == 8;


iao1 = ao.dyad == 1;
iao4 = ao.dyad == 4;
iao5 = ao.dyad == 5;
iao6 = ao.dyad == 6;
iao8 = ao.dyad == 8;

dyad_av(1,:) = [mean(av.x(iav1)) mean(av.y(iav1)) mean(av.z(iav1))];
dyad_ao(1,:) = [mean(ao.x(iao1)) mean(ao.y(iao1)) mean(ao.z(iao1))];
dyad_av(2,:) = [mean(av.x(iav4)) mean(av.y(iav4)) mean(av.z(iav4))];
dyad_ao(2,:) = [mean(ao.x(iao4)) mean(ao.y(iao4)) mean(ao.z(iao4))];
dyad_av(3,:) = [mean(av.x(iav5)) mean(av.y(iav5)) mean(av.z(iav5))];
dyad_ao(3,:) = [mean(ao.x(iao5)) mean(ao.y(iao5)) mean(ao.z(iao5))];
dyad_av(4,:) = [mean(av.x(iav6)) mean(av.y(iav6)) mean(av.z(iav6))];
dyad_ao(4,:) = [mean(ao.x(iao6)) mean(ao.y(iao6)) mean(ao.z(iao6))];
dyad_av(5,:) = [mean(av.x(iav8)) mean(av.y(iav8)) mean(av.z(iav8))];
dyad_ao(5,:) = [mean(ao.x(iao8)) mean(ao.y(iao8)) mean(ao.z(iao8))];