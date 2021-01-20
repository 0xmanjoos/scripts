#include <iostream>
double recurse(double input){ return (input==1) ? 1 : recurse(input-1)*input; }
int main(){
    std::cout<<recurse(5);
}
