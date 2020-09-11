module mat_subprogs 
  implicit none 
contains 
  subroutine print_mat(a,n)
    integer, intent(in) :: n
    real(8), intent(in) :: a(n,n)
    integer i
    do i = 1, n
      write(*,'(100e12.4)') a(i, 1:n)
    enddo
  end subroutine print_mat
end module mat_subprogs
 
program random_mat
  use mat_subprogs
  implicit none 
  real(8), allocatable :: a(:,:)
  integer n, i
  write(*,'(a)',advance = 'no') 'input n : '
  read(*,*) n
  if (n < 1 .or. n > 100) stop 'n must be 0 < n < 101'
  allocate(a(n,n))
  !call random_seed 
  call random_number(a)
  call print_mat(a,n)
end program random_mat
