module subprograms
  implicit none 
contains 
  subroutine print_vector(vector,n)
    integer, intent(in) :: n,vector(n) 
    write(*,*) vector(1:n)
  end subroutine print_vector 
end module subprograms

program main 
  use subprograms 
  implicit none 
  integer i,j,m,n
  integer, allocatable :: array(:,:)
  write(*,'(a)',advance = 'no') 'input n,m >>'
  read(*,*) n, m 
  allocate(array(n,m))
  do j = 1, m 
    do i = 1, n
      array(i,j) = 10 * i + j
    enddo
  enddo
  call print_vector(array(1:1,1:3), 3) 
  call  print_vector(array(1  ,1:3), 3) 
  call  print_vector(array(1:3,  1), 3) 
  call  print_vector(array(1  ,1  ), 3) 
end program main
