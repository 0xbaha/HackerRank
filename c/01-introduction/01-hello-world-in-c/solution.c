#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    // scanf("%[^\n]%*c", &s);
    fgets(s, sizeof(s), stdin);

  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    printf("Hello, World!\n%s",s);
    return 0;
}