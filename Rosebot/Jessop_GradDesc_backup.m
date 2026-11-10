function [xbest,fbest,itrcnt,stat] = Jessop_GradDesc(f,Df,x0,gradTol,xTol,itrBound,s)

% f  - function
% dF - gradient 
% x0 - initial guess
% gradTol - termination criterion on ∥∇f(xbest)∥
% xTol - termination criterion on  ∥xk − xk−1∥.
% itrBound - max number of itterations before failure 
% s - a search parameter with one of three values
    % s = 1 : use α=1 for all iterations.
    % s = 2 : Decide α with a Lagrange polynomial with α1 =0, α2 =1, and α3 = 2.
    % s = 3 : Decide α with bisection over the interval 0 ≤ α ≤ 1; 
    %         if ∇f(x)and∇f(x+d) have the same sign, then set α =1

% set first x to x0
x = x0;
itrcnt = 0;
stat = 1;



while true %INSERT END CRITERION HERE 
    dK = -1 * feval(Df,x);

    % SOLVE FOR ALPHA ONE OF THREE WAYS HERE

    if s == 1
        % Alpha = 1
        alpha = 1;
    elseif s == 2
        


    elseif s == 3
        alpha = Bisection(0,1,x,dK,0.001,0.001,100,Df);
    else
        break
    end
    

    xNext = x + alpha*dK;
    
    itrcnt = itrcnt + 1;
    if abs(feval(f,xNext)) < gradTol
        stat = 0;
        break
    elseif abs(xNext - x) < xTol
        break
    elseif itrcnt >= itrBound 
        break 
    end
    x = xNext;
end

xbest = xNext;
fbest = feval(f,xNext);

end


function [aBest] = Bisection(a,b,x,d,epsilon,delta,maxitr,Df)

% SETUP LOCAL VARIABLES
nitr = 0;
done = 0;

% START LOOP
while done == 0

% Main Math Loop
    aBest = (a + b) / 2;
    faBest = Bisection_Val_Func(x,aBest,d,Df);
    if sign(faBest) == sign(Bisection_Val_Func(x,a,d,Df))
        a = aBest;
    elseif sign(faBest) == sign(Bisection_Val_Func(x,b,d,Df))
        b = aBest; 
    end
    
% END CONDITIONS
    if abs(faBest) <= epsilon
        done = 1;
    elseif faBest == 0
        done = 1;
    elseif nitr >= maxitr
        done = 1;
    elseif sign(Bisection_Val_Func(x,a,d)) == sign(Bisection_Val_Func(x,b,d))
        done = 1;
    end

% ITTERATE THE LOOP
    nitr = nitr + 1;
end
end


function [y] = Bisection_Val_Func(x,alpha,d,Df)
    xStuff = x + alpha*d;
    y = transpose(feval(Df,xStuff)) * d;
end




