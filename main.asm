global _start:
SYS_CALL_WRITE equ 4
SYS_CALL_READ equ 3
SYS_CALL_EXIT  equ 1

section .text
_start:
    MOV eax, SYS_CALL_WRITE                     ; systemcall
    MOV ebx, 1                                  ; file descriptor
    MOV ecx, _msg_                              ; messages
    MOV edx, __msg_len__                        ; Lenght in Bytes
    int 0x80
    