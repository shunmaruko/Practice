program list2_8
  implicit none
  integer :: n, i, fi=10 !ファイルナンバー, 整数宣言
  real(8), allocatable :: array(:,:) !二次元の割付け配列
  write(*,'(a)', advance = 'no') 'input number >>'
  read(*,*) n
  allocate(array(n,n))
  call random_seed
  do i = 1, n 
   call random_number(array(i,i:n))
   array(i+1:n,i) = 0.0d0
  enddo
  do i = 1,n
    write(*, '(100e12.4)') array(i, 1:n) 
  enddo
end program list2_8
