
;Inicio del programa en la posición cero de memoria
	org 0x00
	nop
	nop

_inicio
	bcf STATUS, RP0 ;Ir banco 0
	bcf STATUS, RP1
	movlw b'01000001' ;A/D conversion Fosc/8
	movwf ADCON0
	bsf STATUS,RP0 ;Ir banco 1
	bcf STATUS,RP1
	clrf TRISA ;PORTA salida
	clrf TRISB ;PORTB salida
	clrf TRISC ;PORTC salida
	clrf TRISD ;PORTD salida
	clrf TRISE ;PORTE salida
	movlw b'00000111'
	movwf OPTION_REG ;TMR0 preescaler, 1:156
	movlw b'00001110' ;A/D Port AN0/RA0
	movwf ADCON1
	bsf TRISA,0 ;RA0 linea de entrada para el ADC
	bcf STATUS,RP0 ;Ir banco 0
	bcf STATUS,RP1
	clrf PORTC ;Limpiar PORTC
_bucle
	;btfss INTCON,T0IF
	;goto _bucle ;Esperar que el timer0 desborde
	;bcf INTCON,T0IF ;Limpiar el indicador de desborde
	bsf ADCON0,GO ;Empezar la conversion A/D
_espera
	btfsc ADCON0,GO ;ADCON0 es 0? (la conversion esta completa?)
	goto _espera ;No, ir _espera
	movf ADRESH,W ;Si, W=ADRESH
	movwf PORTC ;Muestra el resultado en PORTC
	goto _bucle ;Ir bucle
end