/* I made this program for Project 1 in the course
 FYS3150 - Computational Physics. Enjoy. */

#include <cmath>        //For math
#include <iostream>     //For printing with cout
#include <fstream>      //For file read
#include <algorithm>    //For filling arrays
#include <ctime>        //For calculating run time

using namespace std;

double func (double x)
/* This is a function which takes
 * a float number 'x' as argument
 * and returns f(x)=100e^-10x */
{
    double r;
    r = 100*exp(-10*x);
    return r;
}
double exact(double x)
/* This is the analytical solution
 * of the function above */
{
    double r;
    r = 1-(1-exp(-10))*x-exp(-10*x);
    return r;
}
double log10(double vi, double ui)
{
    return log10(fabs((vi-ui)/ui));
}


void solver1(double *u, int N)
{
    double *A = new double[N];
    A[0] = 2;
    F[0] = 0;

    for(int i = 1; i < N-1; i += 1)
    {
        double k = i*(h);
        f[i]=pow(h,2)*func(k);       // Filling f
        A[i]=(i+1)/double (i);       // Atilde
        f[i]=f[i]-f[i-1]/A[i-1];     // Ftilde
    }
}

int main ()
{
    //Constant
    int N = pow(10,6);                          //Number of iterations
    double h = 1./(N+1);                        //Step length

    clock_t start, finish;                      //Declare start and final time
    start = clock();

    //Arrays

    int a = 2; int bc=-1;                       //bc=b=c=-1
    double *f = new double[N];
    double *u = new double[N];
    double *atilde = new double[N];
    double *ftilde = new double[N];
    /* Mark: Here I make dynamical arrays with N/N-1 elements */

    //Set initial conditions
    atilde[0]=a;
    ftilde[0]=pow(h,2)*func(0);      //Set initial condition

    //Interation loops to fill the arrays
    for(int i = 0; i < N+1; i += 1)
    {
        double k = i*(h);
        f[i]=pow(h,2)*func(k);       //Filling f
    }


    for(int i = 1; i < N+1; i += 1)
    {
        atilde[i]=a-bc*bc/atilde[i-1];
        ftilde[i]=f[i]-ftilde[i-1]*bc/atilde[i-1];
    }

    //Solve U and write out to file
    u[N-2]=ftilde[N-2]/atilde[N-2];     //Set initial conditions for u
    u[N-1]=0;
    u[0]=0;
    ofstream infile;                    //Giving the file representation name
    infile.open("doubder.dat");         //Connecting name to file
    for(int j = N-3; j > 0; j -= 1)
    {
        double k = j*h;
        u[j]=(ftilde[j]-bc*u[j+1])/atilde[j];
        infile << u[j] << "    " << exact(k) << endl;
    }
    infile.close();
    finish = clock();
    cout << "Run time: " << (finish-start)/float(CLOCKS_PER_SEC) << "s" << endl;

    //double* u_special = new double[N];
    //solver1(u_special,N)
    //cout << u_special[N/2] << endl;

    return 0;
}

