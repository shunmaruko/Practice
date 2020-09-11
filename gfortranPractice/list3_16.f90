module subprograms 
  implicit none
contains 
  subroutine print_mat(ia)
    integer, intent(in) :: ia(:,:)
    integer i
    do i = 1, size(ia,1)
      write(*,*) ia(i, 1:size(ia,2)) 
    enddo
  end subroutine print_mat
end module subprograms

program main 
  use subprograms 
  implicit none 
  integer i, j, ia(3,3) 
  do i = 1, 3 
    ia(i, 1:3) = (/(10 * i + j, j = 1, size(ia,2))/)
  enddo
  call print_mat(ia)
  call print_mat(ia(2:3,2:3))
end program main
