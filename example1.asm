global _start
_start:
	mov eax, 1
	mov ebx, 42
	sub ebx, 29	; THIS SUBTRACTS!!!
	int 0x80
; echo $?
; This shows the exit status code
