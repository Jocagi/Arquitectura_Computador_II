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
   unsigned int8 i = 0;
   unsigned int1 input_flag = 0;
   
   //Configurar A0 como entrada
   set_tris_a(0b00000001); 
   //Configurar puerto B y C como salida
   set_tris_b(0x00); 
   set_tris_c(0x00);
   
   //Inicializar pueto B en 0
   port_b = 0x00;
   
   while(TRUE)
   {
      if(input(PIN_A0) && !input_flag)
      {
         input_flag = 1;
         i++;
         
         port_b = i;
             
         if(i >= 5)
         {
            output_high(PIN_C0);
         }
      }
      else if (!input(PIN_A0))
      {
         input_flag = 0;
      }
   }
}
