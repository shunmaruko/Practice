module subprogs
  implicit none 
contains
  subroutine count 
    integer       :: ic1 = 0
    integer, save :: ic2 = 0
    ic1 = ic1 + 1
    ic2 = ic2 + 1
    write(*,*) ic1, ic2
  end subroutine count 
end module subprogs

program main
  use subprogs
  implicit none
  integer i
  do i = 1, 3
    call count
  enddo
end program main
