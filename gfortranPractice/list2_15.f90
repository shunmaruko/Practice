program list2_15
  real(8) ,allocatable :: a(:,:),b(:,:),c(:,:)
  integer i,j,k,l,m,n
  write(*,'(a)', advance = 'no') 'input l >> ' 
  read(*,*) l 
  write(*,'(a)', advance = 'no') 'input m >> ' 
  read(*,*) m 
  write(*,'(a)', advance = 'no') 'input n >> ' 
  read(*,*) n 
  allocate(a(l,n))
  allocate(b(n,m))
  allocate(c(l,m))
  call random_seed
  call random_number(a(1:l,1:n))
  call random_seed
  call random_number(b(1:n,1:m))  
  c(l,m) = 0.0d0
  do j = 1,m
    do i = 1,l  
      do k = 1,n 
        c(i,j)  = c(i,j) + a(i,k) * b(k,j)
      enddo
    enddo
  enddo
  open(10, file = 'output.d')
  do i = 1, n
    write(10,'(100f10.6)') c(i,1:m)
  enddo
  close(10) 
  deallocate(a)
  deallocate(b)
  deallocate(c) 
end program list2_15 
