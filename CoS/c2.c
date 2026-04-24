// by Bobban / DFR Research & Engineering
// from http://fravia.org/saruma1.htm - thanks guys
//
//  with minor modifications to work on non-pc
//  boxes and with the cmlam-nanny's slightly different formats
//  takes input from stdin
//
#include <stdio.h>
#include <stdlib.h>

typedef unsigned long ulong;
typedef unsigned char byte;

        ulong   key = 0xDEADL;

void decrypt_line(char *inbuff, char *outbuff)
{
        int     in_count , out_count = 0,len;
        byte    ch1,ch2;
        ulong   subkey1,subkey2;
        len = strlen(inbuff)/2;

        for (in_count = 0; in_count < len ; in_count++) {
                subkey1 = key;
                subkey1 = (subkey1 >> 4) & 0x1fL;
                subkey2 = key;
                subkey2 = (subkey2 >> 8) & 0x1fL;
                ch2 = *(inbuff+in_count*2+1);
                ch2 ^= subkey2;
                ch2 = (ch2 & 0x0f) << 4;
                ch1 = *(inbuff + in_count*2);
                ch1 ^= subkey1;
                ch1 &= 0x0f;
                ch1 |=ch2;
                outbuff[out_count] = ch1;
                key += 0x100L - (ulong)ch1;
                ++out_count;
        }
        outbuff[out_count] = 0;
}
int
readit(char *inbuff,FILE *infile)
{
	int count, c;
	count = 0;
	for (;;) {
		c = fgetc(infile);
		if (c < 0) {
			if (count == 0)
				return(0);
			break;
		}
		if (c == '\n' || c == '\r') {
			if (count == 0)
				continue;
			break;
		}
		*inbuff++ = c;
		count++;
	}
	*inbuff = 0;
	return(1);
}

int main (void)
{
        FILE    *infile;
        char    inbuff[400];
        char    outbuff[400];
        //clrscr();

        infile = stdin;
           while(readit(inbuff,infile)) {
                decrypt_line(inbuff,outbuff);
                printf("%s\n",outbuff);
           }

        close(infile);
        return 0;
}
