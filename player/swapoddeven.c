#include<stdio.h>
int main(void)
{
char n[10];
int i,j,temp;
scanf("%s",n);
for(i=0,j=1;n[i]!='\0';i=i+2,j=j+2)
{
temp=n[i];
n[i]=n[j];
n[j]=temp;
}
printf("%s",n);
return 0;
}
