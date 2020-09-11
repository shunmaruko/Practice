program enshu1_16
  implicit none
  real(8) :: t, h, pi = 3.1415926, g = 9.8d0, er, er0 = 1.0d-6,&
             l0=0.0d0, l1=0.0d0
  integer i
  write(*,*) 'input t,h'
  read(*,*) t, h
  l0 = 1.0d0 / t
  do i = 1, 10000
    l1 = t * (g*l0*tanh(2.0d0*pi*h/l0)/(2.0d0*pi))**0.5d0
    er = abs(l1-l0)
    if ( er < er0 ) exit 
    l0 = l1
  enddo 
  write(*,*) 'answer : ', l1
end program enshu1_16
