; just a really dumb idea
; intel syntax
; 32 bit
; 0x4 is write
; 0x3 is read

global _start

section .text:
_start:
    mov eax, 0x4            ; write syscall
    mov ebx, 1              ; i have no fucking idea what to put here so idk ill just put 1 for now
    mov ecx, message        ; uses the message variable as the buffer
    mov edx, message_length ; supplies the message
    int 0x80                ; exit syscall is 0x1

    mov eax, 0x1            ; exits
    mov ebx, 0

section .data:
    message: db "Hello World", 0xA
    message_length equ $-message
    ; completely fucking useless
