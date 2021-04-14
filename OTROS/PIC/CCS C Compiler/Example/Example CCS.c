// PIC16F877A LED blink example
// https://simple-circuit.com/
 
#include <16F877A.h>
#use delay(crystal=20000000)
 
void main()
{
   while(TRUE)
   {
      output_toggle(PIN_B0);    // Toggle output pin RB0
      delay_ms(500);
   }
}
