module matrix_subprogs
  implicit none
contains
  subroutine allocate_matrix(array)
    real(8), allocatable, intent(out) :: array(:,:)
    integer n 
    write(*,'(a)',advance = 'no') 'input n :'
    read(*,*) n  
    if (n<1 .or. 100<n) stop 'input number is invalid'
    allocate(array(n,n))
    call random_number(array)
  end subroutine allocate_matrix
  
  subroutine print_matrix2(array)
    real(8), intent(in) :: array(:,:)
    integer i, n
    n = size(array,1)
    do i = 1, n
      write(*,'(100e12.4)') array(i,1:n)
    enddo 
  end subroutine print_matrix2
end module matrix_subprogs

program main
  use matrix_subprogs
  implicit none 
  real(8), allocatable :: a(:,:)
  call allocate_matrix(a)
  call print_matrix2(a)
end program main

