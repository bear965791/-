#include <stdio.h>
#include <stdlib.h>

//enum的預設值由0開始
typedef enum {black_ops,top_secret,secret,non_secret} securitylevels;

//*s1代表傳入指向array s1的起始位子，也就是指向第一個字元'N'
void f1(char *s1,char *s2){
    for(; *s1 != '\0'; s1++);  //當S1找到第一個null character跳出迴圈,此時*s1指向第一個null character位子
    for(; *s2 != '\0'; *s1 = *s2, s1++, s2++);  //將s2不為null的字元都放入s1中
    *s1 = '\0';
}

securitylevels f2(){
    return (non_secret - black_ops) / 3 < secret ? black_ops : non_secret;
}

int getValue(int A[][2], int B[][2], int n, int row, int column){
    int value = 0;
    for(int k = 0; k < n; k++){
        value = value + A[row][k] * B[k][column];
    }
    return value;
}

void f3(int A[2][2], int B[2][2], int C[2][2],int n){
    for (int row = 0; row < n; row++){
        for(int column = 0; column < n; column++){
            C[row][column] = getValue(A,B,n,row,column);
        }
    }   
}

//將整數i的記憶體位置assign給p,再assign給q,return 20+1=21
int f4(int i){
    int *p = &i, *q = p;
    return ++(*q);
}

double f5(int a, int b){
    double t = ((a--) / 3 + b % 4);
    return t;
}

void f6(int D[], int n){
    int i = 0, m = 0;
    m = n >> 4; //除16
    m = m << 4; //乘16
    for (int i = 7; i >= 4; i--){
        D[i] = (m & (1 << i)) ? 1 : 0;  //不等於0就是true
        printf("%d\n", 1 << i);
        printf("%d\n", (m & (1 << i)));
        printf("%d\n", D[i]);
    }
}

int main(){
    char s1[100] = "NTUT", s2[100] = "Good";
    int A[2][2] = {{1,2}, {2,1}}, B[2][2] = {{1,2}, {2,3}}, C[2][2], D[10];
    f1(s1,s2);
    printf("%s\n", s1);
    printf("%d\n", f2());
    f3(A, B, C, 2);
    printf("%d %d\n", C[0][0], C[1][1]);
    printf("%d\n", f4(20));
    printf("%3.2f\n", f5(6, 6)); //3.2f指小數點前有三位數,小數點後有兩位數
    f6(D, 123);
    printf("%d%d%d\n", D[1], D[3], D[5]);
}