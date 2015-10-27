function r_x=jacobi(A,b,x0,kmax,tor)
    [m,n]=size(A);    
    x=[];
    x(1,:)=x0;
    for k =1:kmax
        for i=1:n
            x(k+1,i)=(1/A(i,i))*(b(i)-(A(i,:)*(x(k,:))')+A(i,i)*x(k,i));
        end
        if norm((A\b-x(k+1,:)'),2)/norm(b,2)<=tor
            break
        end   
    end
    r_x=x(k+1,:);
    if k==kmax
        fprintf('The desired accuracy of the solution was not achieved.\n');
    end
    fprintf('Times:')
    fprintf(num2str(k))
    fprintf('\n\n\n')
    