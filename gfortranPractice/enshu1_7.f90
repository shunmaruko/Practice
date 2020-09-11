program enshu1_7
  implicit none
  integer n, r, sum1,sum2, i
  do 
    write(*,*) 'input number n ,r'
    read(*,*) n,r
    if (n<0 .or. r <0) then 
      write(*,*) 'sorry, input positive number'
      cycle
    endif
    sum1 = 1 
    do i=0,r-1 
      sum1 = sum1 * (n-i)
    enddo
    sum2 = 1
    do i=1,r
      sum2 = sum2 * i
    enddo
    write(*,*) 'nPr=',sum1, 'nCr=',sum1/sum2
  enddo
end program enshu1_7
