program list1_5
    implicit none
	integer wa, n,i !変数を宣言
	wa=0!変数を初期化
	write (*,*) 'input number'
    read (*,*) n
    do i = 1,n
		wa = wa + i
	enddo
    write (*,*) 'answer is ',wa
end program list1_5
