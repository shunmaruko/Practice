program list2_9
  implicit none
  integer array(2,2)
  array(1, 1:2) = (/11, 12/)
  array(2, 1:2) = (/21, 22/)
  write(*,*) array(:,:)
end program list2_9

  
