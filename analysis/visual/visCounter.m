% visCounter.m
% 08/07/19 - ryan pili
%
% program to process a vis BC dyad transcription,
% gives counts of visBC, for each condition, and each participant
% 
% [visbc_AVpptA, visbc_VOpptA, igm_AVpptA, igm_VOpptA; visbc_AVpptB, 
% visbc_VOpptB, igm_AVpptB, igm_VOpptB] = visCounter(dyad, pptA, pptB)
% input:
%       dyad      = file name of transcription in .csv form
%       smileflag = if 0, removes smiles from count. if 1, adds smiles to
%                   count.
% output:
%       visbc_AVpptA = visual backchannel count in audio visual for A
%       visbc_AOpptA = visual backchannel count for audio only for A
%       igm_AVpptA   = in-game mechanic count for audio visual for A
%       igm_AOpptA   = in-game mechanic count for audio only for A
%       visbc_AVpptB = visual backchannel count in audio visual for B
%       visbc_AOpptB = visual backchannel count for audio only for B
%       igm_AVpptB   = in-game mechanic count for audio visual for B
%       igm_AOpptB   = in-game mechanic count for audio only for B
%

function [count_by_ppt, count_by_cond] = visCounter(dyadno, smileflag)

%clearvars -except dyadno smileflag

% dyadno = string(dyadno);

% create dyad table
dyad = readtable(sprintf("/home/ryan/GS/CECLAB/vgcmd_main/analysis/visual/visual_locationCSVs/dyad%02d_vis.csv", dyadno), 'Delimiter', ',');
dyad.Properties.VariableNames = {'Condition', 'Onset', 'Participant', 'Event', 'Offset', 'Role'};

% initialize variables
vAVa = 0;
vAOa = 0;
vAVb = 0;
vAOb = 0;

% initialize condition flag
flag = 3;

% main loop, parses through table made by dyad*_vis.csv
for time = 1:height(dyad)
    if string(dyad.Event(time)) == "smile" && smileflag == 0
        continue
    end
    if contains(dyad.Condition(time), "AV")
        flag = 1;
    elseif contains(dyad.Condition(time), "AO")
        flag = 0;
    end
    if flag == 1
        if dyad.Participant(time) < nanmean(dyad.Participant) && string(dyad.VisType(time)) == 'v'
            vAVa = vAVa + 1;
        elseif dyad.Participant(time) > nanmean(dyad.Participant) && string(dyad.VisType(time)) == 'v'
            vAVb = vAVb + 1;
        end
    elseif flag == 0
        if dyad.Participant(time) < nanmean(dyad.Participant) && string(dyad.VisType(time)) == 'v'
            vAOa = vAOa + 1;
        elseif dyad.Participant(time) > nanmean(dyad.Participant) && string(dyad.VisType(time)) == 'v'
            vAOb = vAOb + 1;
        end
    end
end

count_by_ppt = [vAVa vAOa; vAVb vAOb];
vAV = vAVa + vAVb;
vAO = vAOa + vAOb;
count_by_cond = [vAV vAO];