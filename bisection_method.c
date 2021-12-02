#include<stdio.h>
#include<curses.h>
#include<math.h>
//#include<conio.h>

//#define (x) (x*x*x - 4*x -9)
float ff(){
    //printf(x*x*x - 4*x -9);
    return(1.5);

}
void main(){
  float a,b,c,d,e,test;
  //clrscr();
  pp:
    printf("please enter any two numbers: ");
    scanf("%f %f", &a, &b);
    
    printf("please enter the value of e: ");
    scanf("%f", &e);
    //test=f(1);
    a=ff();
    printf(&a);
    /*if (f(a) * f(b)>0)
        goto pp;

    do{
        c=(a+b)/2;
        if (f(a)*f(c)<0)
            b=c;
        else
            a=c;
    } while(fabs(f(c))>e);
    printf("Required root = %f", c);
    printf("\n f(c) = %f", f(c));
    getch();*/
}