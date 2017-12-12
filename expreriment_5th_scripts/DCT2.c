#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ImageSize 8
#define BUFFER_SIZE 256 
#define PI  3.141592653589 

double max=0.0;
int max_x=0;
int max_y=0;

double F[ImageSize][ImageSize];

void load_pgm_data(char fname[256], 
                   int Image[ImageSize][ImageSize])
{
  FILE *fp;
  int mode;
  char buffer[BUFFER_SIZE];
  int width, height, depth;
  int x,y;

  if((fp=fopen(fname,"r"))==NULL){
    printf("Cannot open \"%s\"\n",fname);
    exit(1);
  }
  fgets(buffer,BUFFER_SIZE,fp);
  if(buffer[0]!='P' || !(buffer[1]=='2' || buffer[1]=='5')){
    printf("The file is not PGM (P2 or P5).\n");
    exit(1);
  }\
  else if(buffer[1]=='2'){
    mode=0;
  }
  else if(buffer[1]=='5'){
    mode=1;
  }

  fscanf(fp,"%d %d",&width,&height);
  fscanf(fp,"%d",&depth);

  if(width != ImageSize || height != ImageSize){
    printf("Size is not different.\n");
    exit(0);
  }

  for(y=0;y<ImageSize;y++){
    for(x=0;x<ImageSize;x++){
      if(mode==0){
        fscanf(fp,"%d ",&Image[y][x]);
      } 
      else if(mode==1){
        Image[y][x]=(unsigned char)fgetc(fp);
      }
    }
  }
  fclose(fp);
}

void DCT(int Image[ImageSize][ImageSize]){
  double C[ImageSize];
  int i,u,v,x,y;

  for(i=0;i<ImageSize;i++){
    C[i]=1;
    if(i==0){
      C[i]/=sqrt(2.0);
    }
  }
  
  for(x=0;x<ImageSize;x++){
    for(y=0;y<ImageSize;y++){
      Image[x][y]-=127.5;
    }
  }
  for(u=0;u<ImageSize;u++){
    for(v=0;v<ImageSize;v++){
      F[u][v]=0;
      for(x=0;x<ImageSize;x++){
	for(y=0;y<ImageSize;y++){
	  F[u][v]+=Image[x][y]
	    *cos((2*x+1)*u*PI/16.0)*cos((2*y+1)*v*PI/16.0);
	}
      }
      F[u][v]*=((1/4.0)*C[u]*C[v]);
      
      // Original
      if(F[u][v]>max){
        max=F[u][v];
	max_x=u;
	max_y=v;
      }
    }
  }

  

  /* printf("                               v\n");
  printf("   ");
  for(u=0;u<ImageSize;u++){
    printf("   %d   ", u);
  }
  printf("\n");
  for(u=0;u<ImageSize;u++){
    if(u==4) printf("u %d ",u);
    else printf("  %d ", u);
    for(v=0;v<ImageSize;v++){
      printf("%6.1lf ",F[u][v]);
    }
    printf("\n");
  }*/
}

int main(int argc, char* argv[]){
  int i, j, u ,v;
  int Image[ImageSize][ImageSize];

  if(argc!=2){
    printf("./dct pgm_file\n");
    exit(1);
  }

  load_pgm_data(argv[1],Image);
  DCT(Image);

  printf("max: %6.1f, (u, v)=(%d, %d)\n", max, max_x, max_y);

  exit(0);
}
