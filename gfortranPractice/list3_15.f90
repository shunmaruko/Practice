module subprogs
  implicit none 
contains 
  subroutine print_ivec(iv, m)
    integer, intent(in) :: m, iv(m)
    write(*,*) iv(1:m)
  end subroutine print_ivec
end module subprogs

program main
  use subprogs
  implicit none 
  integer :: i, ix(10) = (/(i,i = 1,10)/)
  call print_ivec(ix(4:6),3)
end program main 
