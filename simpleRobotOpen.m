clc
clear all;

plateLoaderMenuControl()
s = serialport(['COM8'], 19200, "Timeout", 15);
pause(1.5);



% fprintf('Connecting to robot...');
% s = serialport(['COM8'], 19200, "Timeout", 15);
% pause(1.5);   % short pause to allow your computer to connect to Serial port

% plateLoaderMenuControl(s);


% 
% %%
% writeline(s, 'INITIALIZE');
% readline(s)
% fprintf('Ready\n');


% %%
% mainMenu = menu('Choose Command', 'Reset', 'X-Axis', 'Z-Axis', 'Gripper', 'Move', 'Status', ' Special Moves', 'Exit')
% 
% switch MainMenu
%     case 1
%         disp('You selected Circle.');
%     case 2
%         disp('You selected Square.');
%     case 3
%         disp('You selected Triangle.');
%     otherwise
%         disp('No selection made.');
% end
% 
% 
