module mat_subprogs
  implicit none 
contains
  subroutine print_mat2(a)
    real(8), intent(in) :: a(:,:) 
    integer i, n, m
    n = size(a,1)
    m = size(a,2)
    do i = 1, n
      write(*,'(100e12.4)') a(i,1:n)
    enddo
  end subroutine print_mat2
end module mat_subprogs

program main
  use mat_subprogs
  implicit none  
  real(8), allocatable :: matrix(:,:) !二次元の割付き配列を宣言
  integer i ,n
  write(*,'(a)',advance = 'no') 'input n >> '
  read(*,*) n
  if (n < 0 .or. 100 < n) stop 'input number is invalid'
  allocate(matrix(1:n,1:n))
  call random_number(matrix(:,:))
  call print_mat2(matrix)
end program main
