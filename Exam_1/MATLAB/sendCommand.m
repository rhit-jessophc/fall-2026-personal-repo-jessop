function response = sendCommand(command)
    import matlab.net.*
    import matlab.net.http.*
                      
    r = RequestMessage;
    uri = URI("http://127.0.0.1:8080/api/" + command);
    resp = send(r, uri);
    response = resp.Body.Data;
    fprintf("Response to %s --> %s", command, response);           
end



