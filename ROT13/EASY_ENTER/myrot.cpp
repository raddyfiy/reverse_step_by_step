#include <stdio.h>
#include <string.h>
#include <malloc.h>


#define FORWORD_FW "./myrot.exe"
char * chunkdata=(char *)malloc(100);
int creatchunkdata(char * chunkdata){//X6X3L_iekdj1RKFEDFF49zoqsqq2eD
    memset(chunkdata,0,100);
    char * tmp=(char *)malloc(100);
    memset(tmp,0,100);
    for(int i=1;i<40;i++){
        if(i%8==0){
            tmp[i]=(i%5)+0x30;
            continue;
        }
        tmp[i]=((tmp[i-1]*2)/3+35)^i;
    }
    int j=0;
    for(int i=5;i<35;i++){
        chunkdata[j]=tmp[i];
        j++;
    }
    chunkdata[1]=0x36;
    chunkdata[20]=0x39;
    // puts(chunkdata);
    return 0;
}




int rrrrrrrrrrrot(char * input){
    int inputlen=strlen(input);
    if(inputlen<10){
        return 0;
    }
    int i;
    for(i=0;i<inputlen;i++){
        if(input[i]>='A' && input[i]<='Z'){
            input[i]=((input[i]-'A'+13)%26)+'A';
        }
        if(input[i]>='a' && input[i]<='z'){
            input[i]=((input[i]-'a'+13)%26)+'a';
        }
    }
    for(i=0;i<inputlen;i++){
        if(input[i]!=chunkdata[i]){
            return 0;
        }
    }
    return 1;
}



int main(void){
    char * p,*output;
    int retn;
    p=(char *)malloc(100);
    output=(char *)malloc(100);
    puts("input your fucking flag:");
    gets(p);
    // printf(p);
    strcpy(output,p);
    creatchunkdata(chunkdata);
    retn=rrrrrrrrrrrot(output);
    if(retn){
        puts("Right!!");
        printf("%s%s%s","flag{",p,"}\n"); //K6K3Y_vrxqw1EXSRQSS49mbdfdd2rQ
    }
    else{
        puts("Wrong!!");
    }
    return 0;
}