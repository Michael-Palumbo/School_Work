#include <iostream>
#include <list>
#include <fstream>
#include <string>
#include <stdexcept>

using namespace std;

#define TARGET_NUMBER 2020

void openAndReadFile(list<int> &);
void readFile(ifstream &, list<int> &);
void doPart1(list<int>);
void doPart2(list<int>);
void printList(list<int>);

int main(){

    list<int> items;

    openAndReadFile(items);

    doPart1(items);

    doPart2(items);

    // printList(items);

    return 0;
}

void openAndReadFile(list<int> &items){
    ifstream myFileStream;
    myFileStream.open("input");

    if( myFileStream.is_open() ){
        readFile(myFileStream, items);
    }
    myFileStream.close();
}

void readFile(ifstream &myFileStream, list<int> &items){
    string myString;

    while(myFileStream.good()){
        myFileStream >> myString;
        int number = stoi(myString);
        items.push_back(number);
    }
}

void doPart1(list<int> items){
    for(int item1 : items){
        for(int item2 : items){
            if (item1 + item2 == TARGET_NUMBER){
                int multi = item1 * item2;
                cout << "Part 1: " << item1 << " * " << item2 << " = " << multi << '\n'; 
            }
        }
    }
}

void doPart2(list<int> items){
    for(int item1 : items){
        for(int item2 : items){
            for(int item3 : items){
                if (item1 + item2 + item3 == TARGET_NUMBER){
                    int multi = item1 * item2 * item3;
                    cout << "Part 2: " << item1 << " * " << item2 << " * " << item3 << " = " << multi << '\n'; 
                }
            }
        }
    }
}

void printList(list<int> items){
    cout << "items { ";
    for(int item : items){
        cout << item << ", ";
    }
    cout << "}; \n";
}