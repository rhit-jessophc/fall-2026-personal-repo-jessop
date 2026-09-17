classdef MyShape < handle
    % ^ subclass of handle
    %UNTITLED2 Summary of this class goes here
    %   Detailed explanation goes here

    properties
        Patch matlab.graphics.primitive.Patch
    end

    methods
        function obj = MyShape(xCoords, yCoords, color)
            obj.Patch = patch(xCoords, yCoords, color)
        end

        function outputArg = move(obj, dx, dy)
            % need to mutate the patch
            obj.Patch.XData = obj.Patch.XData + dx;
            obj.Patch.YData = obj.Patch.YData + dy;


        end

    end
end