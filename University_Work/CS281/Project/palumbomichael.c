int print_int (int value)
 {
  int code;
  code = 1;
  asm (
       "add $a0,%1,$zero\n\t"
       "add $v0,%0,$zero\n\t"
       "syscall"
       :
       : "r" (code), "r" (value));
  return value;
 }

int print_str (char* str)
 {
  int code;
  code = 4;
  asm (
       "add $a0,%1,$zero\n\t"
       "add $v0,%0,$zero\n\t"
       "syscall"
       :
       : "r" (code), "r" (str));
  return 0;
 }

int global_ra;

char* string1 = "start fun 1\n";
int fun1 (int x)
 {
 global_ra = *(&x - 1);
 print_str(string1);
 return 1;
 }

char* string2 = "start fun 2\n";
int fun2 (int x)
 {
 *(&x - 1) = global_ra;
 print_str(string2);
 return 2;
 }

char* stringerr = "we should never get here\n";
int main (int argc, char** argv) 
 {
 int v = fun1(10);
 print_int(v);
 if (v == 2) return(2);
 v = fun2(10);
 print_str(stringerr);
 return(1);
 }