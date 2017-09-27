/* This is the program for the warmup
exercises given in the start of the
semester */

#include <cmath>        //For math
#include <iostream>     //For printing with cout
#include <fstream>      //For file read
#include <iomanip>      //For digit precision
#include <string>       //For string operation
#include <sstream>      //for ostringstream

using namespace std;

double f (double a)
/* This is a function f which takes
 * a float number 'a' as argument
 * and returns arctan 'a' */
{
    double r;
    r=atan(a);
    return r;
}

double derivation1 (double x, double h)
/* This function calculates the
 * derivated of the function f in
 * the point 'x' with 'h' steplength
 * by Forward-Euler */
{
    double r;
    r=(f(x+h)-f(x))/h;
    return r;
}

double derivation2 (double x, double h)
/* This function calculates the
 * derivated of the function f in
 * the point 'x' with 'h' steplength
 * by the 3-Point method */
{
    double r;
    r=(f(x+h)-f(x-h))/(2*h);
    return r;
}

int main ()
{
    double h = pow(10,-7); double step = pow(10,-11);     //Constants to deal with h
    for(int i = 0; i < 2; i=i+1)
    {
        double z;                                             //Variables for storing the derivated
        std::ostringstream text;
        text << "der" << i+1 << ".dat";
        std::string filename = text.str();
        ofstream infile;                                      //Naming the file representation
        infile.open( filename.c_str());                       //Connecting name to file
        infile << "#h      derivation value\n";               //Writing head line in file

        for(h; h > step; h -= step)
        /* This for loop counts from 10^-7 to 10^-11 with timestep 10^-11
         * I prefer to make h smaller and smaller because I want to see
         * the error sink. */
        {
            if(i==0)
            {
                z=derivation1(sqrt(2),h);
                infile << h << "  " << std::setprecision(10) << z << endl;
            }
            else
            {
                z=derivation2(sqrt(2),h);
                infile << h << "  " << std::setprecision(10) << z << endl;
            }
        }
        infile.close();       //Closing the file
        cout << "The relative error is " << fabs(z-1/3.) << " for method " << i << endl;
    }
    return 0;
}
