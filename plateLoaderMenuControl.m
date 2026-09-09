function plateLoaderMenuControl(s)

while(1)
    switch(menu('Choose command','Reset','X-Axis',...
            'Z-Axis','Gripper','Move','Status','Special Moves','Exit'))
        case 1
            writeline(s,'RESET');
        case 2
            writeline(s,['X-AXIS ',num2str(menu('Choose location to move to','1','2','3','4','5'))]);           
        case 3
            switch(menu('Z-AXIS:','EXTEND','RETRACT'))
                case 1
                    writeline(s,'Z-AXIS EXTEND');
                case 2
                    writeline(s,'Z-AXIS RETRACT');
            end
        case 8
            fprintf("Goodbye!\n");
            break
    end
    
    readline(s)
end
