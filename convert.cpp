#include <iostream>
using namespace std;

void Convert(int value, int &hour, int &minute, int &seconds)
{

    hour = value / 3600;    // hours
    minute = (value % 3600) / 60;   // minutes
    seconds = value % 60;   // seconds

}

int main()
{
    int hour;
    int seconds;
    int minute;
    int seconds_convert;
    cout << "Enter a number of seconds to convert: ";
    cin >> seconds_convert;

    Convert(seconds_convert, hour, minute, seconds );

    cout << hour <<" hours and " << minute << " minutes " << "and " << seconds << " seconds";
    return 0;
}
