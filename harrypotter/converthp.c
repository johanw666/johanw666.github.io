#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char* argv[])
{
  int i;
  FILE* fin;
  FILE* fout;
  char err_buf[128];
  char line_buf_in[100000];
  char line_buf_out[100000];

  if (argc != 3) {
    sprintf(err_buf, "Usage: %s filein fileout\n", argv[0]);
    printf(err_buf);
    exit(0);
  }

  fin = fopen(argv[1], "rt");
  if ( !fin ) exit(1);
  fout = fopen(argv[2], "wt");
  if ( !fout ) {
    fclose(fin);
    exit(2);
  }

  while ( fgets(line_buf_in, sizeof(line_buf_in) - 1, fin) ) {
    i = 0;
    while ( isspace(line_buf_in[i]) ) i++;
    strcpy(line_buf_out, line_buf_in + i);
    fprintf(fout, line_buf_out);
    fprintf(fout, "\n");
  }
  fclose(fin);
  fclose(fout);
}

