program list1_8
  implicit none
  real(8) :: xn, xm, a, er ,er0 = 1.0d-6 
  integer :: i , im=100
  write(*,'(a)', advance = 'no') 'input a:'
  read(*,*) a
  if (a <= 0.0d0) stop 'a <=0'
  xn = a
  do i = 1, im
    xm = xn - 0.5 *  (xn**2 - a) / xn 
    er = abs(xm-xn)
    if ( er < er0) exit
    xn = xm
  enddo
  write(*,*) 'kai, i, er = ', xm, i, er
end program list1_8 
