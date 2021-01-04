#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <string>

using namespace std;

void vec(){
	vector<int> bigboy;
	for (int i = 1; i < 10;i++) {
		bigboy.push_back(i);
	}
	cout << "Size of vector: "<<bigboy.size() << endl;
}

void file(){

	string data, name;

	cout <<"Enter the name of the new file: ";cin>>name;

	ofstream outfile;
	outfile.open(name);

	cout << "\nEnter the data you want to write: ";cin>>data;

	outfile << data << endl;
	outfile.close();
	cout <<"\ndata written to: "<<name<<"\n\nNow reading from: "<<name<<endl;

	ifstream infile;
	infile.open(name);
	cout <<"\nreading from file: \n"; infile>>data ;cout <<data<<endl;

}
double except(int x, int y) {
	if ( x==0 || y==0) {
		throw "Division by zero condition!";
	}
	double z = x / y;
	return z;
}

int main() {

	int input;
	cout<<"STD_LIBRARY\n[1] Vector\n[2] Fstream\n[3] Exception\nEnter: "; cin >> input;
	switch (input) {
		case 1:
			vec();
			break;
		case 2:
			file();
			break;
		case 3:
			try {
				double asc, asc2;
				cout<<"Enter a number: ";cin>>asc;cout<<"Enter another number: ";cin>>asc2;
				cout<<except(asc, asc2) << endl;
			} catch (const char* msg) {
				cerr <<msg <<endl;
			}
			break;
		default:
			cout<<"Enter a number you dumb brain fuck all retard" << endl;
	}
	return 0;
}
