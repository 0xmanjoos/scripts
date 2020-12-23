global _start

section .text
_start:
	mov ecx, 99	 ; set ecx to 99

	mov ebx, 42  ; ebx and exit statis is 42

	mov eax, 1	 ; sys_exit system call - exits the program

	cmp ecx, 100 ; compares to see if ecx is equal to 100

	jl skip		 ; jump to IF less than

	mov ebx, 13	 ; changes ebx - exit status into 13


; this is a label
skip:
	int 0x80
