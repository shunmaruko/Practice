program list2_12
  implicit none
  integer, parameter :: n = 100
  real(8) wa, m1, m2, b(n,n)
  integer i, j, i1(2), i2(2)
  call random_seed
  call random_number(b(:,:))
  wa = 0.0d0
  m1 = b(1,1)
  m2 = m1
  i1(1:2) = (/1,1/)
  i2(1:2) = i1(1:2)
  do j = 1,n
    do i = 1, n
      wa = wa + b(i,j) 
      if (b(i,j) < m1) then
         m1 = b(i, j)
         i1(1:2) = (/i,j/)
      endif
      if (b(i,j) > m2) then 
         m2 = b(i,j)
         i2(1:2) = (/i,j/) 
      endif
    enddo 
  enddo
  write(*,*) m1, m2, wa, i1(1:2), i2(1:2)
  write(*,*) minval(b), maxval(b) , sum(b) &
            ,minloc(b), maxloc(b)
end program list2_12
