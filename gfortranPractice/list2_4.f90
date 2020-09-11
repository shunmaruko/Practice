program list2_4
  implicit none
  real(8), allocatable :: u(:), v(:)
  integer :: n
  write(*,'(a)',advance ='no') 'input n :'
  read(*,*) n
  allocate(u(n), v(n))
  write(*,'(a)', advance = "no") 'input u(1:n) : '
  read(*,*) u(1:n)
  write(*,'(a)', advance='no') 'input v(1:n) : '
  read(*,*) v(1:n)
  write(*,*) 'dp=', dot_product(u,v)
  deallocate(u,v)
end program list2_4
