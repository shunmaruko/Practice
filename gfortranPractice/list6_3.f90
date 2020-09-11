module subprogs
  implicit none 
contains 
  subroutine gauss_seidel(a, b, x, n, nmax, er0)
    integer , intent(in) :: n, nmax
    integer i,j,k
    real(8), intent(in) :: er0, a(n,n), b(n)
    real(8), intent(out) :: x(n)
    real(8) rev(n), s, err(n),ernow
    do i = 1, n
      if (a(i,i) == 0) stop 'a(i,i)=0'
      rev(i) = 1.0d0 / a(i,i) 
    enddo
    x(1:n) = 0.0d0
    s = 0.0d0
    do k = 1, nmax
      do i = 1, n 
        s = dot_product(a(i,1:i-1),x(1:i-1)) 
        s = s + dot_product(a(i,i+1:n),x(i+1:n))
        x(i) = rev(i) * (b(i) -s)
      enddo
      err(1:n) = b(1:n) - matmul(a, x)
      ernow = dot_product(err, err)
      write(*,*) 'k = ', k, 'err**2 =', ernow
      if (ernow <= er0) then
        write(*,*) '# converged #'
        exit
      endif
    enddo
  end subroutine gauss_seidel
end module subprogs

program main
  use subprogs
  implicit none 
  integer, parameter :: n = 3, nmax = 100
  real(8), parameter :: err0 = 1.0d-6
  real(8) a(n,n), b(n), x(n) 
  a(1,1:n) = (/4,1,-2/)
  a(2,1:n) = (/1,6,3/)
  a(3,1:n) = (/2,1,9/)
  b(1:n)   = (/6,-2,-7/)
  call gauss_seidel(a, b, x, n, nmax, err0)
  write(*,*) 'answer is ', x(1:n)
end program main
