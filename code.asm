global _start
section .text
_start:

; Write a value to screen
	 mov eax, 4
	 mov ebx, 1
	 mov ecx, "food"
	 mov edx, 4
	 int 80h


	; Exit 
	 mov eax, 1
	 mov ebx, 0
	 int 80h
