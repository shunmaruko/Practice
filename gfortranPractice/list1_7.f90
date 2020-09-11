program list1_7
  implicit none
  real(8) dx, s,  x, y
  integer n, i
  write(*,'(a\)') 'input n :'
  read(*,*) n
  if (n<1) stop 'input positive number'
  dx = 1.0d0 / dble(n)
  s = 0.0d0
  do i = 0, n
    x = dx * dble(i) 
    y = x*(1.0d0-x)
    if (i==0 .or. i==n) then
      s = s + y * 0.5d0
    else
      s = s + y
    endif
  enddo
  s = 6.0d0 * s * dx
  write(*,*) 's = ', s
end program list1_7 

