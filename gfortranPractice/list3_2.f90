module subprog
  implicit none 
contains
  subroutine swap(a,b)
   integer a,b
   integer tmp
   if (a==b) return
   tmp = a
   a = b
   b = tmp
  end subroutine swap
end module subprog 

program list3_2
  use subprog
  implicit none
  integer :: x = 77, y = 77, tmp = 0
  write(*,*) 'x, y, tmp = ',x,y,tmp
  call swap(x,y) 
  write(*,*) 'x, y, tmp = ',x,y,tmp
end program list3_2
