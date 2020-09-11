program list2_17
  implicit none 
  integer m, n, k
  real(8), allocate :: a(:,:),b(:,:),c(:,:),d(:,:)
  n = 100
  m = 33
  allocate(a(n,n), b(n,n), c(n,n), d(n,n))
  call random_seed
  call random_number(a(:,:))
  call random_number(b(:,:))
  c(:,:) = matmul(a(:,:),b(:,:))
  k = m + 1
  d(1:m, 1:m) = matmul(a(1:m, 1:m),b(1:m, 1:m)) &
                + matmul(:
  
