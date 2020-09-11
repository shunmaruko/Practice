module sub
  implicit none 
contains
  subroutine gauss_jordan_pv(a, x, b, n) 
    integer, intent(in) :: n 
    integer i,k,m
    real(8) a(n,n) ,b(n)
    real(8), intent(out) :: x(n)
    real(8)  btmp(n), tmp(n), max_a ,w
    do i = 1, n
      max_a = abs(a(i,i))
      m = i
      do k = i+1, n !部分ピポット選択
        if (abs(a(k,i))> max_a) then 
          max_a = abs(a(k,i))
          m     = k 
        end if
      enddo 
      if (max_a == 0.0d0) stop 'matrix is special'
      if (m /= i) then  !行の入れ替え
        tmp(i:n) = a(i,i:n)
        a(i,i:n) = a(m,i:n)
        a(m,i:n) = tmp(i:n)
        w        = b(i)
        b(i)     = b(m)
        b(m)     = w 
      endif
      b(i) = b(i) / a(i,i)  !bの更新
      a(i,i+1:n) = a(i,i+1:n) / a(i,i) !aの更新
      a(i,i) = 1.0d0 
      do k = 1, n
        if (k /= i) then 
          a(k,i+1:n) = a(k,i+1:n) - a(i,i+1:n) * a(k,i)
          b(k) = b(k) - b(i) * a(k,i) 
          a(k,i) = 0.0d0 
        endif
      enddo
   enddo
   x(1:n) = b(1:n)
  end subroutine gauss_jordan_pv
end module sub

program list6_2
  use sub
  implicit none
  integer n 
  real(8) ,allocatable ::  a(:,:) ,b(:), x(:)
  write(*,'(a)', advance = 'no') 'input number n >> '
  read(*,*) n
  allocate(a(n,n), b(n), x(n))
  write(*,*) 'input array ',n**2,'youshould input the amount'
  read(*,*) a(1:n,1:n)
  write(*, *) 'input b'
  read(*,*) b(1:n)
  call gauss_jordan_pv(a,x,b,n)
  write(*,*) 'the answer is ', x(1:n)
end program list6_2 
