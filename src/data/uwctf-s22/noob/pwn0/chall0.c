#include <stdio.h>
#include <stdlib.h>

void hack_me()
{
    char buf[0x10];
    int auth = 0;

    gets(buf);

    if(auth){
        system("/bin/cat ./flag.txt");
    }
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    puts("Welcome to Buffer Overflow 0");
    puts("Can you hack me?");
    hack_me();
}
