global _start

section .text
_start:
	mov ebx, 42 ; ebx and exit statis is 42
	mov eax, 1	; sys_exit system call - exits the program
	jmp skip	; jump to "skip" label
	mov ebx, 13	; changes ebx into 13
				; if this was done correctly, then the exit status should be 42, else 13

; this is a label
skip:
	int 0x80
