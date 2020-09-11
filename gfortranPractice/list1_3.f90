program list1_3
 implicit none
!変数を宣言
 integer wa, n, i
!変数を初期化
 wa=0
!nを標準入力
 write(*,*) 'input n >> '
 read(*,*) n
 if (n<=0) stop 'not correct'
 do i = 1, n
    wa = wa + i
 enddo
 write(*,*) 'wa = ', wa
end program list1_3
