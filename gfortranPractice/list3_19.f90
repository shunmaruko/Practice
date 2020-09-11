module sample 
  implicit none 
contains
  subroutine print_title(title)
    character(*), intent(in) :: title
    write(*,*) title, len(title)
  end subroutine print_title
end module sample

program main
  use sample
  implicit none 
  character(5) :: c = 'hello'
  call print_title(c)
  call print_title('goodbye')
end program main
