program list2_13
  implicit none 
  integer, parameter :: n = 10 
  real(8) a(n), am
  integer i, m
  call random_seed
  call random_number(a(:))
  do i = 1, n-1 
    am = minval(a(i+1:n))
    m = minloc(a(i+1:n),1) + i
    if (a(i) > am ) then 
      a(m) = a(i)
      a(i) = am 
    endif
  enddo
  write(*,'(10e12.4)') a(:) 
end program list2_13
