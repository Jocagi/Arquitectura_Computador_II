
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
	CLRF TRISC		;Definir como PORTC salida

	;Configurar ADCON1
	;A/D Port Configuration Control bits
	MOVLW b'01001110'	;A/D Port AN0/RA0
	MOVWF ADCON1	  	;Mover configutacion
	BSF TRISA,0 		;RA0 linea de entrada para el ADC

	BCF STATUS,RP0 		;Ir banco 0
	BCF STATUS,RP1
	CLRF PORTC 		;Limpiar PORTC

MAIN
	;btfss INTCON,T0IF
	;goto MAIN
	BSF ADCON0,GO 		;Empezar la conversion A/D
ESPERAR_TERMINAR
	;Validar si la conversión es completa
	BTFSC ADCON0,GO 	;ADCON0 es 0?
	GOTO ESPERAR_TERMINAR 	;No: esperar
	MOVF ADRESH,W 		;Si: W=ADRESH
	MOVWF PORTC 		;Resultado en PORTC
	GOTO MAIN 		;Repetir ciclo