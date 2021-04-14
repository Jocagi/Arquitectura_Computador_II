//PIC 16F877A
#include <16F877A.h>
//Cantidad de bits para el ADC 8 o 10
#device ADC=10
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
   unsigned int16 i = 0;
   
   //Configurar ADC
   setup_adc(ADC_CLOCK_DIV_32);      // Set ADC conversion time to 32Tosc
   setup_adc_ports(AN0);             // Configure AN0 as analog
   set_adc_channel(0);               // Select channel 0 input

   //Configurar puerto B como salida
   set_tris_b(0x00);
   
   //Inicializar puerto B en 0
   port_b = 0x00;
   
   while(TRUE)
   {
      i = read_adc();
   
      if(i > 500)
      {
         output_high(PIN_B0);
      }
      else
      {
         output_low(PIN_B0);
      }
   }
}
