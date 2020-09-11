program list2_5
  implicit none
  real(8), allocatable :: r(:)
  integer n
  write(*,'(a)',advance = 'no') 'input n (>=1): '
  read (*,*) n
  if (n < 1) stop 'stop n<1'
  allocate(r(n))
  call random_seed
  call random_number(r(1:n))
  r(1:n) = 2.0d0 * r(1:n) -1.0d0
  write(*,'(2f10.6)') r(1:n)
end program list2_5
