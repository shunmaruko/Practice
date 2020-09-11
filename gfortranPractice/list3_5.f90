module subprogs
  implicit none
contains
  function func_cone_vol(r,h) result(v)
    real(8), intent(in) :: r, h
    real(8) v, s, pi
    pi = 2.0d0 * acos(0.0d0)
    s = pi * r ** 2
    v = s * h / 3.0d0
  end function func_cone_vol
end module subprogs

program main 
  use subprogs
  implicit none 
  real(8) :: a = 1.5d0, l = 3.0d0
  write(*,*) 'ensui taiseki = ', func_cone_vol(a,l)
end program main
