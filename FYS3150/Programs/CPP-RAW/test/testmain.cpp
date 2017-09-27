#include <iostream>     //For printing with cout
#include <fstream>      //For file read
#include <string>
#include <sstream>

using namespace std;

int main ()
{
    for(int i = 1; i < 11; i += 1)
    {
        std::ostringstream iss;
        iss << "table" << i << ".dat";
        std::string filename = iss.str();
        ofstream infile;                                      //Naming the file representation
        infile.open( filename.c_str());                       //Connecting name to file
        infile << "multiplication table for " << i << endl;
        for(int j = 1; j < 11; j+=1)
        {
            infile << j*i << endl;
        }
        infile.close();       //Closing the file
    }
    return 0;
}
