/* In this project I will try to make
 * a function which takes in a array
 * and gives out the determinant */

#include <iostream>

using namespace std;

int main()
{
    //Define matrix
    int N = 3;
    double A[N][N];
    A[0][0] = 1; A[0][1] = 2; A[0][2] = 4;
    A[1][0] = 3; A[1][1] = 8; A[1][2] = 14;
    A[2][0] = 2; A[2][1] = 6; A[2][2] = 13;

    double L[N][N]; double U[N][N];

    for(int i = 0; i < N; i++){
        for(int  j = 0; j < N; j++){
            //U_1j
            U[0][j] = A[0][j];

            //U_ij
            if(j > i){
                double Lik = 0; double Ukj = 0;
                for(int k = 0; k < (i-1); k++){
                    Lik += L[i][k];
                    Ukj += U[k][j];
                }
                U[i][j]=A[i][j]-Lik*Ukj;
            }
            else{
                U[i][j]=0;
            }


            //U_jj
            double Ljk = 0; double Ukj = 0;
            for(int k = 0; k < (j-1); k++){
                Ljk += L[j][k];
                Ukj += U[k][j];
            }
            U[j][j]=A[j][j]-Ljk*Ukj;

            //L_ij
            if(i > j){
                double Lik = 0; Ukj = 0;
                for(int k = 0; k < (i-1); k++){
                    Lik += L[i][k];
                    Ukj += U[k][j];
                }
                L[i][j]=(A[i][j]-Lik*Ukj)/U[j][j];
            }
            else{
                L[i][j]=0;
                //cout << "see me" << endl;
            }
        }
    }
    return 0;
}

