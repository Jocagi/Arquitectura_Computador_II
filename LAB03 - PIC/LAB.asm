;CONFIGURACION

DATO EQU 0X21
INTERRUPT EQU 0X22
SEGMENT7 EQU 0X23
L1 EQU 0X24
L2 EQU 0X25
;INICIO DE PROGRAMA
	ORG 0X00		;POSICION INICIAL DE MEMORIA
	GOTO START

;CODIGO
START
	BSF	STATUS, 5	;Cambiar al banco 1
	BSF	TRISC, 1	;Definir pata 1 del Puerto C como entrada
	BSF	TRISC, 2	;Definir pata 2 del Puerto C como entrada
	CLRF	TRISB		;Definir Puerto B como salida
	CLRF	TRISD		;Definir Puerto D como salida
	BCF	STATUS, RP0	;Cambiar al banco 0
	MOVLW	0X00
	MOVWF	PORTB		;Inicializar en 0
	MOVLW	0X00
	MOVWF	INTERRUPT	;Inicializar en 0
	GOTO	MENU

MENU
	;SECUENCIA LEDS
	BTFSC	PORTC, 1	;Comprobar si el bit 1 del puerto C se encuentra encendido
	CALL 	DERECHA
	BTFSS	PORTC, 1	;Comprobar si el bit 1 del puerto C se encuentra apagado
	CALL 	IZQUIERDA
	CALL	MENU2
	GOTO	MENU
MENU2
	;CONTADOR INTERRUPCIONES
	BTFSC	PORTC, 2	;Comprobar si el bit 2 del puerto C se encuentra encendido
	CALL	INTERRUPTOR
	RETURN

DELAY1SEG
     	MOVLW 5
     	MOVWF L1
	MOVLW 5
     	MOVWF L2
LOOP1
	;CONTADOR INTERRUPCIONES
	BTFSC	PORTC, 2	;Comprobar si el bit 2 del puerto C se encuentra encendido
	CALL	INTERRUPTOR


	DECFSZ L1,1

	GOTO LOOP1
	DECFSZ L2,1
	GOTO LOOP1
	RETURN



IZQUIERDA
	MOVLW	B'11111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111110'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111101'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111011'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11110111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11101111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11011111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'10111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'01111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	RETURN

DERECHA
	MOVLW	B'11111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'01111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'10111111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11011111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11101111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11110111'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111011'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111101'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	MOVLW	B'11111110'
	MOVWF	DATO
	CALL	MV
	CALL	DELAY1SEG
	RETURN

MV
	MOVF	DATO, W		;Mover 'Dato' al registro W
	MOVWF	PORTB		;Mover W al Puerto B (Salida)
	RETURN

DISPLAY
	MOVF	SEGMENT7, W	;Mover 'Contador' al registro W
	MOVWF	PORTD		;Mover W al Puerto D (Salida)
INSTDELAY
	BTFSC	PORTC, 2	;Comprobar si el bit 2 del puerto C sigue encendido
	GOTO	INSTDELAY
	RETURN

INTERRUPTOR
	INCF	INTERRUPT, 1	;Sumar 1 al contador
	CALL	SETDISPLAY
	CALL 	DISPLAY
	RETURN

SETDISPLAY
	BTFSC	INTERRUPT, 3
	CALL	SETDISPLAY89
	BTFSS	INTERRUPT, 3
	CALL	SETDISPLAY01234567
	RETURN

SETDISPLAY01234567
	BTFSC	INTERRUPT, 2
	CALL	SETDISPLAY4567
	BTFSS	INTERRUPT, 2
	CALL	SETDISPLAY0123
	RETURN

SETDISPLAY0123
	BTFSC	INTERRUPT, 1
	CALL	SETDISPLAY23
	BTFSS	INTERRUPT, 1
	CALL	SETDISPLAY01
	RETURN

SETDISPLAY89
	BTFSs	INTERRUPT, 0
	CALL	SETDISPLAY8
	BTFSc	INTERRUPT, 0
	CALL	SETDISPLAY9
	RETURN

SETDISPLAY4567
	BTFSs	INTERRUPT, 1
	CALL	SETDISPLAY45
	BTFSc	INTERRUPT, 1
	CALL	SETDISPLAY67
	RETURN

SETDISPLAY45
	BTFSS	INTERRUPT, 0
	CALL	SETDISPLAY4
	BTFSC	INTERRUPT, 0
	CALL	SETDISPLAY5
	RETURN

SETDISPLAY67
	BTFSS	INTERRUPT, 0
	CALL	SETDISPLAY6
	BTFSC	INTERRUPT, 0
	CALL	SETDISPLAY7
	RETURN

SETDISPLAY23
	BTFSS	INTERRUPT, 0
	CALL	SETDISPLAY2
	BTFSC	INTERRUPT, 0
	CALL	SETDISPLAY3
	RETURN

SETDISPLAY01
	BTFSS	INTERRUPT, 0
	CALL	SETDISPLAY0
	BTFSC	INTERRUPT, 0
	CALL	SETDISPLAY1
	RETURN

SETDISPLAY9
	MOVLW	0xF6
	MOVWF	SEGMENT7
	;Resetear contador
	MOVLW	0X00
	MOVWF	INTERRUPT
	RETURN
SETDISPLAY8
	MOVLW	0xFE
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY7
	MOVLW	0xE0
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY6
	MOVLW	0xBE
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY5
	MOVLW	0xB6
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY4
	MOVLW	0x66
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY3
	MOVLW	0xF2
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY2
	MOVLW	0xDA
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY1
	MOVLW	0x60
	MOVWF	SEGMENT7
	RETURN
SETDISPLAY0
	MOVLW	0xFC
	MOVWF	SEGMENT7
	RETURN

END