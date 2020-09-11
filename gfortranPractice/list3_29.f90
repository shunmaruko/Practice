module globals
  real(8), allocatable, save :: a(:,:)
  integer, save :: n, m
end module globals

module mat_subprogs
  use globals
  implicit none
contains
  subroutine allocate_rmat2
    write(*,'(a)',advance = 'no') 'input n,m:'
    read(*,*) n,m
    allocate(a(n,m))
    call random_number(a)
  end subroutine allocate_rmat2
  
  subroutine print_mat3
    integer i
    do i = 1, n
      write(*,'(100e12.4)') a(i,1:m)
    enddo
  end subroutine print_mat3
end module mat_subprogs

program random_mod2
  use mat_subprogs
  call allocate_rmat2
  call print_mat3
  write(*,*) n, m
end program random_mod2

