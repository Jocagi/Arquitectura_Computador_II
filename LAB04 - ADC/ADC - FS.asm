;Define CONFIG = 0x3F72

;CONFIGUARACION
	DATO EQU 0X21
	COUNT EQU 0X22

;Inicio del programa en la posición cero de memoria
	ORG 0x00

INICIO
	BCF STATUS, RP0 	;Ir a banco 0
	BCF STATUS, RP1

	;Configurar ADCON0
	MOVLW b'01000001'	;A/D conversion (Clock: Fosc/32)
	MOVWF ADCON0		;Mover configutacion

	BSF STATUS,RP0		;Ir a banco 1
	BCF STATUS,RP1
	CLRF TRISB		;Definir como PORTB salida

	;Configurar ADCON1
	;A/D Port Configuration Control bits
	MOVLW b'01001110'	;A/D Port AN0/RA0
	MOVWF ADCON1	  	;Mover configutacion
	BSF TRISA,0 		;RA0 linea de entrada para el ADC

	BCF STATUS,RP0 		;Ir banco 0
	BCF STATUS,RP1
	;CLRF PORTB 		;Limpiar PORTB
	MOVLW B'00111111' 	;Display 0
	MOVWF PORTB
MAIN
	BTFSS INTCON,T0IF
	GOTO MAIN
   	BCF INTCON, T0IF    	;RESET TMR0 OVERFLOW FLAG
	BSF ADCON0,GO 		;Empezar la conversion A/D
ESPERAR_TERMINAR
	;Validar si la conversión es completa
	BTFSC ADCON0,GO 	;ADCON0 es 0?
	GOTO ESPERAR_TERMINAR 	;No: esperar
	MOVF ADRESH,W 		;Si: W=ADRESH
	MOVWF DATO		;Se almacena el resultado
	CALL CONVERT_DECIMAL	;Convertir el dato ADC a un numero 0-9
	GOTO MAIN 		;Repetir ciclo

CONVERT_DECIMAL
	CLRF 	COUNT		;COUNT=0
SUBTRACTION
	INCF	COUNT, 1	;Sumar 1 al contador
	MOVLW	D'28'
    	SUBWF   DATO, 1		; Calcular: FSvalue - DATO
    	;ZERO Flag
	BTFSC   STATUS,Z
	GOTO	END_SUBTRACTION	; ZERO = 1: Por lo tanto DATO = FSvalue
	NOP			; ZERO = 0: Por lo tanto DATO <> FSvalue
    	;CARRY Flag
	BTFSS   STATUS,C
	GOTO	END_SUBTRACTION	; CARRY = 0: DATO < FSvalue
	GOTO	SUBTRACTION	; CARRY = 1: DATO > FSvalue


END_SUBTRACTION
	CLRF 	DATO 		;DATO=0
	MOVF 	COUNT,W 	;W=COUNT
	CALL 	DISPLAY 	;Decodificar el valor de DISPLAY
	MOVWF 	PORTB 		;Escribe el valor en PORTB
	RETURN			;NO: Regresar al inicio

DISPLAY
	ADDWF PCL,f
	RETLW B'01111001' ;E
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
	RETLW B'01111001' ;E

	GOTO MAIN
END