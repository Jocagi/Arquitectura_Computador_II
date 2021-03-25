;CONFIGURACION

DATO EQU 0X21
COUNT EQU 0X22
TEMP EQU 0X23
LIMITE EQU 0X0A

;INICIO DE PROGRAMA
	ORG 0X00		;POSICION INICIAL DE MEMORIA
	GOTO START

;CODIGO
START
	BSF	STATUS, 5	;Cambiar al banco 1
	BSF	TRISC, 1	;Definir pata 1 del Puerto C como entrada
	CLRF	TRISB		;Definir Puerto B como salida
	BCF	STATUS, RP0	;Cambiar al banco 0
	MOVLW	0X00
	MOVWF	PORTB		;Inicializar en 0
	MOVLW	0X00
	MOVWF	COUNT		;Inicializar en 0
	MOVLW	0X00
	MOVWF	TEMP		;Inicializar en 0
	MOVLW	B'00111111'
	MOVWF	PORTB		;Inicializar Display en 0
	GOTO	MAIN

MAIN
	;CONTADOR INTERRUPCIONES
	BTFSC	PORTC, 1	;Comprobar si el bit 1 del puerto C se encuentra encendido
	GOTO	INTERRUPTOR	;SI: Contar la interrupcion
	GOTO 	MAIN		;NO: Regresar al inicio

INTERRUPTOR
	INCF	COUNT, 1	;Sumar 1 al contador
	MOVF 	COUNT,W 	;W=COUNT
	MOVWF 	TEMP 		;TEMP=W
	MOVLW 	LIMITE 		;W=10
	XORWF 	TEMP,W 		;W XOR TEMP
	BTFSS 	STATUS,Z 	;EL resultado de la anterior instruccion es 0?
	GOTO 	SIGUE 		;Z=0, NO es diferente de 0, COUNT = 0,1,2,3,4,5,6,7,8,9
	CLRF 	COUNT 		;Z=1, SI vale 10, TMRO > 9, COUNT = 0
	CLRF 	TEMP 		;Temp=0
SIGUE
	MOVF TEMP,W 		;W=TEMP
	CALL DISPLAY 		;Decodificar el valor de DISPLAY
	MOVWF PORTB 		;Escribe el valor en PORTB
ESPERAR
	BTFSC	PORTC, 1	;Comprobar si el bit 1 del puerto C sigue encendido
	GOTO	ESPERAR		;SI: Esperar
	GOTO 	MAIN		;NO: Regresar al inicio

DISPLAY
	ADDWF PCL,f
	RETLW B'00111111' ;0
	RETLW B'00000110' ;1
	RETLW B'01011011' ;2
	RETLW B'01001111' ;3
	RETLW B'01100110' ;4
	RETLW B'01101101' ;5
	RETLW B'01111101' ;6
	RETLW B'00000111' ;7
	RETLW B'01111111' ;8
	RETLW B'01101111' ;9
END