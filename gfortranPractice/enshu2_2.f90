program enshu2_2
  implicit none
  integer :: a(1:4) = (/1,2,3,4/),i
  do i=2,4
    a(i) = a(i-1)
  enddo
  write(*,'(i3)') (a(i), i=1,4)
  a(1:4) = (/1,2,3,4/)
  a(2:4) = a(1:3)
  write(*,'(4i3)') (a(i), i = 1, 4)
end program enshu2_2
