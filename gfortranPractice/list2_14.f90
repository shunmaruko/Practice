program list2_14
  implicit none 
  real(8) , allocatable :: array(:,:), x(:),var(:)
  integer i,j,n,m,is
  write(*,'(a)',advance='no') 'put n, m >>'
  read(*,*) n,m 
  allocate(array(n,m),x(m),var(n),stat=is)
  if (is /= 0) stop 'cannnot allocate (n is too large)'
  call random_seed
  call random_number(array(:,:))
  call random_seed
  call random_number(x(:))
  var(:) = 0.0d0
  do i = 1,n 
    do j = 1,m 
      var(i) = var(i) + array(i,j) * x(j)
    enddo
  enddo
  write(*,*) var(:)
end program list2_14 
     
