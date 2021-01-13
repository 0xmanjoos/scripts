; nasm -f elf64 input.nasm -o input.o
; ld input.o -o input

section .data
	text db "Hello, What is your name?: "
	text2 db "Hello, "

section .bss
	name resb 16

section .text
	global _start

mov rax, 1
_start:
	call _print
	call _get
	call _print2
	call _name

	mov rax, 1
	mov rdi, 1
	mov rsi, text
	mov rdx, 14
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

_get:
    mov rax, 0
    mov rdi, 0 ; we need to get stdin
    mov rsi, name
    mov rdx, 16
    syscall
    ret

_print:
	mov rax, 1
	mov rdi, 1
	mov rsi, text
	mov rdx, 27
	syscall
	ret

_print2:
	mov rax, 1
	mov rdi, 1
	mov rsi, text2
	mov rdx, 7
	syscall
	ret

_name:
	mov rax, 1
	mov rdi, 1
	mov rsi, name
	mov rdx, 16
	syscall
	ret

