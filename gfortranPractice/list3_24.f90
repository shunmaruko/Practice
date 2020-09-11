module vec_subprogs
  implicit none
contains
  function normal_vec(v) result(nv)
    real(8), intent(in) :: v(:)
    real(8) nv(size(v,1)), v1
    v1 = sqrt(dot_product(v,v))
    if (v1 == 0.0d0) then
      nv(:) = 0.0d0
    else 
      nv(:) = v(:) / v1
    endif
  end function normal_vec
end module vec_subprogs

program main 
  use vec_subprogs
  implicit none 
  integer i
  real(8) :: x(5) = (/(i,i = 1, 5)/)
  write(*,'(100e12.4)') normal_vec(x)
end program main
