#include <16F877A.h>
#use delay(crystal=20000000)
#byte port_b = 0x06
#use fast_io(A) //Optimizacion del compilador
 
void main()
{
   set_tris_a(0x1F); //Configurar puerto A como entrada
   set_tris_b(0x00); //Configurar puerto B como salida
   port_b = 0; //Inicializar pueto B en 0
   
   while(TRUE)
   {
      if(input(PIN_A0))
      {
         port_b = 0b00111111;
      }
      else
      {
         port_b = 0b00000110;
      }
   }
}
