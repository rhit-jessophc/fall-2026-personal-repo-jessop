clc
clear all
close all


s = serialport('COM8',19200,'Timeout',15);
writeline(s,'INITIALIZE');
readline(s);