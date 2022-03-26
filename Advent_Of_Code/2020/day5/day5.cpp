#include <iostream>
#include <string>
#include <vector>

#include "utilities.cpp"

using namespace std;

#define ROWMAX 127
#define COLMAX 7

void doPart1(vector<string>);

vector<int> getSeatIds(vector<string>);
int calculateSeat(string);

int calculateRow(string);
int calculateCol(string);

void doPart2(vector<string>);

int findMissing(vector<int>);

int main(){

    vector<string> seats = openAndReadFile("input");
    
    doPart1(seats);
    doPart2(seats);

}

void doPart1(vector<string> seats){

    vector<int> seatIds = getSeatIds(seats);

    int maxValue = *max_element(seatIds.begin(), seatIds.end()); //returns a pointer to the max_value

    cout << "max value: " << maxValue << endl;

}

vector<int> getSeatIds(vector<string> seats){
    vector<int> seatIds;

    for(string seat : seats){
        int seatID = calculateSeat(seat);
        seatIds.push_back(seatID);
    }
    return seatIds;
}

int calculateSeat(string seat){
    
    string rowCharacter = string(seat.begin(), seat.begin()+7);
    int rowNumber =  calculateRow(rowCharacter);

    string colCharacter = string(seat.begin()+7, seat.end());
    int colNumber =  calculateCol(colCharacter);

    int seatID = rowNumber * 8 + colNumber;

    return seatID;

}

int calculateRow(string seat){
    
    int min = 0;
    int max = ROWMAX;
    
    // B means take UPPER Half
    // F means take LOWER Half

    for(char c : seat){
        if(c == 'B')
            min = (min+max)/2 + 1;
        if(c == 'F')
            max = (min+max)/2;
    }
    return min;
}

int calculateCol(string seat){
    
    int min = 0;
    int max = COLMAX;
    
    // R means take UPPER Half
    // L means take LOWER Half

    for(char c : seat){
        if(c == 'R')
            min = (min+max)/2 + 1;
        if(c == 'L')
            max = (min+max)/2;
    }
    return min;
}

void doPart2(vector<string> seats){

    vector<int> seatIds = getSeatIds(seats);
    sort(seatIds.begin(), seatIds.end());

    int missing = findMissing(seatIds);
    cout << "missing: " << missing << endl;

}

int findMissing(vector<int> seatIds){
    int offset = seatIds[0];
    for(int i = 0; i < seatIds.size() ; i++){
        if(seatIds[i] != i + offset){
            return i + offset;
        }
    }
}