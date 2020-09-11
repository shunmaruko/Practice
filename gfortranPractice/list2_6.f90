program list2_6
  implicit none
  integer i, j
  real(8) a(2,3)
  a(1,1:2) = (/ 1.2d0, 3.4d0/)
  a(2,1:2) = (/ 5.0d0, 7.8d0/)
  do i = 1,2
    write(*,*) (a(i,j), j = 1,2)
  enddo
end program  list2_6
