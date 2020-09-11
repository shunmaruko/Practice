program enshu1_8
	implicit none
	integer n,i,w 
	w=0
	i=0
	write(*,*) 'input number'
	read(*,*) n
    do i=2, n-1
		if (mod(n,i)==0) w = 1    
    enddo
	if (w==0) then
        write (*,*) n,' is 素数'
    else  
    	write (*,*) n,'is not  素数'
    endif
end program enshu1_8 
