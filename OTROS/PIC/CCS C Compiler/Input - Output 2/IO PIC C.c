#include <16F877A.h>
//Frecuencia de oscilador = 20Mhz
#use delay(crystal=20000000)
//Optimizacion del compilador
#use fast_io(A)
//Configuracion de memoria
#byte port_a = 0x05
#byte port_b = 0x06
#byte port_c = 0x07
#byte port_d = 0x08
#byte port_e = 0x09

void main()
{
   //Configurar puerto A como entrada
   set_tris_a(0x3F);
   //Configurar puerto B como salida
   set_tris_b(0x00);
   //Configurar RB0..RB3 como salida y RB4..RB7 como entradas
   set_tris_c(0b00001111); 
   
   //Inicializar pueto B con 1's
   port_b = 0x3F;
   
   while(TRUE)
   {
      if(input(PIN_A0))
      {
         output_low(PIN_C6);
         output_high(PIN_C7);
      }
      else
      {
         output_bit(PIN_C7, 0);
         output_bit(PIN_C6, 1);
      }
   }
}
