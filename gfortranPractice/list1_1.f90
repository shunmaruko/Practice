program loop
        implicit none
	integer i, wa
	wa = 0
	do i = 1, 100
    wa = wa  + 1 
   end

   write(*,*) 'wa = ', wa
end program loop 
