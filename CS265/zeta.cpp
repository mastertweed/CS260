#include <math.h>
#include <stdio.h>
#include <iostream>

using namespace std;

int main( int argc, char **argv) {

int x;
int n;

cout << "Enter Value for x: ";
cin >> x;
cout << "Enter Value for n: ";
cin >> n;
 
float total = 0;

for (int i=0; i<n; i++){
	total = total + pow((1.0/(float(i)+1.0)),float(x));
}

cout << "z(" << x << ")=" << total << " when approximated at n=" << n << "\n";
return 0;
}
