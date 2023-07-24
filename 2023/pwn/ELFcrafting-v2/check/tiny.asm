;; tiny.asm: Copyright (C) 2021 Brian Raiter <breadbox@muppetlabs.com>
;; Licensed under the terms of the GNU General Public License, either
;; version 2 or (at your option) any later version.
;;
;; To build:
;;	nasm -f bin -o tiny tiny.asm && chmod +x tiny

BITS 64

		org	0x700000000

		db	0x7F			; e_ident
_start:	db	"ELF"			; 3 REX prefixes (no effect)
		lea rsi, [shellcode]
		dec edx
		syscall
shellcode:
		align 16
		dw	2 			; e_type
		dw	62			; e_machine
		dd	1			; e_version
phdr:	dd	1			; e_entry	; p_type
		dd	7					; p_flags
		dq	phdr - $$		; e_phoff	; p_offset
		dq	phdr			; e_shoff	; p_vaddr
		dd	0			; e_flags	; p_paddr
		dw	0x40			; e_ehsize	
		dw	0x38			; e_phentsize
		dw	1			; e_phnum	; p_filesz
		dw	0x40			; e_shentsize
		dw	0			; e_shnum
		dw	0			; e_shstrndx
		dq	0x00400001				; p_memsz
		times 8 db 0