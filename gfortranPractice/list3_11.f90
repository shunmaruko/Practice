module sub_mod 
  implicit none 
contains
  subroutine print1d(a,m)
    integer, intent(in) :: m, a(1:*)
    write(*,*) 'sub : ', a(1:m)
  end subroutine print1d
end module sub_mod

program main
  use sub_mod
  implicit none
  integer, parameter :: n = 2
  integer a(n,n,n), i, j, k
  do k = 1, n
    do j = 1, n
      do i = 1,n
        a(i,j,k) = 100 * i + 10 * j + k
      enddo
    enddo
  enddo
  write(*,*) ' main : ' , a
  call print1d(a, n ** 3)
end program main
