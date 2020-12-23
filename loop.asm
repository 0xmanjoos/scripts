global _start

section .text
_start:
	mov ebx, 1	; start ebx at 1
	mov ecx, 4	; number of iterations
; START OF THE LOOP
label:
	add ebx, ebx	; ebx += ebx
	dec ecx			; decrement ecx, similar to i++ but i--
	cmp ecx, 0		; compare ecx with 0
	jg label		; JUMP to lavel IF greater than
	mov eax, 1		; sys_exit system call
	int 0x80

; ecx is being decremented each time, so eventually it will reach 0
; this means that the jump wont happen as shown in the: jg label
