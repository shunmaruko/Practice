module matrixmodule 
  implicit none
contains
  function eval2xmat(a) result(eval)
    real(8), intent(in) :: a(:,:)
    complex(8) eval(2)
    real(8) b, c, d, e
    if (size(a,1) /= size(a,2)) stop 'not square'
    if (size(a,1) /= 2) stop 'not 2×2'
    b = -0.5d0 * (a(1,1) + a(2,2))
    c = a(1,1) * a(2,2) -a(1,2) * a(2,1)
    d = b ** 2 - c
    if (d < 0.0d0) then
      eval(1) = cmplx(-b, sqrt(-d), kind = 8)
	  eval(2) = conjg(eval(1))
    else if (d > 0.0d0) then 
      e = -b + sign(sqrt(d), -b)
      eval(1) = cmplx(e, 0.0d0, kind = 8)
      eval(2) = cmplx(c /e , 0.0d0, kind = 8)
    else
      eval(1) = cmplx(-b, 0.0d0, kind = 8)
      eval(2) = eval(1) 
    endif
  end function eval2xmat
end module matrixmodule

program main
  use matrixmodule
  implicit none
  real(8) matrix(2,2), a, b, c, d
  write(*,*) 'input number'
  read(*,*) a, b, c, d
  matrix(1:2,1) = (/a,b/)
  matrix(2,1:2) = (/c,d/)
  write(*,*) 'answer is ',  eval2xmat(matrix) 
end program main
 
